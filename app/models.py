from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Movie(db.Model):
	Id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(64), index=True, unique = True)
	Description = db.Column(db.String(150))
	Poster = db.Column(db.String(64))
	
	def __init__(self, name, desc, poster):
                self.Name = name
                self.Description = desc
                self.Poster = poster

	def __repr__(self):
		return '<Movie %r>' & (self.Name)

	def serialize(self):
                return {
                        'id' : self.Id,
                        'name' : self.Name,
                        'description' : self.Description,
                        'poster' : self.Poster
                }

class Review(db.Model):
	Id = db.Column(db.Integer, primary_key=True)
	Title = db.Column(db.String(64), index=True)
	Description = db.Column(db.String(200))
	Rating = db.Column(db.Integer)
	User = db.Column(db.String(64))
	DeviceId = db.Column(db.String(200))

	def __init__(self, title, desc, user, deviceid, movieid=0, rating=0):
                self.Title = title
                self.Description = desc
                self.Rating = rating
                self.User = user
                self.DeviceId = deviceid
                self.MovieId = movieid

	def __repr__(self):
		return '<Review %r>' & (Review.Title)

	def serialize(self):
                return {
                        'id' : self.Id,
                        'title' : self.Title,
                        'description' : self.Description,
                        'rating' : self.Rating,
                        'user' : self.User,
                        'deviceid' : self.DeviceId
                }