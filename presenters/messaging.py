#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

# rss parsing
import feedparser
# regex
import re

# models
from models.constants import *

messaging = Blueprint('messaging', __name__)

@messaging.route('/status/')
def status():
	result = {}
	if MESSAGING_RSS_URL and MESSAGING_RSS_TAG:
		rss = feedparser.parse(MESSAGING_RSS_URL)
		if rss:
			title = rss.entries[0].title
			if title and MESSAGING_RSS_TAG in title:
				# show the title most def
				result['message'] = "<strong>%s</strong>" % title.replace(MESSAGING_RSS_TAG, '').strip()
				# ...and as much as possible text from the body...
				body = rss.entries[0].description
				if body:
					result['message'] += ":"
					for word in body.split():
						if len(__less_tags(result['message']) + word) < 150:
							result['message'] += " %s" % word
						else:
							result['message'] += "&hellip;"
							break
				# the whole shebang is a link
				result['message'] = "<a target='new' href='%s'>%s</a>" % (rss.entries[0].link, result['message'])
	return jsonify(result)

def __less_tags(text):
	'''Django style function for filtering out tags from a string'''
	return re.sub(r'<[^>]*?>', '', text)