/* hey...this is the implementation of quicksort in CLRS, i like this one :-) */

#include<iostream>

using namespace std;

int partition(int *A, int p, int r)
{
	int x=A[r];
	int i=p-1;
	for(int j=p;j<=r-1;j++)
	{
		if(A[j]<=x)
		{
			i++;
			swap(A[i],A[j]);
		}
	}
	swap(A[i+1],A[r]);
	return i+1;
}

void quicksort(int *A, int p, int r)
{
	if(p<r)
	{
		int q=partition(A,p,r);
		quicksort(A,p,q-1);
		quicksort(A,q+1,r);
	}
}

int main()
{
	int A[6]={9,10,6,12,0,-1};
	quicksort(A,0,5);
	for(auto i:A)cout<<i<<" ";
	cout<<endl;
	return 0;
} 
