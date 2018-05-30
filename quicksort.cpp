#define Cutoff 3  
int Median3(int A[],int Left,int Right);  
void Qsort(int A[],int Left,int Right);  
  
void  Quicksort(int A[],int N){  
    Qsort( A, 0, N - 1 );   
    /*A:the array*/  
    /*0:Left index*/  
    /*N-1:Right index*/  
}  
  
int Median3(int A[],int Left,int Right){   
    int Center=(Left+Right)/2;  
    if(A[Left]>A[Center])  
        swap(A[Left],A[Center]);   
    if(A[Left]>A[Right])  
        swap(A[Left],A[Right]);  
    if(A[Center]>A[Right])  
        swap(A[Center],A[Right]);   
    /* Invariant: A[ Left ] <= A[ Center ] <= A[ Right ] */   
    swap(A[Center],A[Right-1]); /* Hide pivot */   
    /* only need to sort A[ Left + 1 ] … A[ Right – 2 ] */  
    return A[Right-1];/* Return pivot */   
}  
  
void Qsort(int A[],int Left,int Right){     
    int i,j;   
    int Pivot;  
    if(Left+Cutoff<=Right){/* if the sequence is not too short */  
        Pivot=Median3(A,Left,Right);/* select pivot */  
        i=Left;       
        j=Right-1;/* why not set Left+1 and Right-2? */  
        for(;;){   
            while(A[++i]<Pivot){}/* scan from left */  
            while(A[--j]>Pivot){}/* scan from right */  
            if(i<j)  
                swap(A[i],A[j]);/* adjust partition */  
            else  
                break;/* partition done */  
            }  
        swap(A[i],A[Right-1]);/* restore pivot */   
        Qsort(A,Left,i-1);/* recursively sort left part */  
        Qsort(A,i+1,Right);/* recursively sort right part */  
    }  /* end if - the sequence is long */  
    else /* do an insertion sort on the short subarray */   
        insertion_sort(A+Left,Right-Left+1);  
}
