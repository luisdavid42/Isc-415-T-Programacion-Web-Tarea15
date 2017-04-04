from flask import Blueprint
from flask import request
from flask import render_template
import urllib.request
import os
from app.models import Movie, db, Review

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def hello_world():
    return render_template('review.html')