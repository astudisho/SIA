#include <cstdlib>
#include <float.h>
#include <iostream>
#include <ctime>
#include <cmath>

using namespace std;

int a[11] = {0};

int numeroAleatorio();

//srand (time(NULL));

int main()
{
	for (int i = 0; i < 1000000; ++i)
	{
		a [ numeroAleatorio() + 5 ] ++ ;
	}

	for (int i = 0; i < 11; i++ )
	{
		cout << i - 5 << " : " << a[i] << endl;
	}
}

int numeroAleatorio()
{
	int res = round((float)rand()/(float)(RAND_MAX/10))-5;
	return res;
}