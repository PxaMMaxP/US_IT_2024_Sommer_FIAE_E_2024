# Aufgabe 15
# Erstelle ein Dictionary mit dem Namen von drei Klassenkameraden und deren Handynummern. Schreibe ein Programm,
# dass das Dicitonary mit clear() leert und überprüft, ob es nun leer ist.

mobile_numbers = {
    "Max": 123456,
    "Moritz": 654321,
    "Mia": 987654
}

print("Mobile Numbers: ", mobile_numbers)

mobile_numbers.clear()

if not mobile_numbers:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")
    
