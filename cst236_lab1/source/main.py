""" main program file """

from datetime import datetime
import time
import getpass
import difflib
from source.answers import fibonacci, calc_pi, conversion, \
    can_convert, i_know, get_triangle_area, get_quadrilateral_area, \
    calculate_tip, calculate_sales_tax, days_to_christmas
from source.git_utils import is_file_in_repo, get_git_file_info, \
    get_file_info, get_repo_branch, \
    get_repo_url
from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_corners_type

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    """ interface class for asking questions and teaching/correcting answers """
    def __init__(self):

        self.keywords = ["Convert", "Is", "How", "Open", "Please",
                         "What", "When", "Where", "Who", "Why"]
        self.question_mark = chr(0x3F)

        self.question_answers = {
            "What type of triangle is ": QA("What type of triangle "
                                            "is ", get_triangle_type),
            "What is the area of triangle with sides ":QA("What is the "
                                                          "area of triangle with sides ",
                                                          get_triangle_area),
            "What type of quadrilateral is ": QA("What type of "
                                                 "quadrilateral is ",
                                                 get_quadrilateral_corners_type),
            "What is the area of quadrilateral with sides and "
            "angles ": QA("What is the area of quadrilateral with "
                          "sides and angles ", get_quadrilateral_area),
            "What time is it ": QA("What time is it ",
                                   datetime.now().strftime("%m-%d-%Y %H:%M:%S")),
            "What is the digit of fibonacci ": QA("What is "
                                                  "the digit of fibonacci", fibonacci),
            "What is the digit of pi ": QA("What is the "
                                           "digit of pi", calc_pi),
            "Please clear memory": QA("Please clear memory", self.clear),
            "Open the door Hal": QA("Open the door Hal",
                                    "I'm afraid I can't do that "+getpass.getuser()),
            "What units can I convert": QA("What units can I convert", can_convert),
            "When does Half-Life 3 come out":QA("When does "
                                                "Half-Life 3 come out",
                                                "ha ha ha, as if that will ever happen."),
            "Why is it called the Legend of Zelda when you "
            "play as Link": QA("Why is it called the Legend of "
                               "Zelda when you play as Link", "Becuase every princess "
                               "is named Zelda after the in-game legend about the first"
                               " princess, who was named Zelda."),
            "What is the meaning of life, the universe, and everything":
                QA("What is the meaning of life, the universe, and everything", "42"),
            "What do you know": QA("What do you know", i_know),
            "How do I make a PBJ 2.0": QA("How do I make a PBJ 2.0",
                                          "On the bottom bun in vertical rows place creamy peanut-"
                                          "butter, nutella, and crunchy peanut-butter. Then on the "
                                          "top bun in horizontal rows place jelly/jam, honey, and "
                                          "marshmellow spread."),
            "How much is a percent tip on a bill of ": QA("How much is a percent tip on a bill of ",
                                                          calculate_tip),
            "What is the total bill on if the sales tax is percent":
                QA("What is the total bill on if the sales tax is percent", calculate_sales_tax),
            "How many day until Christmas":
                QA("How many days until Christmas", days_to_christmas),
            "Is the in the repo": QA("Is the in the repo", is_file_in_repo),
            "What is the status of ": QA("What is the status of ", get_git_file_info),
            "What is the deal with ": QA("What is the deal with ", get_file_info),
            "What branch is ": QA("What branch is ", get_repo_branch),
            "Where did come from": QA("Where did come from", get_repo_url)
        }
        self.last_question = None


    def ask(self, question=""):
        """ function for asking questions """
        #pylint: disable=too-many-statements
        # 51 statements is not too many for what is done in this function
        #pylint: disable=too-many-branches
        # 14 branches is not too many as this function does quite a bit of stuff
        # pylint: disable=bare-except
        # I have no clue how to fix this without breaking the code
        # pylint: disable=useless-else-on-loop
        # if the question is not in question_answers then it would drop into
        # the else section, and I don't know how to change without breaking

        start = time.clock()
        outputfile = open("Log_file.txt", 'a')
        outputfile.write(str(question)+":\n")

        if not isinstance(question, str):
            self.last_question = None
            outputfile.write("Not A String!"+"\n")
            proc_time = time.clock() - start
            outputfile.write(str(proc_time)+'\n\n')
            raise Exception('Not A String!')
        if question.split(' ')[0] == 'Convert':
            measure = question.split(' ')
            convert = conversion(measure[1], measure[2], measure[4])
            outputfile.write(convert+'\n')
            proc_time = time.clock() - start
            outputfile.write(str(proc_time)+"\n\n")
            return convert
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            outputfile.write(NOT_A_QUESTION_RETURN+"\n")
            proc_time = time.clock() - start
            outputfile.write(str(proc_time)+'\n\n')
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    if keyword[0] == '<' and keyword[-1] == '>':  #assuming file path has no spaces
                        path = keyword[1:len(keyword)-1]
                        args.append(path)
                    else:
                        args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        outputfile.write(str(answer.value)+'\n\n')
                        return answer.value
                    else:
                        try:
                            check = answer.function(*args)
                            outputfile.write(str(check)+'\n')
                            proc_time = time.clock() - start
                            outputfile.write(str(proc_time)+'\n\n')
                            return check
                        except Exception as exc:
                            outputfile.write("Error: "+str(exc)+'\n')
                            proc_time = time.clock() - start
                            outputfile.write(str(proc_time)+'\n\n')
                            raise Exception("Error: "+str(exc))
            else:
                outputfile.write(UNKNOWN_QUESTION+'\n')
                proc_time = time.clock() - start
                outputfile.write(str(proc_time)+'\n\n')
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        """ function for teaching answers for asked questions """
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        """ function for correcting taught answers """
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    def clear(self):
        """ function for reseting known questions """
        self.question_answers = 0
        self.__init__()
