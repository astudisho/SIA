import enjambre as enj

enj.rnd.seed(5)

'''
	Enjambre(self, numParticulas, numGeneraciones, numDimensiones, tamVecindario, 
				 rangoMin, rangoMax, velocidadMax, funcionFitness):
'''

NUM_PARTICULAS = 20
NUM_GENERACIONES = 40
NUM_DIMENSIONES = 10
TAM_VECINDARIO = 10
RANGO_MIN = -5
RANGO_MAX = 5
VELOCIDAD_MIN = (RANGO_MAX - RANGO_MIN) * 0.10
VELOCIDAD_MAX = (RANGO_MAX - RANGO_MIN) * 0.20	#10% a 20% del espacio de busqued

PHI_1 = [] 			#Aleatorio para cada individuo
PHI_MAX = 2.05		#Phi maximo varia dependiendo quien tiene mayor influencia
PHI_2 = []			#Aleatorio para cada individuo
PHI_2_MAX = 2.05	#Phi maximo 

def fitness( posicion ):
	suma = 0
	for i in posicion:
		suma += pow( i , 2 )

	return suma

if __name__ == '__main__':
	e = enj.Enjambre( 	NUM_PARTICULAS, NUM_GENERACIONES, NUM_DIMENSIONES, \
						TAM_VECINDARIO, RANGO_MIN, RANGO_MAX, VELOCIDAD_MIN ,\
						VELOCIDAD_MAX, fitness, PHI_MAX)
	
	while e.getContadorGeneraciones() < NUM_GENERACIONES:
		e.correGeneracion()

		if (e.getContadorGeneraciones() % 10) == 0\
			or e.getContadorGeneraciones() == 1:
			e.imprimeMuestra()
			#print( "Generacion " + str( e.getContadorGeneraciones() ) + '\n\n' )
			#print(e)