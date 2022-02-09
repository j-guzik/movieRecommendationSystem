import random
import databaseCon
from numpy import load

connection = databaseCon.Database()

def getRecommendedMovies(id):
  row = connection.getRow(id)
  cosine = load(r'J:\Informatyka\3.5\inzynierka2\csv_07.12.21\15.12\26.12\cosine.npy')
  sim_scores = list(enumerate(cosine[row]))
  sim_scores.pop(row)
  sim_scores =sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[0:5]
  movie_indices = [i[0] for i in sim_scores]
  movies = [connection.getId(i) for i in movie_indices]
  return movies

def getRecommendation(uidFirebase):
  uid = connection.getUser(uidFirebase)
  uid = uid[0]
  top3 = connection.getTop3(uid)
  print("top")
  print(top3)
  movies_set = []
  for i in top3:
    recomm_movies = getRecommendedMovies(i)
    for j in recomm_movies:
      if j not in movies_set:
        movies_set.append(j)
  print(movies_set)
  random_table = random.sample(movies_set, 4)
  ok = []
  for i in random_table:
    ok = [connection.getRecommendDetails(i) for i in random_table]
  return ok


print(getRecommendation("5Abu7GVu08XR9YJKDEi1sIYE3vt2"))
