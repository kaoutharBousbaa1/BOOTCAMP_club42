printf("This is an interactive guessing game! \n You have to enter a number between 1 and 99 to find out the secret number.\n Type '0' to end the game.\n Good luck!\n")
NombreMystere = 0, NombreChoisi = 0, ContinuerPartie = 0, coups = 0
while ContinuerPartie != 0:
  while NombreChoisi != NombreMystere:
      NombreMystere = randint(1,99)
      NombreChoisi = int(input("Quel est le nombre? "))
      
      if NombreMystere > NombreChoisi:
          printf("C'est plus!\n")
          coups++
      elif NombreMystere < NombreChoisi:
          printf("C'est moins!\n")
          coups++
      else:
          printf("Bravo!! Vous avez trouvez le nombre mystere! avec un nombre des coups %d\n", %coups)
          ContinuerPartie = int(input("Voulez-vous continuer?(0/1)"))
       

