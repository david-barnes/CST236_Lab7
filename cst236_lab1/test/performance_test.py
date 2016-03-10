""" test file for performance test cases """

from unittest import TestCase
from mock import mock
from source.answers import days_to_christmas
from source.main import Interface
from test.plugins.ReqTracer import requirements

class TestPerformance(TestCase):
    """ test cases for performance requirements """

    @requirements(['#0050', '#0051', '#0052'])
    def test_log_write(self):
        """ test for writing to a log file """
        attempt = Interface()
        result = attempt.ask("What type of quadrilateral is 3 3 3 3 60 120 60 120?")
        self.assertEqual(result, "rhombus")


    @requirements(['#0053'])
    def test_performance_fibonacci(self):
        """ performance test for fibonacci sequence """
        attempt = Interface()
        result = attempt.ask("What is the 1000 digit of fibonacci?")
        self.assertEqual(result, '9')


    @requirements(['#0054'])
    def test_performance_quad_area2(self):
        """ performance test for finding the area of a quadrilateral """
        attempt = Interface()
        result = attempt.ask("What is the area of a quadrilateral"
                             " with sides and corners 20 20 20 20 60 120 60 120?")
        self.assertEqual(result, '346.41')


    @requirements(['#0055'])
    def test_performance_christmas(self):
        """ performance test for finding the days until christmas """
        attempt = Interface()
        result = attempt.ask("How many days until Christmas?")
        days = days_to_christmas()
        self.assertEqual(result, days)


    @requirements(['#0056'])
    @mock.patch('subprocess.Popen')
    def test_performance_file_info(self, mock_subproc_popen):
        """ performance test for mock function """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('4655434B5448495321, 2/27/2016, David Barnes', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("What is the deal with <nose2.cfg>?")
        self.assertEqual(result, "4655434B5448495321, 2/27/2016, David Barnes")


    @requirements(['#0057'])
    def test_performance_convert(self):
        """ performance test for converting lengths """
        attempt = Interface()
        result = attempt.ask("Convert 10 meters to yards")
        self.assertEqual(result, '10.9361 yards')
