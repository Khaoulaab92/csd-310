#Khaoula Azdoud
#07/06/2023
#Module 8 Assignment: Movies: Update & Deletes

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

    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                     config["database"]))

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.

    # Inner join query
    cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

    # Get the results from the cursor object
    films = cursor.fetchall()

    print("\n-- {} --".format(title))

    # Iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


show_films(cursor, "DISPLAYING FILMS")

# Insert a new record into the film table
cursor.execute(
    "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES('A Beautiful Mind', '2002', '135', 'Ron Howard', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),(SELECT genre_id FROM genre WHERE genre_name = 'Drama'))")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

#Update  the film Alien to being a Horror film
cursor.execute("UPDATE film SET  genre_id = 1 WHERE film_name = 'Alien'")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

#Delete the movie Gladiator
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

cursor.close()
db.close()

