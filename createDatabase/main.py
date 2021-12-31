import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv (r'J:\Informatyka\3.5\inzynierka\csv_07.12.21\15.12\26.12\movies_sql.csv', sep="|", lineterminator='\n')
df = pd.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-4P427RGF\SQLEXPRESS;'
                      'Database=recommenderdata;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE movies (
			id int primary key not null,
			overview nvarchar(2000),
			poster_path nvarchar(200) NULL,
            title nvarchar(100) NULL,
            popularity float NULL,
            release_date date NULL,
            backdrop_path nvarchar(200) NULL,
            rating float NULL,
            row int NULL
			)
               ''')

cursor.execute('''
        CREATE TABLE  users (
            id_user int NOT NULL IDENTITY(1, 1),
            id_firebase VARCHAR(45) NOT NULL,
            PRIMARY KEY (id_user)
        );
               ''')

cursor.execute('''
        CREATE TABLE rating (
            id_rating int NOT NULL IDENTITY(1, 1),
            rating int NOT NULL,
            PRIMARY KEY (id_rating),
            user_id int NOT NULL FOREIGN KEY REFERENCES users(id_user),
            movie_id int NOT NULL FOREIGN KEY REFERENCES movies(id),
        );
               ''')


# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO movies (id, overview, poster_path, title, popularity, release_date, backdrop_path, rating, row)
                VALUES (?,?,?, ? ,?, ?, ? ,?, ?)
                ''',
                row.id,
                row.overview,
                row.poster_path,
                row.title,
                row.popularity,
                row.release_date,
                row.backdrop_path,
                row.rating,
                row.row
                )
conn.commit()
