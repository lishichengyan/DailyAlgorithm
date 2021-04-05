void selection_sort(int a[],int n){  
    int i,j,min;  
    for(i=0;i<n;i++){  
        min=i;//假设当前元素是最小的，min记录它的下标  
        for(j=i+1;j<n;j++){  
            if(a[j]<a[min])  
                min=j;  
        }  
        if(min!=i)//如果这个元素本身就是最小的，就不要交换了  
            swap(a[i],a[min]);  
    }  
}  
