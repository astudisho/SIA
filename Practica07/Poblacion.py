import random as rnd
import Individuo

#Individuo( self, numDimensiones, rangoMin, rangoMax, funcionFitness )

class Poblacion():
	def __init__(self, numIndividuos, rangoMin, rangoMax, numDimensiones, funcionFitness):
		self.__numIndividuos = numIndividuos	
		self.__poblacion = []

		for i in range( numIndividuos ):
			self.__poblacion.append( Individuo.Individuo( numDimensiones, rangoMin, rangoMax, funcionFitness ) )

	def getPoblacion(self): return self.__poblacion

	def getMuestra(self, propio, numIndividuos = 3):
		muestra = [ propio ]

		while muestra.count( propio ) != 0:
			muestra = rnd.sample( self.__poblacion , numIndividuos )

		return muestra
	def getRandom(self): return rnd.uniform( rMin, rMax )

	def correCiclo(self):
		for individuo in self.__poblacion:
			r1, r2, r3 = self.getMuestra( individuo )

			print( r1.getSolucion() )

			vi = Individuo.Individuo.suma( r1 ,Individuo.Individuo.resta( r2, r3 ) )