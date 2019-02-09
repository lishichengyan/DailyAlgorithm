class UnionFind{
	// 我们规定：用数组来表示森林
	// -1表示每棵树最初的父节点，-1也可以表示当前树的高度 
	// 数字0 - N表示每个节点的编号
	// 写的时候不要犯迷糊，disjSet_[root]是这个root的父亲，如果是unionByHeight还可以理解成求树高 
public:
	UnionFind(int size){
		size_ = size;
		disjSet_.resize(size_);
		for(auto elem : disjSet_) elem = -1;
	}
	
	// key operations
	// 简单的union，把root2连到root1上 
	void simpleUnion(int root1, int root2){
		disjSet_[root2] = root1;  // 把root2的爸爸设置成root1 
	}
	
	// 按height来union，矮的union到高的上 
	void unionByHeight(int root1, int root2){
		if(disjSet_[root2] < disjSet_[root1]){  // 注意树高是负数，此时root2更高 
			disjSet_[root1] = root2;  // 让root2成为新的root 
		}else{
			if(disjSet_[root1] == disjSet_[root2]){  // 一样高 
				disjSet_[root1]--;  // 树高加1 
			}
			disjSet_[root2] = root1; 
		} 
	} 
	
	// find返回x所在的树的标识，其实就是树根的第一个儿子 
	int find(int x){
		if(disjSet_[x] < 0){
			return x;
		}
		else{
			return find(disjSet_[x]);	
		}
	} 
	
	// 带路径压缩的find 
	int findWithPathCompression(int x){
		if(disjSet_[x] < 0){
			return x;
		}
		else{
			disjSet_[x] = findWithPathCompression(disjSet_[x]);	
		}
	} 

public:
	int size_;
	vector<int> disjSet_;  // 里面放爸爸，注意disjSet_[0]没用，因为我们用0来表示最开始的爸爸 
};
