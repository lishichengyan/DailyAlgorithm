void shell_sort(int a[],int n){  
    int i,j,increment;  
    int tmp;  
    for(increment=n/2;increment>0;increment/=2){  
        for(i=increment;i<n;i++){//内部其实是选择排序（Insertion Sort）  
            tmp=a[i];  
            for(j=i;j>=increment;j-=increment){  
                if(tmp<a[j-increment])  
                    a[j]=a[j-increment];  
                else  
                    break;  
            }  
            a[j]=tmp;  
        }  
    }  
}  
