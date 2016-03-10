"""
Use this plugin to activate coverage report.

To install this plugin, you need to activate ``coverage-plugin``
with extra requirements :

::

    $ pip install nose2[coverage-plugin]


Next, you can enable coverage reporting with :

::

    $ nose2 --with-coverage

Or with this lines in ``unittest.cfg`` :

::

    [coverage]
    always-on = True


"""
from nose2.events import Plugin

# pylint: disable=no-member
# config is aquired from outside file
# pylint: disable=bare-except
# while no exception is raised a message is output

class Coverage(Plugin):
    """ coverage plugin class """
    configSection = 'coverage'
    commandLineSwitch = ('C', 'with-coverage', 'Turn on coverage reporting')

    def __init__(self):
        """Get our config and add our command line arguments."""
        self.con_source = self.config.as_list('coverage', [])
        self.con_report = self.config.as_list('coverage-report', [])
        self.con_config = self.config.as_str('coverage-config', '').strip()
        self.cov_source = self.config.as_str('coverage-source', '').strip()
        self.cov_report = None
        self.cov_config = None
        self.cov_controller = None

        group = self.session.pluginargs
        group.add_argument(
            '--coverage', action='append', default=[], metavar='PATH',
            dest='coverage_source',
            help='Measure coverage for filesystem path (multi-allowed)'
        )
        group.add_argument(
            '--coverage-report', action='append', default=[], metavar='TYPE',
            choices=['term', 'term-missing', 'annotate', 'html', 'xml'],
            dest='coverage_report',
            help='Generate selected reports, available types:'
                 ' term, term-missing, annotate, html, xml (multi-allowed)'
        )
        group.add_argument(
            '--coverage-config', action='store', default='', metavar='FILE',
            dest='coverage_config',
            help='Config file for coverage, default: .coveragerc'
        )

    def handle_args(self, event):
        """Get our options in order command line, config file, hard coded."""

        self.cov_source = (event.args.coverage_source or
                           self.con_source or ['.'])
        self.cov_report = (event.args.coverage_report or
                           self.con_report or ['term'])
        self.cov_config = (event.args.coverage_config or
                           self.con_config or '.coveragerc')

        try:
            import cov_core
        except:
            print('Warning: you need to install [coverage-plugin] '
                  'extra requirements to use this plugin')
            return

        self.cov_controller = cov_core.Central(self.cov_source,
                                               self.cov_report,
                                               self.cov_config)
        self.cov_controller.start()


    def after_summary_report(self, event):
        """Only called if active so stop coverage and produce reports."""

        if self.cov_controller:
            self.cov_controller.finish()
            self.cov_controller.summary(event.stream)
