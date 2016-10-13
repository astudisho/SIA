import random
import matplotlib.pyplot as ppl

random.seed(1)

NUM_DECIMALES = 4
MAX_POBLACION = 128
TAMANO_DICCIONARIO = 32
OFFSET = 270
MAX_GENERACIONES = 128
AUMENTO = 1

def funcionFitness( x ):
	return  ( ( - ( abs (x[0] + 2*x[1] + 3*x[2] + 4*x[3] - 30) ) ) + OFFSET) * AUMENTO

def funcionFx( x ):
	return x[0] + 2*x[1] + 3*x[2] + 4*x[3] - 30

class Individuo(object):
	"""docstring for Individuo"""
	def __init__(self, genoma, fenotipo):
		super(Individuo, self).__init__()
		
		self.genoma = genoma
		self.fenotipo = fenotipo
		self.fitness = -1
		self.fx = None

	def setFitness(self, fitness):		self.fitness = fitness
	def setFx(self, fx): 	self.fx = fx

class Poblacion(object):
	"""docstring for Poblacion"""

	diccionarioGenomico = \
		{
		 "00000" : 0,	"00001" : 1.,  	"00010" : 2.,	 "00011" : 3.,	
		 "00100" : 4.,	"00101" : 5.,	"00110" : 6.,	 "00111" : 7.,
		 "01000" : 8.,	"01001" : 9.,	"01010" : 10.,	 "01011" : 11.,
		 "01100" : 12.,	"01101" : 13.,	"01110" : 14.,	 "01111" : 15., 

		 "10000" : 16.,	"10001" : 17.,  "10010" : 18.,	 "10011" : 19.,	
		 "10100" : 20.,	"10101" : 21.,	"10110" : 22.,	 "10111" : 23.,
		 "11000" : 24.,	"11001" : 25.,	"11010" : 26.,	 "11011" : 27.,
		 "11100" : 28.,	"11101" : 29.,	"11110" : 30., 	 "11111" : 30.
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


		return 	Individuo( genoma1, self.getFenotipo( genoma1 ) ) , \
				Individuo( genoma2, self.getFenotipo( genoma2 ) )

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

	def getFenotipo(self, genoma):		
		return	self.diccionarioGenomico[ genoma[0] ] ,\
				self.diccionarioGenomico[ genoma[1] ] ,\
				self.diccionarioGenomico[ genoma[2] ] ,\
				self.diccionarioGenomico[ genoma[3] ]

	def inicializaPoblacion(self):
		for i in range ( 0 ,  MAX_POBLACION):

			auxGenoma = (self.diccionarioGenomico.keys()[random.randint(0, TAMANO_DICCIONARIO - 1)],\
						self.diccionarioGenomico.keys()[random.randint(0, TAMANO_DICCIONARIO - 1)],\
						self.diccionarioGenomico.keys()[random.randint(0, TAMANO_DICCIONARIO - 1)],\
						self.diccionarioGenomico.keys()[random.randint(0, TAMANO_DICCIONARIO - 1)])

			nuevoIndividuo = Individuo( auxGenoma , self.getFenotipo( auxGenoma ) )

			self.poblacion.append( nuevoIndividuo )

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

		return self.poblacion[-1]
		#print( elegido, totalProbabilidad )
		raise

	def imprimirPoblacion( self ):
		self.poblacion = sorted( self.poblacion , key= lambda ind: ind.fitness )

		print("Poblacion: ")
		for ind in self.poblacion:
			print( ind.genoma , ind.fenotipo , ind.fitness , ind.fx)


	def graficarPoblacion( self , numGeneracion):
		self.poblacion = sorted( self.poblacion , key= lambda ind: ind.fitness )

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

	def calcularFx( self ):
		for ind in self.poblacion:
			ind.setFx( funcionFx( ind.fenotipo ) )

	def sortPoblacion(self, criterio = None):
		self.poblacion = sorted( self.poblacion,key = lambda x: x.fitness )


def cicloPrincipal( maxGeneraciones ):
	numGeneraciones = 0

	p = Poblacion(funcionFitness)
	p.inicializaPoblacion()
	p.calcularFitness()
	p.imprimirPoblacion()

	while( numGeneraciones != maxGeneraciones ):
		#p.poblacionNueva.clear()
		del( p.poblacionNueva[:] )
		p.resetTotalFitness()
		p.calcularFitness()

		while( len( p.poblacionNueva) != MAX_POBLACION ):
			p.seleccionMejores()

		#p.poblacion = p.poblacionNueva
		p.setPoblacion( p.poblacionNueva )
		p.calcularFitness()
		p.sortPoblacion()
		#p.imprimirPoblacion()

		numGeneraciones += 1

		if (numGeneraciones % 32) == 0:
			p.calcularFitness()
			p.calcularFx()
			p.imprimirPoblacion()

			raw_input()
if __name__ == '__main__':
	cicloPrincipal( MAX_GENERACIONES )