import Poblacion

NUM_DIMENSIONES = 10
NUM_INDIVIDUOS = 20
FACTOR_ESCALA = None 	# [ 0.4 , 0.9 ]
RANGO_CRUCE = None 		#[ 0.1, 1.0]

MAX_GENERACIONES = 40
RANGO_MIN = -5
RANGO_MAX = 5


def fit( lista ):
	res = 0 

	for i in range( len( lista ) ):
		res += i ** 2

	return res

#Poblacion(self, numIndividuos, rangoMin, rangoMax, numDimensiones, funcionFitness):

class EvolucionDiferencial():
	def __init__(self):
		p = Poblacion.Poblacion( NUM_INDIVIDUOS, RANGO_MIN, RANGO_MAX, NUM_DIMENSIONES, fit)

		p.correCiclo()

if __name__ == '__main__':
	EvolucionDiferencial()