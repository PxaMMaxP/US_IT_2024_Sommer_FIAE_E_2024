# AUfgabe 12
# Erstelle ein Dictionary mit Informationen über einen Film (z.B.: Titel, Jahr, Genre). Schreibe ein Programm dass das Dictionary
# mithilfe von update um die Bewertung des Films erweitert.

movies = {
    "title": "The Godfather",
    "year": 1972,
    "genre": "Crime",
}

movies.update({"rating": 9.2})

print(movies)