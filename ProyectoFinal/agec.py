import random, math, robot as r, sys
import pdb

random.seed(20161)

TAMANO_POBLACION = 20
NUM_ALELOS = 3

MAX_GENERACIONES = 10
MIN_ALELO = 0
MAX_ALELO = 360
PORCENTAJE_MUTACION = 5

MAX_INT = sys.maxsize
MIN_INT = - sys.maxsize
NUM_DECIMALES = 8

class Individuo(object):
	"""docstring for Individuo"""
	def __init__(self, genotipo, posicionBuscada):
		super(Individuo, self).__init__()
		self.__genotipo = genotipo
		self.__fitness = -1
		self.__fx = MAX_INT
		self.__margenError = MAX_INT
		self.__posicionBuscada = posicionBuscada

	def getGenotipo(self): return self.__genotipo
	def getFitness(self): return self.__fitness
	def setFitness(self, fitness): self.__fitness = fitness
	def setFx(self, fx): self.__fx = fx
	def getFx(self): return self.__fx
	def getMargenError(self): return self.__margenError
	def getPosicionBuscada(self): return self.__posicionBuscada

	def setMutacion(self, index, val ) : self.__genotipo[index] = val
	def setMargenError(self, margen): self.__margenError = margen

	def funcionFitness( self ):
		auxFitness = 0

		self.setFx( r.calculaPosicion( self.getGenotipo() ) )
		#print(self.getGenotipo())
		#print(r.calculaPosicion((0,0,0)))
		
		#print(self.getFx(), self.getPosicionBuscada())
		self.setMargenError( r.calculaError( self.getFx(), self.getPosicionBuscada() ) )

		#print( "1 / " + str(self.getMargenError() ) + " = " + str( 1 / self.getMargenError() ) )
		#raw_input()

		try:
			self.setFitness( 1 / self.getMargenError() )
		except ZeroDivisionError:
			self.setFitness( MAX_INT )
		except:
			raise


class Poblacion(object):
	"""docstring for Poblacion"""
	def __init__(self, numAlelos, minAlelo, maxAlelo, tamanoPoblacion,\
				 porcentajeMutacion, posicionBuscada, margenError):
		super(Poblacion, self).__init__()
		self.poblacion = []
		self.hijos = []
		self.minAlelo = minAlelo
		self.maxAlelo = maxAlelo
		#self.maxGeneraciones = maxGeneraciones
		self.tamanoPoblacion = tamanoPoblacion
		self.numAlelos = numAlelos
		self.totalFitness = 0
		self.porcentajeMutacion = float(porcentajeMutacion) / 100
		self.posicionBuscada = posicionBuscada
		self.margenError = margenError

	def getMejor(self): return self.poblacion[-1] 
	def getPosicionBuscada(self): return self.posicionBuscada
	#def generaAlelo(self):	return 	( random.random() * random.randint( self.minAlelo, self.maxAlelo ) )
	def generaAlelo(self): return random.uniform( MIN_ALELO , MAX_ALELO )
	def resetTotalFItness(self): self.totalFitness = 0
	def setPoblacion(self, hijos) : self.poblacion = hijos

	def inicializaPoblacion(self):
		for i in range(self.tamanoPoblacion):
			auxGenoma = []
			for j in range(self.numAlelos):
				auxGenoma.append( self.generaAlelo() )
			self.poblacion.append( Individuo( auxGenoma , self.getPosicionBuscada() ) )

	def calculaFitness(self):
		for individuo in self.poblacion:
			individuo.funcionFitness()
			self.totalFitness += individuo.getFitness()

	def aparear(self, padre, madre):
		numAlelos = random.randint( 1, len( padre.getGenotipo() ) - 1 )

		genoma1 = padre.getGenotipo()[ : numAlelos ] + madre.getGenotipo()[ numAlelos : ]
		genoma2 = madre.getGenotipo()[ : numAlelos ] + padre.getGenotipo()[ numAlelos : ]

		return 	Individuo( genoma1, self.getPosicionBuscada() ) , \
				Individuo( genoma2, self.getPosicionBuscada() )

	def seleccionMejores( self ):
		aux1 = self.ruleta()

		flag = True

		while( flag ):
			aux2 = self.ruleta()

			if aux1 != aux2:
				flag = False

		hijos = self.aparear( aux1, aux2 )

		self.hijos.append( hijos[0] )
		self.hijos.append( hijos[1] )

	def ruleta( self ):
		totalProbabilidad = 0

		elegido = random.random()

		for individuo in self.poblacion:
			aux =  (individuo.getFitness() / self.totalFitness) 
			totalProbabilidad += aux

			if elegido <= totalProbabilidad:
				#print( "Debug: " , totalProbabilidad )
				return individuo

		print(len(self.poblacion))
		return self.poblacion[-1]
		#print( elegido, totalProbabilidad )
		raise

	def imprimirMejor(self, individuo):
		auxImpresion = []
		for j in individuo.getGenotipo():
			print ("{}\t".format( round( j, NUM_DECIMALES )  ) , end=' '  )

		print("f(x) = ", end = "" )
		for i in individuo.getFx():
			print( round( i , NUM_DECIMALES ) , end = ' ' ) 
		print ( round(individuo.getFitness(), NUM_DECIMALES ) , end = ' ' )
		print(" error: " + str( individuo.getMargenError() ) )

	def imprimirPoblacion( self ):
		for individuo in self.poblacion:
			auxImpresion = []
			for j in individuo.getGenotipo():
				print ("{}\t".format( round( j, NUM_DECIMALES )  ) , end=' '  )

			print("f(x) = ", end = "" )
			for i in individuo.getFx():
				print( round( i , NUM_DECIMALES ) , end = ' ' ) 
			print ( round(individuo.getFitness(), NUM_DECIMALES ) , end = ' ' )
			print(" error: " + str( individuo.getMargenError() ) )
		print()
		pass

	def sortPoblacion(self, criterio = None):
		self.setPoblacion( sorted( self.poblacion,key = lambda x: x.getFitness() ) )

	def mutarPoblacion(self):
		numeroMutantes = int(math.ceil(self.tamanoPoblacion * self.numAlelos * self.porcentajeMutacion))

		for i in range( numeroMutantes ):
			aux = self.poblacion[ random.randint( 0, self.tamanoPoblacion - 1 ) ]
			aux.setMutacion( random.randint( 0, self.numAlelos - 1 ) , self.generaAlelo() )

	def cicloPrincipal(self):
		numGeneraciones = 0

		p.inicializaPoblacion()
		p.calculaFitness()
		p.sortPoblacion()
		print("Generacion " + str(numGeneraciones) )
		#p.imprimirPoblacion()

		while ( p.poblacion[-1].getMargenError() > self.margenError ):
			#print(len(self.poblacion))
			self.hijos = []
			self.resetTotalFItness()
			self.sortPoblacion()
			self.calculaFitness()

			while len(self.hijos) < self.tamanoPoblacion:
				self.seleccionMejores()
				self.mutarPoblacion()

			self.setPoblacion( self.hijos )

			#p.sortPoblacion()

			numGeneraciones += 1
			
			if (numGeneraciones % 50) == 0:
				print("Generacion " + str(numGeneraciones) )
				p.calculaFitness()
				p.sortPoblacion()
				p.imprimirMejor( p.getMejor() )
				print()
				#p.imprimirPoblacion()

		'''print("Generacion " + str(numGeneraciones) )
		p.calculaFitness()
		p.sortPoblacion()
		p.imprimirPoblacion()'''
			
		print( p.poblacion[-1].getFx() )
		print( p.poblacion[-1].getMargenError() )
		print( numGeneraciones )

if __name__ == '__main__':
	posicionBuscada = ( int(sys.argv[1]), int(sys.argv[2]) , int(sys.argv[3]) )
	margenError = 2.5

	p = Poblacion( 	NUM_ALELOS, MIN_ALELO, MAX_ALELO, TAMANO_POBLACION, \
					PORCENTAJE_MUTACION, posicionBuscada, margenError)

	p.cicloPrincipal()
