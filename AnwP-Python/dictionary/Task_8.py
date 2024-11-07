# Aufgabe 8
# Du findest ein Dictionary mit den Namen von Schülern als Schlüssel und deren Noten als Werte.
# Schreibe ein Programm, das den Notendurchschnitt aller Noten berechnet (benutze values() und keys())
 
students = {
    "Alan": 1,
    "Jacques": 6,
    "Gerhard": 1,
    "Willi": 4,
    "Susanne":2
}

total_grades = sum(students.values())
number_of_students = len(students)
average_grade = total_grades / number_of_students

print(f"Der Notendurchschnitt ist: {average_grade:.2f}")