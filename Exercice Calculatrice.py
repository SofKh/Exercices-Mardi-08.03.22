# Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), son poids(en kg).
# Retournez ensuite la catégorie dans laquelle se trouve la personne.

import math

def calcul_imc():
    Taille=input("Veuillez entrer votre taille en metre: ")
    Poids=("Veuillez entrer votre poids en kg: ")
    return Poids / Taille**2

    if calcul_imc() < 18.5 :
        print("Votre categorie IMC est Poids Insuffisant")
    
    elif Calcul_Imc <= 24.9 :
        print("Votre categorie IMC est Poids Normal")
    
    elif Calcul_Imc <= 29.9 :
        print("Votre categorie IMC est Embonpoint")
    
    elif Calcul_Imc <= 34.9 :
        print("Votre categorie IMC est Embonpoint")

    elif Calcul_Imc <= 39.9 :
        print("Votre categorie IMC est Embonpoint")
    
    elif Calcul_Imc >= 40.0 :
        print("Votre categorie IMC est Embonpoint")


    






