#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-09-08
# @Author  : Prabir Ghosh
# @Version : 1.0.0
#
# Flask Application To Read A File
from app.api import app

def test_dependencies():
    import os
    import math
    from flask import Flask, request, jsonify
    from chardet import detect
    assert True

def test_get_file():
    with app.test_client() as test_client:
        response = test_client.get("/get_file/file2.txt?start=1&end=6")
        assert response.status_code == 200