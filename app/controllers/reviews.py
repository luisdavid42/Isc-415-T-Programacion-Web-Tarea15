from flask import Blueprint
from flask import request
from flask import render_template
from flask import jsonify
from flask import json
from sqlalchemy.sql import func
import urllib.request
import os
from app.models import Movie, db, Review

reviews = Blueprint('reviews', __name__)

@reviews.route('/', methods=['GET'])
def showreviews():
    return render_template('reviews.html')


@reviews.route('/wiri', methods=['GET'])
def showallreviews():
    reviewresults = []
    reviewtitles = []
    reviews = Review.query.all()
    
    for i in reviews:
        if i.Title not in reviewtitles:
            reviewtitles.append(i.Title)
            
    for i in reviews:
        title = i.Title
        if title in reviewtitles:
            i.Rating = Review.query.with_entities(func.avg(Review.Rating).label('average')).filter(Review.Title == title).scalar()
            reviewresults.append({'name' : i.Title, 'rating' : i.Rating })
            reviewtitles.remove(title)
            
    response = jsonify(reviewresults)
    return response

@reviews.route('/search', methods=['GET'])
def showreviewsbyname():
    moviename = request.args.get('name')
    movielist = []
    moviecount = Review.query.filter_by(Title = moviename).count()
    if moviecount>0:
        movieresults = Review.query.filter_by(Title = moviename).all()
        for i in movieresults:
            movielist.append(i.serialize())
        response = jsonify(movielist)
        return response
    else:
        return render_template('review.html'), 404
    

@reviews.route('/', methods=['POST'])
def handle_fomdata():
        moviename = request.form['name']
        movielength = Movie.query.filter_by(Name = moviename).count()
        if movielength>0 :
            nmovie = Movie.query.filter_by(Name = moviename).first()
            reviewscore = request.form['score']
            reviewdesc = request.form['review']
            reviewuser = request.form['user']
            deviceid = request.headers.get('User-Agent')
            nreview = Review(moviename, reviewdesc, reviewuser, deviceid, nmovie.Id, reviewscore)
            db.session.add(nreview)
            db.session.commit()       
        return render_template('review.html')