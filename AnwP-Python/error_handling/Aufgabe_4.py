# Aufgabe 4
# Du findest eine Liste mit 5 Zahlen. Der Benutzer soll einen Index eingeben
# und das Programm gibt das Element an dieser Position aus. Verwende Error Handling um einen
# IndexError und einen ValueError abzufangen wenn der Benutzer keinen gültigen Index eingibt
# (Am liebsten durch eine seperate exception)
 
numbers = [10, 20, 30, 40, 50]

def input_int(question: str) -> int:
    try:
        return int(input(f"{question}: "))
    except ValueError:
        print("ValueError: Sie haben keine ganze Zahl eingegeben. Programm wird beendet..")
        exit(-1)
        
try:
    index = input_int("Bitte geben Sie einen Index ein")
    print(f"Das Element an der Position {index} ist: {numbers[index]}")
except IndexError:
    print("IndexError: Der Index ist nicht in der Liste enthalten. Programm wird beendet..")
    exit(-1)