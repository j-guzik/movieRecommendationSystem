import pyodbc

class Database:

    def __init__(self):
        self.connection = pyodbc.connect('Driver={SQL Server};'
                                         'Server=LAPTOP-4P427RGF\SQLEXPRESS;'
                                         'Database=recommenderdata;'
                                         'Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def selectAll(self):
        data = []
        users = []
        items = []
        ratings = []

        self.cursor.execute("SELECT rating, user_id, movie_id from rating;")
        rows = self.cursor.fetchall()

        for r in rows:
            ratings.append(r[0])
            users.append(r[1])
            items.append(r[2])

        data.append(users)
        data.append(items)
        data.append(ratings)

        return data

    def getName(self, id):
        self.cursor.execute("SELECT title FROM movies WHERE id = " + str(id) + ";")
        rows = self.cursor.fetchall()
        return list(rows[0])

    def insertUser(self, uid):
        self.cursor.execute("INSERT INTO users (id_firebase) VALUES ('" + str(uid) + "');")
        self.connection.commit()
        return "User created successfully."

    def getUser(self, id):
        self.cursor.execute("SELECT id_user FROM users WHERE id_firebase = '" + str(id) + "';")
        rows = self.cursor.fetchall()
        return list(rows[0])

    def getMovies(self):
        data = []
        self.cursor.execute("select * from movies order by rating desc;")
        rows = self.cursor.fetchall()
        for row in rows:
            data.append(list(row))
        return data

    def getPopularMovies(self):
        data = []
        self.cursor.execute("SELECT TOP 8 * from movies order by popularity desc;")
        rows = self.cursor.fetchall()
        for row in rows:
            data.append(list(row))
        return data

    def rateItem(self, movieId, ratingValue, uid):
        self.cursor.execute("INSERT INTO rating (rating, user_id, movie_id) VALUES (" + str(ratingValue) + ",(select id_user from users where id_firebase='" + uid + "')," + str(movieId) + ");")
        self.connection.commit()
        return "Movie rated."

    def currentRate(self, movieId, uid):
        self.cursor.execute("select top 1 rating from rating where movie_id =" + str(movieId) + "and user_id = (select id_user from users where id_firebase='" + uid + "') order by rating desc");
        rows = self.cursor.fetchall()
        return list(rows[0])

    def getRow(self, movieId):
        self.cursor.execute("SELECT row FROM movies WHERE id = " + str(movieId) + ";")
        rows = self.cursor.fetchall()
        rows = list(rows[0])
        return rows[0]

    def getId(self, row):
        self.cursor.execute("SELECT id FROM movies WHERE row = " + str(row) + ";")
        rows = self.cursor.fetchall()
        rows = list(rows[0])
        return rows[0]

    def getTop3(self, uid):
        data = []
        self.cursor.execute("select top 3 movie_id from rating where (rating > 5) and user_id=" + str(uid) + " order by id_rating desc;")
        rows = self.cursor.fetchall()
        for row in rows:
            row = list(row)
            data.append(row[0])
        return data

    def getRecommendDetails(self, movieid):
        data = []
        self.cursor.execute("SELECT TOP 6 * from movies where id=" + str(movieid) + ";")
        rows = self.cursor.fetchall()
        for row in rows:
            data.append(list(row))
        return data