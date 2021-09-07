#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-09-08
# @Author  : Prabir Ghosh
# @Version : 1.0.0
#
# Flask Application To Read A File
__version__ = "1.0.0"


# Importing Dependencies
import os
import math
from flask import Flask, request, jsonify
from chardet import detect
app = Flask(__name__)

# Exception Handler To Create Exceptions
class AppException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

# Register Exception Handler 
@app.errorhandler(AppException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Method get_file
# inputs:
#   file_name: string (default: 'file1.txt') -- path
#   start: int -- query string
#   end: int -- query string
#   
#   example: /get_file/file2.txt?start=1&end=6
# oputput:
#   content of that file  
@app.route('/get_file', defaults={"file_name": "file1.txt"}, methods=["GET"], strict_slashes=False)
@app.route('/get_file/<file_name>', methods=["GET"], strict_slashes=False)
def get_file(file_name):
    if os.path.exists(os.path.join("app", file_name)) == False:
        raise AppException(f"{file_name} file not found", status_code=404)

    encoding = detect(open(os.path.join("app", file_name), "rb").read())['encoding']
    lines = open(os.path.join("app", file_name), "r", encoding=encoding).readlines()
    
    start = 0
    end   = len(lines)
    if end == 0:
        raise AppException(f"{file_name} file is empty", status_code=406)

    if 'start' in request.args:
        if request.args['start'].isnumeric():
            start = int(request.args['start'])
        else:
            raise AppException(f"start point should be a number", status_code=406)
    if 'end' in request.args:
        if request.args['end'].isnumeric():
            end = int(request.args['end'])
        else:
            raise AppException(f"end point should be a number", status_code=406)

    if end < start:
        raise AppException(f"end point should be greater than start point", status_code=405)
    elif end == start:
        raise AppException(f"start point and end point cannot be same", status_code=405)

    return "<br/>".join(lines[start:end])
    