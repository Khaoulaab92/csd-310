import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\ndatabase user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n  Press any key to continue...\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.Er_ACCES_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

# First Query Select all fields from the studio table
cursor = db.cursor()
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS --\n")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# Second Query Select all fields from the genre table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("-- DISPLAYING Genre RECORDS --\n")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# Third query Select the movie names for those movies that have a run time of less than two hours
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
films = cursor.fetchall()
print("-- DISPLAYING Short Film RECORDS --\n")
for film in films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

# Fourth query Get a list of film names, and directors ordered by director
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
films = cursor.fetchall()
print("-- DISPLAYING Director RECORDS in Order --\n")
for film in films:
    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))
db.close()
cursor.close()
