#!/usr/bin/env python3

nom_fichier = "notes.txt"

def afficher_menu():
    print("1. Afficher les notes")
    print("2. Ajouter une note")
    print("3. Modifier une note")
    print("4. Supprimer une note")
    print("5. Quitter")
    return input("Choisissez une option: ")

def afficher_notes():
    with open(nom_fichier, "r") as f:
        print(f.read())

def ajouter_note():
    with open(nom_fichier, "a") as f:
        note = input("Entrez votre note: ")
        f.write(note + "\n")

def modifier_note():
    with open(nom_fichier, "r") as f:
        notes = f.readlines()

    print("Quelle note voulez-vous modifier? (index 0-basé)")
    for i, note in enumerate(notes):
        print(f"{i}: {note}")

    index = int(input("Entrez l'index de la note: "))
    notes[index] = input("Entrez votre nouvelle note: ") + "\n"

    with open(nom_fichier, "w") as f:
        f.writelines(notes)

def supprimer_note():
    with open(nom_fichier, "r") as f:
        notes = f.readlines()

    print("Quelle note voulez-vous supprimer? (index 0-basé)")
    for i, note in enumerate(notes):
        print(f"{i}: {note}")

    index = int(input("Entrez l'index de la note: "))
    del notes[index]

    with open(nom_fichier, "w") as f:
        f.writelines(notes)

if __name__ == "__main__":
    while True:
        choix = afficher_menu()

        if choix == "1":
            afficher_notes()
        elif choix == "2":
            ajouter_note()
        elif choix == "3":
            modifier_note()
        elif choix == "4":
            supprimer_note()
        elif choix == "5":
            break
        else:
            print("Choix non valide.")
