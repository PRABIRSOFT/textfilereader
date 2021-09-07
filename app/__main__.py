#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-09-08
# @Author  : Prabir Ghosh
# @Version : 1.0.0
#
# Flask Application To Read A File
from app.api import app 

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)