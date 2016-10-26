import random as rnd
import copy

class Individuo():
	def __init__(self, numDimensiones, rangoMin, rangoMax, funcionFitness):
		self.__solucion = []
		self.__numDimensiones = numDimensiones
		self.__rangoMin = rangoMin
		self.__rangoMax = rangoMax
		self.__fitness = None
		self.__funcionFitness = funcionFitness

		for i in range( self.__numDimensiones ):
			self.__solucion.append( self.getRandom( self.__rangoMin, self.__rangoMax ) )


	def getSolucion(self): return self.__solucion
	def getNumDimensiones(self): return self.__numDimensiones
	def getFitness(self): return self.__fitness
	def calculaFitness(self): self.__fitness = self.__funcionFitness( self.__solucion )
	def getRandom(self, rMin, rMax): return rnd.uniform( rMin, rMax)
	def setSolucion(self, solucion): self.__solucion = solucion

	@staticmethod
	def suma( ind1, ind2 ):
		print("SUMA", ind2.getSolucion() )
		aux = copy.deepcopy( ind1 )
		vectorAux = []

		for i in range( len( aux.getSolucion() ) ) :
			vectorAux.append( ind1.getSolucion()[ i ] + ind2.getSolucion()[ i ] )

		aux.setSolucion( vectorAux )

		return aux

	@staticmethod
	def resta(ind1, ind2):
		print("RESTA", ind1.getSolucion() )
		print("RESTA", ind2.getSolucion() )
		aux = copy.deepcopy( ind1 )
		vectorAux = []

		for i in range( len( aux.getSolucion() ) ) :
			vectorAux.append( ind1.getSolucion()[ i ] - ind2.getSolucion()[ i ] )

		aux.setSolucion( vectorAux )

		print(vectorAux)

		input()

		return aux