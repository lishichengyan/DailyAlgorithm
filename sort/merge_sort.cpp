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
    for(int i=0;i<totalNum;i++,rightEnd--)
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
