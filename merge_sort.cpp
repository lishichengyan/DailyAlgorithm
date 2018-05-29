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
