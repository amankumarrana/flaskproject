# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:04:23 2018

@author: baman 

Flask application instance
"""

from flask import Flask
apps = Flask(__name__)

from app import routes