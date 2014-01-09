#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright 2012-2014 Cisco Systems, Inc
# See LICENSE for details.

""" API """

from flask import Flask
from server import Echo

app = Flask(__name__)


@app.route('/')
def hello():

    return ''



