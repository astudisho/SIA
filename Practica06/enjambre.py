import particula as par
import random as rnd
import math

class Enjambre():
	def __init__(self, numParticulas, numGeneraciones, numDimensiones, tamVecindario, 
				 rangoMin, rangoMax, velocidadMax, funcionFitness):

		self.__numParticulas = numParticulas
		self.__particulas = []
		self.__tamVecindario = tamVecindario

		self.__mejorParticulaGlobal = None

		for x in range(self.__numParticulas):
			self.__particulas.append( par.Particula( numDimensiones, tamVecindario, \
													 rangoMin, rangoMax, velocidadMax,\
													 funcionFitness ) )

	def calculaVecindarios(self):
		for x in self.__particulas:
			listaDistancias = []

			for indiceY, y in enumerate( self.__particulas ): 
				sumatoria = 0

				for i in range(self.__numParticulas):
					sumatoria += pow( x.getPosicion()[i] - y.getPosicion()[i] , 2 )

				distancia = math.sqrt( sumatoria ) 
				listaDistancias.append( ( distancia, indiceY ) )

			listaDistancias = sorted( listaDistancias )
			listaDistancias.pop( 0 )
			vecindario = []

			for indice in listaDistancias[ : self.__tamVecindario ]:
				vecindario.append( self.__particulas[ indice[1] ] )

			x.setVecindario( vecindario )

			print( vecindario[0])