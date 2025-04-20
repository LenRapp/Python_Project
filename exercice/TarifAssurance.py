# Un club d'assurance propose à ses clients trois tarifs différents identifiables par niveau: niveau haut, niveau moyen et  niveau bas.
#
#  Le tarif dépend de la situation du conducteur:
#
# - un conducteur de moins de 25 ans et titulaire du permis depuis deux ans ou moins, se voit attribuer le tarif haut.
#
# - un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans, ou de 25 ans ou plus  mais
#
# titulaire du permis depuis deux ans ou moins a le droit au tarif moyen;
#
# - un conducteur de 25 ans ou de plus de 25 ans titulaire du permis depuis plus de deux ans bénéfice du tarif bas.
#
# Ecrire un algorithme qui demande à l'utilisateur de saisir son âge ainsi que l'année d'obtention de son permis et qui affiche le tarif qui lui est attribué.


age=(int(input("Votre âge : ")))
permis=int(input("Année d'obtention du permis : "))

if age < 25 and permis <= 2:
    print("tarif haut")
elif age < 25 and permis > 2 or age >= 25 and permis <= 2:
    print("tarif moyen")
elif age >= 25 and permis > 2:
    print("tarif bas")


