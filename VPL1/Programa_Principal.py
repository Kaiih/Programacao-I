import sys
from Roupa import Roupa

##################################################

a=Roupa()
a.Calcula_Total()
a.Leitura()
print(a.toString())

del(a)

sys.exit(0)