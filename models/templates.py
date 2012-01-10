#!/usr/bin/python
# -*- coding: utf -*-

import os
import codecs

class Templates:

    def __init__(self, name):
        self.dir = os.getcwd() + '/static/html/'
        self.path = self.dir + '%s.html' % name

    def exists(self):
        """
        check that a file exists
        """
        return os.path.isfile(self.path)

    def write(self, template):
        """
        write html into a template file
        """
        if not os.path.isdir(self.dir):
            os.makedirs(self.dir)

        if os.access(self.path, os.W_OK):
            with codecs.open(self.path, 'w', 'utf-8') as f:
                f.write(template)
        else:
            raise Exception('The file %s is not writable!' % self.path)

    def read(self):
        """
        read html from a template file
        """
        with codecs.open(self.path, 'r', 'utf-8') as f:
            html = f.read()
        return html
