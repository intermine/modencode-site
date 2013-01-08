#!/usr/bin/python
# -*- coding: utf -*-

import config

# framework
from flask import Blueprint, render_template, request, redirect, url_for

# imports
from libs import utils
from functools import wraps

# models
from models.modmine import Modmine
from models.templates import Templates
from models.constants import *

allpubs = Blueprint('allpubs', __name__)

@allpubs.route('/allpubs/')
def rinaldo(update=False):
    """
    serve allpubs page
    """
    t = Templates('allpubs')
    
    if update or not t.exists():
        m = Modmine()
        #time = utils.current_time()
        from models.publications import publications as modencode_publications

        html = render_template('allpubs/allpubs.html', **dict(locals().items() + globals().items()))

        return html

        try:
            t.write(html)
        except Exception, inst:
            return str(inst)

    return t.read()
    
