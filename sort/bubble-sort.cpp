void bubble_sort(int a[],int n){  
    int i,j,tmp;  
    for(i=0;i<n-1;i++){//n个元素需要排序n-1趟  
        for(j=0;j<n-i-1;j++){//每做一次外循环就有i+1个元素归位（注意i从0开始，所以是i+1）,那么就只需要排剩下的n-i-1个  
            if(a[j]>a[j+1]){  
                tmp=a[j+1];  
                a[j+1]=a[j];  
                a[j]=tmp;  
            }  
        }  
    }  
}  
