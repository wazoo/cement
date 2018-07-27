
from cement import Controller
from cement.utils.version import get_version_banner

BANNER = get_version_banner()


class Base(Controller):
    class Meta:
        label = 'base'
        description = 'Cement Framework Developer Tools'
        epilog = 'Example: cement generate app /path/to/myapp'

        arguments = [
            (['-v', '--version'], {'action': 'version', 'version': BANNER}),
        ]

    def _default(self):
        self.app.args.print_help()
