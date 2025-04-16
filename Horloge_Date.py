from datetime import datetime
import time

heure_actuel = datetime.now()
date_actuel = time

print("Heure actuel :", heure_actuel.strftime("%H:%M:%S"))
print("Date actuel :", date_actuel.strftime("%d/%m/%Y"))
