#include <ctime>
#include <iostream>
#include <cstdio>
#include <cstdlib>

const int 	NUMERO_VARIABLES = 11, 
			NUMERO_ITERACIONES = 100000;

using namespace std;

float randomFloat( float a , float b );

int main
{
	int a[NUMERO_VARIABLES] = {0}, b[NUMERO_VARIABLES] = {0};

	srand (time(NULL));


	for (int i = 0; i < NUMERO_ITERACIONES; ++i)
	{
		a[ (int)(randomFloat( -5 , 5 ) + 5)  ] ++;
	}


	for (int i = 0; i < NUMERO_VARIABLES; ++i)
	{
		cout << i - 5 <<" : " << a[i] << endl;
	}

	cout << rand() << endl;
		
}

float randomFloat(float a, float b) 
{
    float random = ((float) rand()) / (float) RAND_MAX;
    float diff = b - a;
    float r = random * diff;
    return a + r;
}