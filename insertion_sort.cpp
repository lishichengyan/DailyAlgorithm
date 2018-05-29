void InsertionSort(int A[],const int size)
{
    int i,j;
    int tmp;
    for(i=1;i<size;i++)
    {
        tmp=A[i];
        j=i;
        while(j>0&&tmp<A[j-1])
        {
            A[j]=A[j-1];
            j--;
        }
        A[j]=tmp;
    }
}

