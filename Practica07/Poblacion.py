import random as rnd
import Individuo
import copy

random.seed( 1234567890 )
#Individuo( self, numDimensiones, rangoMin, rangoMax, funcionFitness )

class Poblacion():
	def __init__(self, numIndividuos, rangoMin, rangoMax, numDimensiones, funcionFitness, factorEscala):
		self.__numIndividuos = numIndividuos
		self.__poblacion = []
		self.__poblacionU = []
		self.__fatorEscala = factorEscala

		for i in range( numIndividuos ):
			self.__poblacion.append( Individuo.Individuo( numDimensiones, rangoMin, rangoMax, funcionFitness ) )

	def F( self, ind1, factor ):
		aux = copy.deepcopy( ind1 )
		auxArreglo = []

		for i in range( len( ind1.getSolucion() ) ):
			auxArreglo.append( ind1.getSolucion()[ i ] * factor )

		aux.setSolucion( auxArreglo )

		return aux


	def getPoblacion(self): return self.__poblacion

	def getMuestra(self, propio, numIndividuos = 3):
		muestra = [ propio ]

		while muestra.count( propio ) != 0:
			muestra = rnd.sample( self.__poblacion , numIndividuos )

		return muestra
	def getRandom(self, rMin, rMax): return rnd.uniform( rMin, rMax )

	def correCiclo(self):
		for individuo in self.__poblacion:
			r1, r2, r3 = self.getMuestra( individuo )

			vi = Individuo.Individuo.suma( r1 , self.F( Individuo.Individuo.resta( r2, r3 ), self.__fatorEscala ) )
			
			jr = self.getRandom( 0 , 1 )

			self.__poblacionU = []

			for j in range( len( self.__poblacion ) ):
				uij = copy.deepcopy( self.__poblacion[ 0 ] )

				rcj = self.getRandom( 0, 1 )

				if ( rcj <  self.__fatorEscala ) or ( j == jr ):
					self.__poblacionU.append( vi )

				else:
					self.__poblacionU.append( individuo )


		for i in range( self.__numIndividuos ):
			self.__poblacion[ i ].calculaFitness()
			self.__poblacionU[ i ].calculaFitness()
			print(self.__poblacion[ i ].getFitness(), self.__poblacionU[ i ].getFitness())

			if self.__poblacion[ i ].getFitness() < self.__poblacionU[ i ].getFitness():
				print("Mejor que el otro")
				self.__poblacion[ i ] = self.__poblacionU[ i ]