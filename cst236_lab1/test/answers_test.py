''' Tests for determining answers'''
from unittest import TestCase
import getpass
from datetime import datetime

from source.answers import can_convert, i_know, days_to_christmas
from source.main import Interface
from test.plugins.ReqTracer import story, requirements


class TestJobStories(TestCase):
    ''' Job story test cases'''

    @story("When I ask \"What time is it?\" I want to be"
           " given the current date/time so I can stay up to date")
    def test_job_story_time(self):
        ''' test for the time job story '''
        attempt = Interface()
        result = attempt.ask("What time is it?")
        self.assertEqual(result, datetime.now().strftime("%m-%d-%Y %H:%M:%S"))

    @story("When I ask \"What is the n digit of fibonacci\""
           " I want to receive the answer so I don't have to figure it out myself")
    def test_job_story_fibonacci(self):
        ''' Test for determining the nth digit of the fibonacci sequence '''
        attempt = Interface()
        result = attempt.ask("What is the 5 digit of fibonacci?")
        self.assertEqual(result, '3')

    @story("When I ask \"What is the n digit of pi\" I want to"
           " receive the answer so I don't have to figure it out myself")
    def test_job_story_pi(self):
        ''' test for determining the nth digit of pi '''
        attempt = Interface()
        result = attempt.ask("What is the 5 digit of pi?")
        self.assertEqual(result, "5")

    @story("When I ask \"What is the n digit of pi\" I want to"
           " receive the answer so I don't have to figure it out myself")
    def test_job_story_pi2(self):
        ''' test to see that the function returns the first digit of pi'''
        attempt = Interface()
        result = attempt.ask("What is the 1 digit of pi?")
        self.assertEqual(result, "3")

    @story("When I ask \"Please clear memory\" I want the application"
           " to clear user set questions and answers so I can reset the application")
    def test_job_story_clear(self):
        ''' test to see if the user set question answers are cleared '''
        attempt = Interface()
        attempt.ask("What is the meaning of life?")
        attempt.teach("42")
        attempt.ask("Please clear memory?")
        result4 = attempt.ask("What is the meaning of life?")
        self.assertEqual(result4, "I don't know, please provide the answer")

    @story("When I say \"Open the door hal\", I want the application"
           " to say \"I'm afraid I can't do that <user name> so I know that is not an option")
    def test_job_story_open(self):
        ''' test to see that the program refuses a request '''
        attempt = Interface()
        result = attempt.ask("Open the door Hal?")
        self.assertEqual(result, "I'm afraid I can't do that "+getpass.getuser())

    @story("When I ask \"Convert <number> <units> to <units>\" I want"
           " to receive the converted value and units so I can know the answer.")
    def test_job_story_convert(self):
        ''' test to see if the program can convert between units '''
        attempt = Interface()
        result = attempt.ask("Convert 10 meters to yards")
        self.assertEqual(result, '10.9361 yards')

    @story("When I ask for a numberic conversion I want at least 10 "
           "different units I can convert from/to")
    def test_job_story_conversions(self):
        ''' test to see if the program lists all available conversions'''
        attempt = Interface()
        result = attempt.ask("What units can I convert?")
        answer = can_convert()
        self.assertEqual(result, answer)

    @story("When I ask \"When does Half-Life 3 come out\" I want the"
           " application to laugh at the assumption that there will be a Half-Life 3.")
    def test_job_story_lol(self):
        ''' test to see if the program laughs at the absurdity that the game will come out '''
        attempt = Interface()
        result = attempt.ask("When does Half-Life 3 come out?")
        self.assertEqual(result, "ha ha ha, as if that will ever happen.")

    @story("When I ask \"Why is it called the Legend of Zelda when you"
           " play as Link\" I want the application to explain why.")
    def test_job_story_legend(self):
        ''' test to tell the legend of zelda '''
        attempt = Interface()
        result = attempt.ask("Why is it called the Legend of Zelda when you play as Link?")
        self.assertEqual(result, "Becuase every princess is named Zelda "
                                 "after the in-game legend about the first"
                                 " princess, who was named Zelda.")

    @story("When I ask \"What is the meaning of life, the universe"
           ", and everything\" I want the application to respond 42.")
    def test_job_story_life(self):
        ''' test to see if the program knows the answer to the ultimate question '''
        attempt = Interface()
        result = attempt.ask("What is the meaning of life, the univers, and everything?")
        self.assertEqual(result, "42")

    @story("When I ask \"What do you know\" I want the application"
           " to tell me every question it has an answer for.")
    def test_job_story_knowns(self):
        ''' test to see if the program can output all known questions '''
        attempt = Interface()
        result = attempt.ask("What do you know?")
        answer = i_know()
        self.assertEqual(result, answer)

    @story("When I ask \"How do I make a PBJ 2.0\" I want the"
           " application to tell me how to make one.")
    def test_job_story_pbj(self):
        ''' test to know if the program knows how to make a PBJ 2.0 '''
        attempt = Interface()
        result = attempt.ask("How do I make a PBJ 2.0?")
        self.assertEqual(result, "On the bottom bun in vertical rows"
                                 " place creamy peanut-butter, nutella, and crunchy peanut-butter."
                                 " Then on the top bun in horizontal rows place jelly/jam,"
                                 " honey, and marshmellow spread.")


class TestRequirements(TestCase):
    ''' Test cases for answer requirements '''

    @requirements(['#0002', '#0022'])
    def test_requirement_triangle_area(self):
        ''' test to see if the program can calculate the area of a triangle '''
        attempt = Interface()
        result = attempt.ask("What is the area of a triangle with sides 6 5 5?")
        self.assertEqual(result, "12.0")

    @requirements(['#0004', '#0005', '#0023'])
    def test_requirement_quad_area(self):
        ''' test to see if the program can calculate the area of a quadrilateral '''
        attempt = Interface()
        result = attempt.ask("What is the area of a quadrilateral "
                             "with sides and corners 2 4 2 4 90 90 90 90?")
        self.assertEqual(result, '8.0')

    @requirements(['#0004', '#0005', '#0023'])
    def test_requirement_quad_area2(self):
        ''' test to see if the program can calculate the area of a rhombus '''
        attempt = Interface()
        result = attempt.ask("What is the area of a quadrilateral with"
                             " sides and corners 4 4 4 4 60 120 60 120?")
        self.assertEqual(result, '13.856')

    @requirements(['#0004', '#0005', '#0023'])
    def test_requirement_quad_area3(self):
        ''' code coverage test for a disconnected quadrilateral'''
        attempt = Interface()
        result = attempt.ask("What is the area of a quadrilateral"
                             " with sides and corners 4 5 4 4 90 90 90 90?")
        self.assertEqual(result, 'Can not determine area because'
                                 ' the quadrilateral is disconnected')

    @requirements(['#0024'])
    def test_requirement_tip(self):
        ''' test to see if the program can calculate a given % tip '''
        attempt = Interface()
        result = attempt.ask("How much is a 15 percent tip on a bill of 17.65?")
        self.assertEqual(result, "2.65")

    @requirements(['#0025'])
    def test_requirement_sales_tax(self):
        ''' test to see if the program can calculate total bill after tax '''
        attempt = Interface()
        result = attempt.ask("What is the total bill on 39.95 if the sales tax is 6.5 percent?")
        self.assertEqual(result, "42.55")

    @requirements(['#0026'])
    def test_requirement_christmas(self):
        ''' test to see how many days until christmas '''
        attempt = Interface()
        result = attempt.ask("How many days until Christmas?")
        days = days_to_christmas()
        self.assertEqual(result, days)
