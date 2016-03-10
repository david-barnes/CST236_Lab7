""" pluging file for writing the requirements and job stories
    to an output file
"""

from nose2.events import Plugin

# pylint: disable=no-init
# plugin class is for config file
# pylint: disable=no-self-use
# function called outside of program
# pylint: disable=too-few-public-methods
# file is used by the program to create an after summary report
# so no need for public access
# pylint: disable=invalid-name
# dicts are used by multiple functions and are therefore constants

class RequirementTrace(Plugin):
    """ pluging class for writing to an output file """
    configSection = "req-tracer"

    def after_summary_report(self, dummy):
        """ function for writing to the output file """
        output_file = open("Project_Traces.txt", "w")
        output_file.write("Requirements\n")
        output_file.write("************\n\n")
        for key, item in sorted(Requirements.items()):
            output_file.write(key+':'+'\n')
            for func in item.func_name:
                output_file.write('\t'+func+'\n')
            output_file.write('\n')
        output_file.write("\nJob Stories\n")
        output_file.write("***********\n\n")
        for job in Stories:
            output_file.write(job.js_text+':'+'\n')
            for func in job.func_name:
                output_file.write('\t'+func+'\n')
            output_file.write('\n')


class RequirementTraceObj(object):
    """ class for accessing the Requirement dict """
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []


class JSTrace(object):
    """ class for accessing the Stories dict """
    js_text = ""

    def __init__(self, text):
        self.js_text = text
        self.func_name = []


Requirements = {}

Stories = []

def requirements(req_list):
    """ function for adding to the Requirements dict """
    def wrapper(func):
        """ function for adding to the Requirements dict """
        def add_req_and_call(*args, **kwargs):
            """ function for adding to the Requirements dict """
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


def story(job_story):
    """ function for adding to the Stories dict """
    def wrapper(func):
        """ function for adding to the Stories dict """
        def add_job_and_call(*args, **kwargs):
            """ function for adding to the Stories dict """
            for job in Stories:
                if job.js_text == job_story:
                    job.func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_job_and_call

    return wrapper

with open('project_requirements.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTraceObj(desc)
        if line[0] == '*':
            job_id = line[1:].strip()
            Stories.append(JSTrace(job_id))
