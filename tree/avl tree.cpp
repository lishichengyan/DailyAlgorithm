#include <iostream>
#include <algorithm>

using namespace std;

struct TreeNode{
	int val;
	TreeNode* left;
	TreeNode* right;
	int height;
	TreeNode(int x): val(x), left(NULL), right(NULL), height(0){}
};

int getHeight(TreeNode* p){
	if(p == NULL){
		return -1;
	}
	return p->height;
} 

TreeNode* singleRotateWithLeft(TreeNode* k2){
	TreeNode* k1 = k2->left;
	k2->left = k1->right;
	k1->right = k2;
	// 注意调整高度的先后顺序 
	k2->height = max(getHeight(k2->left), getHeight(k2->right)) + 1;
	k1->height = max(getHeight(k1->left), k2->height) + 1;
	return k1;
}

TreeNode* singleRotateWithRight(TreeNode* k2){
	TreeNode* k1 = k2->right;
	k2->right = k1->left;
	k1->left = k2;
	k2->height = max(getHeight(k2->left), getHeight(k2->right)) + 1;
	k1->height = max(getHeight(k1->left), k2->height) + 1;
	return k1;	
}

TreeNode* doubleRotateWithLeft(TreeNode* k3){
	k3->left = singleRotateWithRight(k3->left);
	return singleRotateWithLeft(k3); 
}

TreeNode* doubleRotateWithRight(TreeNode* k3){
	k3->right = singleRotateWithLeft(k3->right);
	return singleRotateWithRight(k3);
}

TreeNode* insert(int x, TreeNode* p){
	if(!p){
		p = new TreeNode(x);
	}else if(x < p->val){
		p->left = insert(x, p->left);
		if(getHeight(p->left) - getHeight(p->right) == 2){
			if(x < p->left->val){
				p = singleRotateWithLeft(p);
			}else{
				p = doubleRotateWithLeft(p);
			}
		}
	}else if(x > p->val){
		p->right = insert(x, p->right);
		if(getHeight(p->right) - getHeight(p->left) == 2){
			if(x > p->right->val){
				p = singleRotateWithRight(p);
			}else{
				p = doubleRotateWithRight(p);
			}
		}
	}else{
		// x already in the tree, we do nothing
	}
	p->height = max(getHeight(p->left), getHeight(p->right)) + 1;
	return p;
}

void pre(TreeNode* root){
	if(!root) return;
	cout << root->val << " ";
	pre(root->left);
	pre(root->right);
}

int main(){
	// TreeNode* root = insert(3, root) 不对 
	TreeNode* root = NULL;  // 一定要先赋值为NULL 
	root = insert(3, root);  // 再调用 
	root = insert(2, root);
	root = insert(1, root);
	root = insert(4, root);
	root = insert(5, root);
	root = insert(6, root);
	pre(root);
	return 0;	
} 
