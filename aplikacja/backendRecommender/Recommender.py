import random

from surprise import SVD
import pandas as pd
from surprise import Dataset
from surprise import Reader
from collections import defaultdict
from surprise.model_selection import cross_validate
import databaseCon
from numpy import load

connection = databaseCon.Database()
# loadedData = con.selectAll()

# userGroupId = loadedData[0]
# ingredientId = loadedData[1]
# ratings = loadedData[2]
#
# def do_Predict():
#     ratings_dict = {'userID': userGroupId,
#                     'itemID': ingredientId,
#                     'rating': ratings}
#
#     df = pd.DataFrame(ratings_dict)
#     reader = Reader(rating_scale=(1, 4))
#     data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']], reader)
#     trainset = data.build_full_trainset()
#     algo = SVD()
#     algo.fit(trainset)
#     testset = trainset.build_anti_testset()
#     predictions = algo.test(testset)
#     cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
#     return get_top_n(predictions)
#
# def get_top_n(predictions, n = 20):
#     top_n = defaultdict(list)
#     for uid, iid, true_r, est, _ in predictions:
#         top_n[uid].append((iid, est))
#
#     for uid, user_ratings in top_n.items():
#         user_ratings.sort(key=lambda x: x[1], reverse=True)
#         top_n[uid] = user_ratings[:n]
#
#     return top_n
#
#
# def getRecommendedItems(uid):
#     itemInfo = []
#     recommendations = do_Predict()
#     for users in recommendations.items():
#         if users[0] == uid:
#             for items in users[1]:
#                 itemInfo.append(con.getName(items[0]))
#             return(itemInfo)
#
# print(getRecommendedItems(1))


def getRecommendedMovies(id):
  row = connection.getRow(id)
  cosine = load(r'J:\Informatyka\3.5\inzynierka\csv_07.12.21\15.12\26.12\cosine.npy')
  sim_scores = list(enumerate(cosine[row]))
  sim_scores.pop(row)
  sim_scores =sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[0:4]
  movie_indices = [i[0] for i in sim_scores]
  # print(movie_indices)
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
      movies_set.append(j)
  print(movies_set)
  random_table = random.sample(movies_set, 10)
  ok = []
  for i in random_table:
    ok = [connection.getRecommendDetails(i) for i in random_table]
  return ok


print(getRecommendation("5Abu7GVu08XR9YJKDEi1sIYE3vt2"))
# print("koks")
# print(getRecommendedMovies(121))