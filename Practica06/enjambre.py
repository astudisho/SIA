import particula as par
import random as rnd
import math

class Enjambre():
	def __init__(self, numParticulas, numGeneraciones, numDimensiones, tamVecindario, 
				 rangoMin, rangoMax, velocidadMin, velocidadMax, funcionFitness, maxPhi):

		self.__numParticulas = numParticulas
		self.__particulas = []
		self.__tamVecindario = tamVecindario
		self.__numDimensiones = numDimensiones

		self.__mejorParticulaGlobal = None

		self.__contadorGeneraciones = 0

		for x in range(self.__numParticulas):
			self.__particulas.append( par.Particula( numDimensiones, tamVecindario, \
													 rangoMin, rangoMax, velocidadMin,\
													 velocidadMax, funcionFitness, maxPhi ) )

	def getContadorGeneraciones(self): return self.__contadorGeneraciones

	def __str__(self):
		string = "Enjambre" + "\n\n"

		for particula in self.__particulas:
			string += str( particula )

		return string

	def calculaVecindarios(self):
		for x in self.__particulas:
			listaDistancias = []

			for indiceY, y in enumerate( self.__particulas ): 
				sumatoria = 0

				for i in range(self.__numDimensiones):
					sumatoria += pow( x.getPosicion()[i] - y.getPosicion()[i] , 2 )

				distancia = math.sqrt( sumatoria ) 
				listaDistancias.append( ( distancia, indiceY ) )

			listaDistancias = sorted( listaDistancias )
			listaDistancias.pop( 0 )
			vecindario = []

			for indice in listaDistancias[ : self.__tamVecindario ]:
				vecindario.append( self.__particulas[ indice[1] ] )

			x.setVecindario( vecindario )
			#print( "Vecindario",vecindario)

	def imprimeMuestra(self):
		print( "Generacion " + str( self.__contadorGeneraciones ) )
		print( "Mejor particula" )
		print( str(self.__particulas[ 0 ] ) )
		#print( '\n' )

		print( "Peor particula" )
		print( str(self.__particulas[ -1 ] ) )
		#print( '\n' )


	def correGeneracion(self):
		self.calculaVecindarios()

		for particula in self.__particulas:
			particula.calculaMejorVecino()
			particula.calculaVelocidad()
			particula.calculaPosicion()

		self.__particulas = sorted( self.__particulas, key= lambda par: par.getFitness() )

		self.__contadorGeneraciones += 1