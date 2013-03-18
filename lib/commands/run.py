#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Moodle Development Kit

Copyright (c) 2013 Frédéric Massart - FMCorz.net

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

http://github.com/FMCorz/mdk
"""

import logging
from lib.command import Command


class RunCommand(Command):

    _arguments = [
        (
            ['-a', '--all'],
            {
                'action': 'store_true',
                'dest': 'all',
                'help': 'runs the script on each instance'
            }
        ),
        (
            ['-i', '--integration'],
            {
                'action': 'store_true',
                'dest': 'integration',
                'help': 'runs the script on integration instances'
            }
        ),
        (
            ['-s', '--stable'],
            {
                'action': 'store_true',
                'dest': 'stable',
                'help': 'runs the script on stable instances'
            }
        ),
        (
            ['script'],
            {
                'help': 'the name of the script to run'
            }
        ),
        (
            ['names'], {
                'default': None,
                'help': 'name of the instances',
                'nargs': '*'
            }
        )
    ]
    _description = 'Run a script on a Moodle instance'

    def run(self, args):

        # Resolving instances
        names = args.names
        if args.all:
            names = self.Wp.list()
        elif args.integration or args.stable:
            names = self.Wp.list(integration=args.integration, stable=args.stable)

        # Doing stuff
        Mlist = self.Wp.resolveMultiple(names)
        if len(Mlist) < 1:
            raise Exception('No instances to work on. Exiting...')

        for M in Mlist:
            logging.info('Running \'%s\' on \'%s\'' % (args.script, M.get('identifier')))
            try:
                M.runScript(args.script, stderr=None, stdout=None)
            except Exception as e:
                logging.warning('Error while running the script on %s' % M.get('identifier'))
                logging.debug(e)
            else:
                logging.info('')

        logging.info('Done.')