#programme connexion

#let'code (:
reset = 1
while reset == 1:
#on commence par créer la demande de connexion ou d'identification
    def connexion():
        print("================================================")
        print("(((((((((((((((((((((WELCOME))))))))))))))))))))")
        print("================================================")
        print("================================================")
        print("++++++++++++++++++++++MENU++++++++++++++++++++++")
        print("================================================")

        print("VEILLEZ A ENTRER LES CHIFFRES CORRESPONDANT A VOTRE REPONSE \n")
        print("1-S'Identifier")
        print("2-Se Connexion")

        #variable pour le choix et boucle pour les choix

        vide = ""

        choix = int(input("Saisi: "))

        while (choix <= 0) or (choix >= 3) or (choix == vide):
            print("VEILLEZ A ENTRER LES CHIFFRES CORRESPONDANT A VOTRE REPONSE \n")
            print("1-S'Identifier")
            print("2-Se Connexion")
            choix = int(input("Saisi:"))
        return choix

    print("================================================")
    print("(((((((((((((((((((((WELCOME))))))))))))))))))))")
    print("================================================")
    print("================================================")
    print("++++++++++++++++++++++MENU++++++++++++++++++++++")
    print("================================================")

    print("VEILLEZ A ENTRER LES CHIFFRES CORRESPONDANT A VOTRE REPONSE \n")
    print("1-S'Identifier")
    print("2-Se Connexion")
    choix = 0
    while choix == 0:
        #variable pour le choix et boucle pour les choix

        vide = ""

        choix = int(input("Saisi: "))
        

        while (choix <= 0) or (choix >= 3) or (choix == vide):
            print("VEILLEZ A ENTRER LES CHIFFRES CORRESPONDANT A VOTRE REPONSE \n")
            print("1-S'Identifier")
            print("2-Se Connexion")
            choix = int(input("Saisi:"))

        #dans le cas ou il S'identifie
        if choix == 1:
            print("+++++++++++++++++IDENTIFICATION+++++++++++++++++\n\n\n")

            nom_et_prenom = input("Entrez votre nom et prénoms:")
            pseudo = input("Entrer votre pseudo: ")
            password = input("Entrer votre mot de passe: ")
            confirm = input("Confirmer votre mot de passe: ")

            #boucle pour validation du formulaire

            while (nom_et_prenom == vide ) or (pseudo == vide) or (password == vide) or (confirm == vide) or (password != confirm ):
                print("VEILLER REMPLIR CORRECTEMENT LES CHAMPS DE TEXT MERCI!!!!!!\n\n\n")
                nom_et_prenom = input("Entrez votre nom et prénoms:")
                pseudo = input("Entrer votre pseudo: ")
                password = input("Entrer votre mot de passe: ")
                confirm = input("Confirmer votre mot de passe: ")

            print("vous êtes enregistrez avec succes!!!\n")
            #enregistrement dans un fichier

            info = f"{nom_et_prenom} {pseudo} {password} "
            conn = f"{pseudo} \n"
            log = f"{password} \n"

            with open("identify.txt", "a+") as file:
                file.write(info+"\n")
                file.close()
            with open("connexion.txt", "a+") as file1:
                file1.write(conn+"\n")
                file1.close()
            with open("password.txt", "a+") as pas:
                pas.write(log+"\n")
                pas.close()
        else:
            print("======================CONNEXION=======================\n\n\n")

            N_pseudo = input("Entrez votre pseudo: ")
            
            with open("connexion.txt", "r") as file:
                for x in file:
                    if N_pseudo == x :
                        N_password = input("Entrez votre mot de passe")
                        with open("password.txt", "a") as pas:
                            for a in pas:
                                if N_password == a:
                                    print("vous êtes vraiment : ",N_pseudo)
                                else:
                                    print("acces denied")
                            pas.close()
                    else:
                        print("ce pseudo n'existe pas!!!!")
                file.close()

            while (N_pseudo == vide):
                print("VEILLER REMPLIR CORRECTEMENT LES CHAMPS DE TEXT MERCI \n\n\n")
                with open("connexion.txt", "r") as file:
                    N_pseudo = input("Entrez votre pseudo: ")
                    for x in file:
                        if N_pseudo == x :
                            N_password = input("Entrez votre mot de passe")

                            with open("password.txt", "a") as pas:
                                for x in pas:
                                    if N_password == x:
                                        print("vous êtes vraiment : ",N_pseudo)
                                    else:
                                        print("acces denied")
                                pas.close()
                        else:
                            print("ce pseudo n'existe pas!!!!")
                    file.close()

            affiche = int(input("tapez 1 pour Afficher la liste de présence ou 2 sortir: "))

            if affiche == 1:
                with open("identify.txt", "r") as file3:
                    print(file3.read())
                    file3.close()
            else:
                print("vous êtes déconecté")
                
                while (affiche <= 0) or (affiche >= 3):
                    affiche = int(input("tapez 1 pour Afficher la liste de présence ou 2 sortir: "))
                    if affiche == 1:
                        with open("identify.txt", "r") as file3:
                            print(file3.read())
                            file3.close()
                    else:
                        print("vous êtes déconecté")
            choix = 1
    reset = int(input("voulez vous continuer?? \n tapez 1 pour revenir au menu ou 2 pour quitter "))
             
