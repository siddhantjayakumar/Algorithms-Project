// Ben Catterall
// 05/02/2014
// Fast matrix multiplication calculation using dynamic programming and the memoization technique 

#include <iostream>
#include <limits>

#define NUM_MATRICES 6
using namespace std;

int minMatrix(int i, int j);
void printMulOrder(int j, int i);
void printMatrix(int matrix[][NUM_MATRICES], int n) ;

//The dimensions of the matrices.
// M:	A	A   A ...     A
// i: 1    2  3   ... n-1   n 
// Hence, a matrix's dimensions are given by dimensions[i-1] and dimensions[i] as i is one indexed for logic
// but adjusted to be zero indexed in the code.
int dimensions[] = {30,35,15,5,10,20,25};

//The memoization of the number of multiplications (values above upper diagonal)
//and the split point (values below the upper diagonal)
int memo[NUM_MATRICES][NUM_MATRICES];


int main(int argc, char **argv) 
{
	//calculate the minimum matrix order
	minMatrix(1,NUM_MATRICES);
	cout << "Minimum number of scalar multiplications: " << minMatrix(1,NUM_MATRICES) << endl << endl;
	
	printMatrix(memo, NUM_MATRICES);
	
	//prints the order to multiply the matrices to achieve this minimum
	cout << "Matrix order: ";
	printMulOrder(1,6);
	
	return 0;
}
//Print the multiplication order for the matrix
//PRECONDITION: 1 <= i <= j <= NUM_MATRICES
void printMulOrder(int i, int j)
{
	if( i == j) {
		cout << "(A" << i << ")";
		return;
	}
	cout << "(";

	int k = memo[j-1][i-1];
	printMulOrder(i, k);
	printMulOrder(k+1, j);
	cout << ")";
}

//Calculate the minimum number of  multiplication operations needed to multiply the set of matrices together
//PRECONDITION: 1 <= i <= j <= NUM_MATRICES
int minMatrix(int i, int j) 
{
	if( i == j)
		return 0;
	int minK = i;
	
	int min = std::numeric_limits<int>::max();
	
	//Check all possible places to partition
	for(int k = i; k <j; k++)
	{
		//if we already have a value, use it. Otherwise, calculate it.
		int minIK = 0;
		if(memo[i-1][k-1] != 0)
			minIK = memo[i-1][k-1]; 
		else 
			minIK = minMatrix(i, k);
		
		//if we already have a value, use it. Otherwise, calculate it.
		int minKPlusOneJ = 0;
		if(memo[k+1-1][j-1] != 0)
			minKPlusOneJ = memo[k+1-1][j-1];
		else 
			minKPlusOneJ = minMatrix(k+1, j);	
			
		int thisMin = (minIK + minKPlusOneJ + dimensions[i-1]*dimensions[k]*dimensions[j]);
		
		//if this gives a smaller number of multiplications than the current number, use it.
		if(thisMin < min)
		{
			min = thisMin;
			minK = k;
		}
	}
	//remember the value and the k that yielded this value
	memo[i-1][j-1] = min;
	memo[j-1][i-1] = minK;
	return min;
}

//Prints out a matrix
void printMatrix(int matrix[][NUM_MATRICES], int n) 
{
	for(int i = 0; i <n; i++)
	{
		for(int j = 0; j < n; j++)
			cout << matrix[i][j] << " " ;
		cout << endl;
	}
		
	cout << endl;
}