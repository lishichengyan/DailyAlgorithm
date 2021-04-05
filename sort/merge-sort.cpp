// 不需要temp数组的版本
// 以及非递归的版本
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cmath>

using namespace std;


void merge(int a[], int ls, int mid, int re){
	int lsize = mid - ls + 1;
	int rsize = re - mid;
	int rs = mid + 1;
	int i, j, k;
	
	int larr[lsize];
	int rarr[rsize];
	
	for(i = 0; i < lsize; i++){
		larr[i] = a[i + ls];
	}
	for(j = 0; j < rsize; j++){
		rarr[j] = a[j + rs];
	}
	
	i = j = 0;
	k = ls;
	while(i < lsize && j < rsize){
		if(larr[i] <= rarr[j]){
			a[k++] = larr[i++];
		}else{
			a[k++] = rarr[j++];
		}
	}
	
	while(i < lsize) a[k++] = larr[i++];
	while(j < rsize) a[k++] = rarr[j++]; 
}

void mergesort(int a[], int l, int r){
	if(l < r){
		int mid = l + (r - l) / 2;
		mergesort(a, l, mid);
		mergesort(a, mid + 1, r);
		merge(a, l, mid, r);
	}
}

void iter_mergesort(int a[], int l, int r){
	// i表示每次merge的数组大小，i取1，2，4，8...
	// j表示每次merge的数组最左边（即第一个元素）的下标 
	int i, j; 
	int tot = r - l + 1;
	// i最多可以取到tot-1，是因为如果待排序数组的元素个数为奇数，就会出现类似下面的情况：
	// o o o o o
	// (oo) (oo) o
	// (oooo) o
	// (ooooo)
	// 可见i最多能取到tot-1
	// 而个数为偶数的情况下，两边的个数是一致的，i最多取tot/2
	// 而j最大的取值是tot-2，即刚开始按照i=1来merge时，最后一轮的j是最大的
	// 往后随着需要merge的数组大小在不断增加，j只能越变越小 
	for(i = 1; i <= tot - 1; i *= 2){
		for(j = 0; j <= tot - 2; j += 2*i){
			int mid = j + i - 1;
			int re = min(j + 2*i - 1, tot - 1);  // 在偶数的情况下，right end不可能取到tot - 1，奇数的情况下，只能取tot-1 
			merge(a, j, mid, re);
		}
	}
	
}
 
int main(){
	int a[6] = {1, 0, -1, 5, 4, -3};
	int temp[6];
	
	iter_mergesort(a, 0, 5);
	
	for(int i = 0; i < 6; i++)
		cout << a[i] << " ";
	
	return 0;
	
} 

// 下面是Weiss数据结构书上的版本
void MergeSort(int A[],int N){
    int* tmpArray;
    tmpArray=(int*)malloc(sizeof(int)*N);
    if(tmpArray!=NULL){
        Msort(A,tmpArray,0,N-1);
        free(tmpArray);
    }
    else{
        exit(1);
    }
}

void Msort(int A[],int tmpArray[],int left,int right){
    int center;
    if(left<right){
        center=left+(right-left)/2;
        Msort(A,tmpArray,0,center);
        Msort(A,tmpArray,center+1,right);
        Merge(A,tmpArray,left,center+1,right);
    }
}


void Merge(int A[],int tmpArray[],int lpos,int rpos,int rightEnd){
    int leftEnd=rpos-1;
    int totalNum=rightEnd-lpos+1;
    int tmp=lpos;
    while(lpos<=leftEnd&&rpos<=rightEnd){
        if(A[lpos]<=A[rpos])
            tmpArray[tmp++]=A[lpos++];
        else
            tmpArray[tmp++]=A[rpos++];
    }
    // 两个while只有一个会执行
    while(lpos<=leftEnd)
        tmpArray[tmp++]=A[lpos++];
    while(rpos<=rightEnd)
        tmpArray[tmp++]=A[rpos++];
    for(int i=0;i<totalNum;i++,rightEnd--) // 每一层的totalNum都是不一样的，这里只是为了从末尾把没放到A的元素放进去
        A[rightEnd]=tmpArray[rightEnd];
}

///////////////////////////////////////////////////
// 递归的版本，参考维基百科: https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F#C++
void mergesort(vector<int>& arr, vector<int>& reg, int start, int end){
	if(start >= end) return;
	int len = end - start;
	int mid = len/2 + start;
	int start1 = start, end1 = mid;
	int start2 = mid + 1, end2 = end;
	mergesort(arr, reg, start1, end1);
	mergesort(arr, reg, start2, end2);
	int k = start;
	while(start1 <= end1 && start2 <= end2)
		reg[k++] = arr[start1] < arr[start2] ? arr[start1++] : arr[start2++];
	while(start1 <= end1) reg[k++] = arr[start1++];
	while(start2 <= end2) reg[k++] = arr[start2++];
	for(k = start; k <= end; k++) arr[k] = reg[k];
}
