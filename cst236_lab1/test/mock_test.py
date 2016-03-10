""" Test cases for mock functions """
import os
from unittest import TestCase
from mock import mock
from source.git_utils import is_file_in_repo,\
    get_git_file_info, has_untracked_files, get_repo_root

from source.main import Interface
from test.plugins.ReqTracer import requirements

class TestMockRequirements(TestCase):
    """ Mock test case requirements """

    @requirements(["#0100"])
    @mock.patch('subprocess.Popen')
    def test_mock_in_repo(self, mock_subproc_popen):
        """ test to see if the file is in the repo """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('true', 'file not found')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("Is the <nose2.cfg> in the repo?")
        self.assertEqual(result, "Yes")


    @requirements(["#0100"])
    @mock.patch('subprocess.Popen')
    def test_mock_not_in_repo(self, mock_subproc_popen):
        """ test to see if the file is in the repo """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("Is the <filename> in the repo?")
        self.assertEqual(result, "No")


    @requirements(["#0100"])
    @mock.patch('source.git_utils.get_diff_files')
    def test_mock_not2(self, mock_get_diff_files):
        """ test to see if the file is in the repo """
        filename = "nose2.cfg"
        mock_get_diff_files.return_value = os.path.abspath(filename)
        result = is_file_in_repo(filename)
        self.assertEqual(result, "No")


    @requirements(["#0101"])
    @mock.patch('source.git_utils.get_diff_files')
    def test_mock_diff(self, mock_get_diff_files):
        """ test to see if the file is modified locally """
        filename = "nose2.cfg"
        mock_get_diff_files.return_value = os.path.abspath(filename)
        result = get_git_file_info(filename)
        self.assertEqual(result, "nose2.cfg has been modified locally")


    @requirements(["#0101"])
    @mock.patch('source.git_utils.get_untracked_files')
    @mock.patch('source.git_utils.get_diff_files')
    def test_mock_untracked(self, mock_get_diff_files, mock_get_untracked_files):
        """ test to see if the file has been checked in """
        filename = "nose2.cfg"
        mock_get_diff_files.return_value = ('')
        mock_get_untracked_files.return_value = os.path.abspath(filename)
        result = get_git_file_info(filename)
        self.assertEqual(result, "nose2.cfg has not been checked in")


    @requirements(["#0101"])
    @mock.patch('source.git_utils.get_untracked_files')
    def test_mock_has_untracked(self, mock_get_untracked_files):
        """ test to see if the file is untracked """
        filename = "nose2.cfg"
        mock_get_untracked_files.return_value = "I hate mock!"
        result = has_untracked_files(filename)
        self.assertEqual(result, True)


    @requirements(["#0101"])
    @mock.patch('source.git_utils.git_execute')
    def test_mock_repo_root(self, mock_git_execute):
        """ test to get the file's root """
        filename = os.path.abspath("nose2.cfg")
        mock_git_execute.return_value = filename
        result = get_repo_root(filename)
        self.assertEqual(result, filename)


    @requirements(["#0101"])
    @mock.patch('subprocess.Popen')
    def test_mock_non_exist(self, mock_subproc_popen):
        """ test to see if an exception is raised """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        with self.assertRaises(Exception, msg="Path filename does not exist cannot get git file"):
            attempt.ask("What is the status of <filename>?")


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_mock_status_update(self, mock_subproc_popen):
        """ test to see if the file is up to date """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("What is the status of <nose2.cfg>?")
        self.assertEqual(result, "nose2.cfg is up to date")


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_mock_status_dirty(self, mock_subproc_popen):
        """ test to see if the file is a dirty repo """
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': [('', ''), ('', ''),
                                             ('', ''), ('true', ''), ('', ''), ('', '')]}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("What is the status of <nose2.cfg>?")
        self.assertEqual(result, "nose2.cfg is a dirty repo")


    @requirements(['#0102'])
    @mock.patch('subprocess.Popen')
    def test_mock_file_info(self, mock_subproc_popen):
        """ test to see the file's info """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('4655434B5448495321, 2/27/2016, David Barnes', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("What is the deal with <nose2.cfg>?")
        self.assertEqual(result, "4655434B5448495321, 2/27/2016, David Barnes")


    @requirements(['#0103'])
    @mock.patch('subprocess.Popen')
    def test_mock_branch(self, mock_subproc_popen):
        """ test to get the repo branch """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('DavidB', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("What branch is <nose2.cfg>?")
        self.assertEqual(result, "DavidB")


    @requirements(['#0104'])
    @mock.patch('subprocess.Popen')
    def test_mock_root(self, mock_subproc_popen):
        """ test to get the file's root """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('https://github.com/OregonTech/DavidB', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        attempt = Interface()
        result = attempt.ask("Where did <nose2.cfg> come from?")
        self.assertEqual(result, "https://github.com/OregonTech/DavidB")
