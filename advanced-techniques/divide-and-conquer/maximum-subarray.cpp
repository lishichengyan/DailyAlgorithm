class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len=nums.size();
        if(len==0)
        {
            return 0;
        }
        else
        {
            return find_max_subarr(nums,0,len-1);
        }
    }
    
    int find_max_subarr(vector<int>& nums,int low,int high)
    {
        // base case
        if(low==high)
        {
            return nums[low];
        }
        else
        {
            int mid=(low+high)/2;
            int max_left=find_max_subarr(nums,low,mid);
            int max_right=find_max_subarr(nums,mid+1,high);
            int max_cross=find_max_cross(nums,low,mid,high);
            return max(max(max_left,max_right),max_cross);
        }
    }
    
    int find_max_cross(vector<int>& nums,int low,int mid,int high)
    {
        
        int max_left=INT_MIN;
        int max_right=INT_MIN;
        int sum=0;
        for(int i=mid;i>=low;i--)
        {
            sum+=nums[i];
            if(sum>max_left)
            {
                max_left=sum;
            }
        }
        sum=0;
        for(int j=mid+1;j<=high;j++)
        {
            sum+=nums[j];
            if(sum>max_right)
            {
                max_right=sum;
            }
        }
        return max_left+max_right;
    }
};
