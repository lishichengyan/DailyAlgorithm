/* hey...this is the implementation of quicksort in CLRS, i like this one :-) */

#include<iostream>

using namespace std;

// 循环不变式是i前面的元素永远比pivot大。
// 可以这样想：当A[j]小的时候i跟进，ij重合，交换不起作用，
// 如果A[j]大，那么ij就会远离，i留在原来比pivot小的地方，
// 但是一越过去就比pivot大。
// 总之就是让i一直保持在这种微妙的位置上。
int partition(int *A, int p, int r)
{
	int x=A[r];
	int i=p-1;
	for(int j=p;j<=r-1;j++)
	{
		if(A[j]<=x)
		{
			i++;
			swap(A[i],A[j]); // 当 i == j 时存在不必要的交换
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
