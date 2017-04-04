from flask import Flask
from app.models import db


app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
db.create_all(app=app)


from app.controllers.main import main
from app.controllers.movies import movies
from app.controllers.reviews import reviews
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(movies, url_prefix='/movies')
app.register_blueprint(reviews, url_prefix='/reviews')