from matrizEsparsa import matrizEsparsa

A = matrizEsparsa()
B = matrizEsparsa()


A.set(1,1,4)
B.set(1,1,5)

A.multiplica_escalar(2)
B.multiplica_escalar(3)

A.print()
B.print()

C = A.multiplica_matrizes(B)

C.print()

