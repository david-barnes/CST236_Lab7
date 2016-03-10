"""
Test for source.main.py
"""
from unittest import TestCase
from source.main import Interface
from test.plugins.ReqTracer import requirements


class TestAskingQuestions(TestCase):
    """ Test cases for asking questions """

    @requirements(['#0006', '#0007'])
    def test_ask_question(self):
        """ test to see if program knows the question """
        attempt = Interface()
        result = attempt.ask("How are you?")
        self.assertEqual(result, "I don't know, please provide the answer")


    @requirements(['#0008'])
    def test_ask_question_no_keyword(self):
        """ test asking a question without a keyword """
        attempt = Interface()
        result = attempt.ask("Can I ask you a question?")
        self.assertEqual(result, "Was that a question?")


    @requirements(['#0009'])
    def test_ask_question_no_mark(self):
        """ test asking a question without a question mark """
        attempt = Interface()
        result = attempt.ask("How are you")
        self.assertEqual(result, "Was that a question?")


    @requirements(['#0006'])
    def test_ask_question_with_int(self):
        """ test passing an int instead of a string """
        attempt = Interface()
        with self.assertRaises(Exception, msg="Not A String!"):
            attempt.ask(42)


class TestAsweringQuestions(TestCase):
    """ Test cases for answering questions """

    @requirements(['#0001', '#0002', '#0010', '#0012', '#0013'])
    def test_ask_question_with_answer(self):
        """ test askingf a question with a known answer """
        attempt = Interface()
        result = attempt.ask("What type of triangle is 2 2 4?")
        self.assertEqual(result, "isosceles")

    @requirements(['#0010', '#0011', '#0012', '#0013'])
    def test_ask_partial_question(self):
        """ test asking a partial question """
        attempt = Interface()
        result = attempt.ask("What type of triangle has 2 2 4?")
        self.assertEqual(result, "isosceles")

    @requirements(['#0003', '#0004', '#0005'])
    def test_ask_question_quadrilateral(self):
        """ test asking if the program can identify the
        quadrilateral with given sides and angles """
        attempt = Interface()
        result = attempt.ask("What type of quadrilateral is 3 3 3 3 60 120 60 120?")
        self.assertEqual(result, "rhombus")

    @requirements(['#0014'])
    def test_ask_question_no_answer(self):
        """ test asking a question with no known answer """
        attempt = Interface()
        result = attempt.ask("How many sides does a quadrilateral have?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0012'])
    def test_exception_parameters(self):
        """ exception test for passing too many parameters """
        attempt = Interface()
        with self.assertRaises(Exception, msg="Too many extra parameters"):
            attempt.ask("What type of triangle is 2 2 4 4?")


class TestTeachingAnswers(TestCase):
    """ Test cases for teaching answers """

    @requirements(['#0015', '#0016'])
    def test_giving_answer(self):
        """ test teaching an answer """
        attempt = Interface()
        question = "How many sides does a quadrilateral have?"
        attempt.ask(question)
        attempt.teach("four sides.")
        result = attempt.ask(question)
        self.assertEqual(result, "four sides.")

    @requirements(['#0017'])
    def test_giving_answer_no_question(self):
        """ test teaching an answer without asking a question first """
        attempt = Interface()
        result = attempt.teach("four sides.")
        self.assertEqual(result, "Please ask a question first")

    @requirements(['#0018'])
    def test_giving_answer_known(self):
        """ test teaching an answer to a question with a known answer  """
        attempt = Interface()
        question = "What type of quadrilateral is ?"
        attempt.ask(question)
        result = attempt.teach("square")
        self.assertEqual(result, "I don't know about that. I was taught differently")


class TestCorrectingAnswers(TestCase):
    """ Test cases for correcting taught answers """

    @requirements(['#0019', '#0020'])
    def test_correcting_answer(self):
        """ test correcting an answer """
        attempt = Interface()
        question = "How many sides and corners does a quadrilateral have?"
        attempt.ask(question)
        attempt.teach("four sides.")
        attempt.correct("four sides and corners.")
        result = attempt.ask(question)
        self.assertEqual(result, "four sides and corners.")

    @requirements(['#0021'])
    def test_correcting_no_question(self):
        """ test trying to correct an answer without asking a question """
        attempt = Interface()
        result = attempt.correct("four sides.")
        self.assertEqual(result, "Please ask a question first")
