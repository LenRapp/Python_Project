import datetime

def reponse(message):
    message = message.lower().strip()

    if "bonjour" in message or "salut" in message:
        return "Salut"
    elif "comment ça va" in message or "ça va" in message:
        return "Super et toi"
    elif "super" in message or "ça va" in message:
        return "Génial"
    elif "pas trop" in message or "non" in message:
        return "Mince j'éspère que tu iras meiux"
    elif "nom" in message or "prenom" in message:
        return "Je suis le petit Chatbot de python"
    elif "heure" in message:
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif "date" in message:
        return datetime.datetime.now().strftime("%d/%m/%Y")
    elif "bye" in message or "quitter" in message:
        return "Au revoir"
    else:
        return "Désolé je ne comprend pas"

def chatbot():
    print("Je suis ton chatbot console ! Tape (bye/quitter) pour quitter")
    while True:
        user_input = input("Toi :")
        repondre = reponse(user_input)
        print("ChatBot: ",repondre)

        if user_input.lower().strip() in["quitter","bye"]:
            break

chatbot()
