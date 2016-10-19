import enjambre as enj

'''
	Enjambre(self, numParticulas, numGeneraciones, numDimensiones, tamVecindario, 
				 rangoMin, rangoMax, velocidadMax, funcionFitness):
'''

NUM_PARTICULAS = 20
NUM_GENERACIONES = 40
NUM_DIMENSIONES = 10
TAM_VECINDARIO = 2
RANGO_MIN = -5
RANGO_MAX = 5
VELOCIDAD_MAX = 2	#10% a 20% del espacio de busqued
PHI_1 = [] 			#Aleatorio para cada individuo
PHI_1_MAX = 2.05	#Phi maximo varia dependiendo quien tiene mayor influencia
PHI_2 = [] 			#Aleatorio para cada individuo
PHI_2_MAX = 2.05		#Phi maximo 

def fitness( posicion ):
	suma = 0
	for i in posicion:
		suma += pow( i , 2 )

	if suma == 0:
		return MAXINT, suma
	else:
		return 1 / suma, suma

if __name__ == '__main__':
	e = enj.Enjambre( 	NUM_PARTICULAS, NUM_GENERACIONES, NUM_DIMENSIONES, \
						TAM_VECINDARIO, RANGO_MIN, RANGO_MAX, VELOCIDAD_MAX, fitness)
	e.calculaVecindarios()