import os
from paste.script import command
from paste.deploy import appconfig
from zope.app.debug.debug import Debugger
import zope.app.wsgi


class Shell(command.Command):

    max_args = 1
    min_args = 1

    usage = "CONFIG_FILE"
    summary = "Python debug shell with BlueBream application loaded"
    group_name = "bluebream"

    parser = command.Command.standard_parser(verbose=True)

    def command(self):
        cwd = os.getcwd()
        config_file = self.args[0]
        config_name = 'config:%s' % config_file
        conf = appconfig(config_name, relative_to=cwd)
        zope_conf = conf['zope_conf']
        db = zope.app.wsgi.config(zope_conf)
        debugger = Debugger.fromDatabase(db)
        # Invoke an interactive interpreter shell
        banner = ("Welcome to the interactive debug prompt.\n"
                  "The 'root' variable contains the ZODB root folder.\n"
                  "The 'app' variable contains the Debugger, 'app.publish(path)' "
                  "simulates a request.")
        __import__('code').interact(banner=banner,
                                    local={'debugger': debugger,
                                           'app': debugger,
                                           'root': debugger.root()})
