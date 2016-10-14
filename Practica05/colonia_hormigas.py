import random, math, numpy as np

MIN = -5
MAX = 5
STEP = 10./16

VALOR_INICIAL = 0
NUMERO_HORMIGAS = NUMERO_CIUDADES = 20

MAX_GENERACIONES = 1
ALFA = 1
BETA = 5
Q_DEPOSITO = 20
P_EVAPORACION = 0.9
PI_0 = 10e-6

'''probabilidad = 	( ( feromonas_camino ^ importancia_feromona ) / ( distancia_camino ^ importancia_distancia ) ) / \
				( ( suma_feromonas ^ importancia_feromona ) / ( suma_distancias ^ importancia_distancia ) ) '''

class Camino(object):
	"""docstring for Camino"""
	def __init__(self, distancia ):
		super(Camino, self).__init__()
		self.__distancia = abs(distancia)
		self.__feromonas = PI_0

	def __str__(self): return "Dst: " + str( round( self.__distancia , 3 ) ) + " Fer: " + str(self.__feromonas)

	def getDistancia( self ):	return self.__distancia
	def getFeromona( self ): return self.__feromonas
	def evaporaFeromona( self , evaporacion = P_EVAPORACION ): self.__feromonas *= evaporacion
	def depositaFeromona( self, deposito = Q_DEPOSITO ) : self.__feromonas += deposito

class CaminosNodo(object):
	"""docstring for CaminosNodo"""
	def __init__(self, caminos):
		super(CaminosNodo, self).__init__()

		self.__sumaDistancias = 0
		self.__sumaFeromonas = 0
		self.__caminos = []

		for i in caminos:
			self.__caminos.append( Camino( i ) )

		self.calculaSumaFeromonas()
		self.calcularSumaDistancias()

	def getCaminos(self): return self.__caminos

	def __str__(self) : return 	"SumaDistancias: " + str(self.__sumaDistancias) + \
								" SumaFeromonas: " +str(self.__sumaFeromonas)

	def calculaSumaFeromonas(self):
		self.__sumaFeromonas = 0

		for camino in self.__caminos:
			self.__sumaFeromonas += camino.getFeromona()

	def calcularSumaDistancias(self):
		self.__sumaDistancias = 0

		for camino in self.__caminos:
			self.__sumaDistancias += camino.getDistancia()

	def evaporaFeromonas(self):
		for camino in self.__caminos:
			camino.evaporaFeromonas( P_EVAPORACION )

	def ruleta( self ):
		totalProbabilidad = 0

		elegido = random.random()

		print("Elegido " , elegido)
		
		for camino in self.__caminos:
			print("Camino: " + str(camino) )
			'''probabilidad =  ( ( camino.getFeromona() ** ALFA / camino.getDistancia() ** BETA ) )/ \
							( ( self.__sumaFeromonas ** ALFA / self.__sumaDistancias ** BETA ) )'''

			arriba = camino.getFeromona() ** ALFA / camino.getDistancia() ** BETA
			abajo = self.__sumaFeromonas ** ALFA / self.__sumaDistancias ** BETA

			print("Arriba = " , arriba )
			print("Abajo = ", abajo )

			print(arriba / float(abajo))

			#print("probabilidad: " + str(probabilidad) )

			totalProbabilidad += probabilidad

			if elegido <= totalProbabilidad:
				print( "Debug: " , totalProbabilidad )
				return camino

		print(len(self.poblacion))
		return self.__caminos[ -1 ]
		#print( elegido, totalProbabilidad )
		raise
		

class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, valor, nombre ):
		super(Nodo, self).__init__()
		self.__valor = valor
		self.__nombre = nombre

	def __str__(self): return self.__nombre + " : " + str( self.__feromonas )

	def getNombre(self):	return self.__nombre
	def getCoordenada(self): return self.__valor

class Hormiga():
	def __init__(self, nodoInicio):
		self.__nodoInicio = nodoInicio
		self.__distanciaRecorrida = 0
		self.reset()

	def reset(self):
		self.__nodosVisitados = [ self.__nodoInicio ]

		self.__nodosPorVisitar = range( NUMERO_CIUDADES )
		self.__nodosPorVisitar = self.__nodosPorVisitar.remove( self.__nodoInicio )
		self.__distanciaRecorrida = 0

	def recorreNodos(self):
		nodoActual = self.__nodoInicio

		while( len(self.__nodosVisitados) == NUMERO_CIUDADES ):
			caminoElegido = ColoniaHormigas.CAMINOS[ nodoActual ] . ruleta()

			print(caminoElegido.getDistancia())


class ColoniaHormigas(object):
	"""docstring for ColoniaHormigas"""
	def __init__(self):
		super(ColoniaHormigas, self).__init__()
	
	CAMINOS = []
	HORMIGAS = []
	#CAMINOS = [ ([  ] * NUMERO_CIUDADES) for x in range(NUMERO_CIUDADES) ]
	for x in range(NUMERO_CIUDADES):
		CAMINOS.append( CaminosNodo(np.arange(MIN, MAX, STEP) ) )

	def cicloPrincipal(self):
		contadorGeneraciones = 0

		while( contadorGeneraciones != MAX_GENERACIONES ):

			for hormiga in colonia.HORMIGAS:
				pass

			contadorGeneraciones += 1

if __name__ == '__main__':
	colonia = ColoniaHormigas()
	hormiga = Hormiga(0)

	'''for i in ColoniaHormigas.CAMINOS:
		print(i)'''
	#ColoniaHormigas.CAMINOS[0].calcularSumaDistancias()
	#ColoniaHormigas.CAMINOS[0].calculaSumaFeromonas()

	print(ColoniaHormigas.CAMINOS[0])

	print(ColoniaHormigas.CAMINOS[0].ruleta())