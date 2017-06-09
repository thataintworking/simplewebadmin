#!/usr/bin/env python3

# coding=utf-8
# Author: rsmith
# Copyright ©2016 iProspect, All Rights Reserved

import base64
import hashlib
import logging
import os
import random
import string
from datetime import datetime, timedelta
from decimal import Decimal
from config import log_dir
import click
from flask import Flask, request, session, abort, render_template, send_from_directory, redirect, url_for, make_response

logger = logging.getLogger('creativewebadmin.py')  # have to be explicit because __name__ = '__main__'

logger.info('Using log dir = %s', log_dir)
app_path = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(app_path, 'templates')
static_folder = os.path.join(app_path, 'static')


TEN_YEARS = 3650


def prefix_route(route_function, prefix='', mask='{0}{1}'):
    def newroute(route, *args, **kwargs):
        return route_function(mask.format(prefix, route), *args, **kwargs)
    return newroute


app = Flask('creativewebadmin', template_folder=template_folder, static_folder=static_folder)
app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


MESSAGE = 'message'
USER = 'user'


def request_params():
    if request.method == 'POST':
        return request.form
    else:
        return request.args


@app.route('/', methods=['GET', 'POST'])
def index():
    session.permanent = True
    message = session.pop(MESSAGE, None)
    return render_template('index.html', message=message)


@app.route('/favicon.ico')
def favicon():
    imgdir = os.path.join(app.root_path, 'static', 'images')
    return send_from_directory(imgdir, 'creativewebadmin.ico', mimetype='image/vnd.microsoft.icon')


@click.command()
@click.argument('port', default=5009)
def main(port):
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
