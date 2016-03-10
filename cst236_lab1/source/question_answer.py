""" QA class source file """
#pylint: disable=too-few-public-methods
# as this class is used internally by the main program
# I don't see why it would need any public methods

class QA(object):
    """ QA classs for getting answers to questions """
    def __init__(self, question, answer):
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer
