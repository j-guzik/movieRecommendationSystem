from flask import Flask
import json
from Recommender import getRecommendation
import databaseCon
import Recommender

app = Flask(__name__)

#
# @app.route("/predictions/<int:uid>", strict_slashes=False)
# def predictions(uid):
#     return json.dumps(getRecommendedItems(uid), indent=2)

@app.route("/newUser/<string:uid>", strict_slashes=False)
def newUser(uid):
    connection = databaseCon.Database()
    return connection.insertUser(uid)

@app.route("/getUser/<string:uid>", strict_slashes=False)
def getUser(uid):
    connection = databaseCon.Database()
    return json.dumps(connection.getUser(uid), indent=2)

@app.route("/getMovies/", strict_slashes=False)
def getMovies():
    connection = databaseCon.Database()
    return json.dumps(connection.getMovies(), indent=2)

@app.route("/getPopularMovies/", strict_slashes=False)
def getPopularMovies():
    connection = databaseCon.Database()
    return json.dumps(connection.getPopularMovies(), indent=2)

@app.route("/rateItem/<int:movieId>/<int:ratedValue>/<string:uid>", strict_slashes=False)
def rateItem(movieId, ratedValue, uid):
    connection = databaseCon.Database()
    return connection.rateItem(movieId, ratedValue, uid)

@app.route("/currentRate/<int:movieId>/<string:uid>", strict_slashes=False)
def currentRate(movieId, uid):
    connection = databaseCon.Database()
    return json.dumps(connection.currentRate(movieId, uid), indent=2)

@app.route("/recommendations/<string:uid>", strict_slashes=False)
def recommendations(uid):
    return json.dumps(getRecommendation(uid), indent=2)

if __name__ == '__main__':
    app.run(debug=True)
