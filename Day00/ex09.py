NombreMystere = 0, NombreChoisi = 0, ContinuerPartie = 0, MAX = 0, coups = 0, MIN = 1
while (ContinuerPartie != 0)
  while(NombreChoisi != NombreMystere)

      srand(time(NULL))
      NombreMystere = (rand() % (MAX - MIN +1)) + MIN
      NombreChoisi = input("Quel est le nombre? ")
      
      if (NombreMystere > NombreChoisi) 
          printf("C'est plus!\n")
          coups++
      else if(NombreMystere < NombreChoisi) 
          printf("C'est moins!\n")
          coups++
      else
          printf("Bravo!! Vous avez trouvez le nombre mystere! avec un nombre des coups %d\n",&coups)
          ContinuerPartie = input("Voulez-vous continuer?(0/1)")
       

