import random
import matplotlib.pyplot as ppl

NUM_DECIMALES = 4
NUM_POBLACION = 16
OFFSET = 17
MAX_GENERACIONES = 30

class Individuo(object):
	"""docstring for Individuo"""
	def __init__(self, genoma, fenotipo):
		super(Individuo, self).__init__()
		
		self.genoma = genoma
		self.fenotipo = fenotipo
		self.fitness = -1

	def setFitness(self, fitness):
		self.fitness = fitness

class Poblacion(object):
	"""docstring for Poblacion"""

	diccionarioGenomico = \
		{
		 "0000" : -4.0,	 "0001" : -3.8,  "0010" : -3.6,	 "0011" : -3.4,	
		 "0100" : -3.2,	 "0101" : -3.0,	 "0110" : -2.8,	 "0111" : -2.6,
		 "1000" : -2.4,	 "1001" : -2.2,	 "1010" : -2.0,	 "1011" : -1.8,
		 "1100" : -1.6,	 "1101" : -1.4,	 "1110" : -1.2,	 "1111" : -1.0 
		}

	def __init__(self, funcionFitness ):
		super(Poblacion, self).__init__()

		self.poblacion = []
		self.poblacionNueva = []

		self.funcionFitness = funcionFitness
		self.totalFitness = 0

	def setPoblacion(self, poblacion ): self.poblacion = poblacion

	def aparear(self, padre, madre):

		numAlelos = random.randint( 1, len( padre.genoma ) - 1 )

		genoma1 = padre.genoma[ : numAlelos ] + madre.genoma[ numAlelos : ]
		genoma2 = madre.genoma[ : numAlelos ] + padre.genoma[ numAlelos : ]

		return 	Individuo( genoma1, self.diccionarioGenomico[genoma1] ) , \
				Individuo( genoma2, self.diccionarioGenomico[genoma2] )

	def seleccionMejores( self ):
		aux1 = self.ruleta()

		flag = True

		while( flag ):
			aux2 = self.ruleta()

			if aux1 != aux2:
				flag = False

		hijos = self.aparear( aux1, aux2 )

		self.poblacionNueva.append( hijos[0] )
		self.poblacionNueva.append( hijos[1] )

	def inicializaPoblacion(self):
		for ind in Poblacion.diccionarioGenomico:
			self.poblacion.append( Individuo( ind , Poblacion.diccionarioGenomico[ ind ] ) )

		self.poblacion = sorted( self.poblacion , key= lambda ind: ind.fenotipo )

	def resetTotalFitness( self ) : self.totalFitness = 0

	def calcularFitness( self ):
		for individuo in self.poblacion:
			fitness = round( self.funcionFitness( individuo.fenotipo ) , NUM_DECIMALES )
			individuo.setFitness( fitness )
			self.totalFitness += fitness
			#print( individuo.genoma + ' : ' + str( self.funcionFitness( individuo.fenotipo ) ) )

	def ruleta( self ):
		totalProbabilidad = 0

		elegido = round( random.random() , NUM_DECIMALES )

		for individuo in self.poblacion:
			aux =  (individuo.fitness / self.totalFitness) 
			totalProbabilidad += aux

			if elegido <= totalProbabilidad:
				#print( "Debug: " , totalProbabilidad )
				return individuo

		raise

	def imprimirPoblacion( self ):
		print("Poblacion: ")
		for ind in self.poblacion:
			print( ind.genoma , ind.fenotipo , ind.fitness )


	def graficarPoblacion( self , numGeneracion):
		poblacionX = []
		poblacionY = []

		for ind in self.poblacion:
			poblacionX.append( ind.fenotipo )
			poblacionY.append( ind.fitness )

		print( poblacionX )

		ppl.title( "Generacion " + str(numGeneracion) )
		ppl.xlabel("Fenotipo")
		ppl.ylabel("Fitness")

		ppl.ylim( ymax = 30, ymin = 0 )
		ppl.xlim( xmax = -.5, xmin = -4.5 )
		ppl.grid( True )
		ppl.plot( poblacionX, poblacionY, 'ro')
		ppl.show()

def cicloPrincipal( maxGeneraciones ):
	numGeneraciones = 0

	p = Poblacion( lambda x: -( x**4 + 5*x**3 + 4*x**2 - 4*x + 1 ) + OFFSET )
	p.inicializaPoblacion()
	p.calcularFitness()
	p.graficarPoblacion(0)

	while( numGeneraciones != maxGeneraciones ):
		#p.poblacionNueva.clear()
		del( p.poblacionNueva[:] )
		p.resetTotalFitness()
		p.calcularFitness()

		while( len( p.poblacionNueva) != NUM_POBLACION ):
			p.seleccionMejores()

		#p.poblacion = p.poblacionNueva
		p.setPoblacion( sorted( p.poblacionNueva , key= lambda ind: ind.fenotipo ) )

		numGeneraciones += 1

		if numGeneraciones % (maxGeneraciones / 5) == 0 :
			p.calcularFitness()
			p.imprimirPoblacion()
			p.graficarPoblacion( numGeneraciones )
	

if __name__ == '__main__':
	cicloPrincipal( MAX_GENERACIONES )