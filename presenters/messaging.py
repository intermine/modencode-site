#!/usr/bin/python
# -*- coding: utf -*-

# framework
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

# rss parsing
import feedparser

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
				result['message'] = title.replace(MESSAGING_RSS_TAG, '').strip()
	return jsonify(result)