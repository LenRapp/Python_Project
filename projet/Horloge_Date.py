from datetime import datetime


def momentJournee(heure):
    if 5 >= heure <= 12:
        return "le matin"
    elif 13 >= heure <= 18:
        return "l'après midi"
    else:
        return "le soir"

datetime = datetime.now()
heure = datetime.hour

print("Heure actuel :", datetime.strftime("%H:%M:%S"))
print("Date actuel :", datetime.strftime("%d/%m/%Y"))
print("C'est",momentJournee(heure))
