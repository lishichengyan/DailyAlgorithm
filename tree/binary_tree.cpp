#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

// 二叉树的定义 
struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 辅助函数，分割字符串 
vector<string> split(string& str, string& delim){
	vector<string> res;
	if(str == "") return res;
	
	char* pch = new char[str.length() + 1];
	strcpy(pch, str.c_str());
	
	char* pdelim = new char[delim.length() + 1];
	strcpy(pdelim, delim.c_str());
	
	char* ptok = strtok(pch, pdelim);
	while(ptok){
		string tmp = ptok;
		res.push_back(tmp);
		ptok = strtok(NULL, pdelim);
	}
	
	return res;
}
 
// 层序遍历 
void levelOrder(TreeNode* root){
	if(root == NULL) {
		return;
	}
	queue<TreeNode*> q;	
	q.push(root);
	while(!q.empty()){
		TreeNode* tmp = q.front();
		q.pop();
		cout << tmp->val << " ";
		if(tmp->left){
			q.push(tmp->left);
		}
		if(tmp->right){
			q.push(tmp->right);
		}
	}
}

// 前序遍历，递归版本 
void preOrder(TreeNode* root){
	if(root == NULL) {
		return;
	}	
	cout << root->val << " ";
	preOrder(root->left);
	preOrder(root->right);
}

//中序遍历，递归版本 
void inOrder(TreeNode* root){
	if(root == NULL) {
		return;
	}
	inOrder(root->left);
	cout << root->val << " ";
	inOrder(root->right);
}

//后序遍历，递归版本 
void postOrder(TreeNode* root){
	if(root == NULL) {
		return;
	}
	postOrder(root->left);
	postOrder(root->right);
	cout << root->val << " ";		
}

// 从中序遍历得到的序列构建二叉树 
TreeNode* buildTree(vector<string>& seq){
	/* 
	* para: a level-order sequence, including NULL 
	* return: the root of the binary tree
	*
	* eg: 0, 1, 2, NULL, 4, NULL, NULL
	*       0 
	*		/ \
	*     1  2
	*     \
	*     4
	*/
	
	queue<TreeNode*> q;
	
	if(seq.empty()) return NULL;
	TreeNode* root = new TreeNode(stoi(seq[0]));
	
	int i = 1;
	q.push(root);
	while(!q.empty() && i < seq.size()){
		TreeNode* cur = q.front();
		q.pop();
		
		// construct left subtree
		if(seq[i] != "NULL" && cur->left == NULL){
			TreeNode* tmp = new TreeNode(stoi(seq[i]));
			cur->left = tmp;
			q.push(tmp);  // enqueue new node
			i++;  // move to next node 
		}else{
			i++; 
		} 
		
		// construct right subtree, similar logic
		if(seq[i] != "NULL" && cur->right == NULL){
			TreeNode* tmp = new TreeNode(stoi(seq[i]));
			cur->right = tmp;
			q.push(tmp);
			i++;		
		}else{
			i++;
		}	
	}
	return root;
}

int main(){
	string seq = "0,1,2,NULL,4,NULL,NULL";
	string delim = ",";
	vector<string> strSeq = split(seq, delim);
	
	
	TreeNode* root = buildTree(strSeq);
	return 0;
} 
