// 暴力地计算vector的幂集
void computePowerSet(vector<int> input, vector<vector<int>>& powerSet){
	int len = input.size();
	long long setSize = pow(2, len);
	for(long long i=0; i<setSize; i++){
		vector<int> subSet;
		for(long long j=0; j<len; j++){
			if(i & (1<<j)){
				subSet.emplace_back(input[j]);
			}
		}
		powerSet.emplace_back(subSet);
	}
	// for debug purpose
	/*
	for(auto subSet : powerSet){
		for(auto elem : subSet){
			cout << elem << " ";
		}
		cout<<endl;
	}*/
} 
