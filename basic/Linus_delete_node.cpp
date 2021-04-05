// how to delete a node in a linked list?
// Linus provided an interesting way
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
 };

ListNode* initList(vector<int> nums){
	ListNode* dummy = new ListNode(INT_MAX);
	ListNode* p, *q = dummy;
	for(auto num : nums){
		p = new ListNode(num);
		q->next = p;
		q = p;
	}
	return dummy->next;
}


bool cond(ListNode* p){
	return (p->val > 2);	
}

void remove_if(ListNode** p, bool (*pf)(ListNode*)){
	for(ListNode** cur = p; *cur; ){
		ListNode* entry = *cur;
		if(pf(entry)){
			*cur = entry->next;
			free(entry);
		}else{
			cur = &entry->next;
		}
	}
}

int main(){
	vector<int> nums{1, 2, 3, 4, 5};
	ListNode* head = initList(nums);
	
	remove_if(&head, cond);
	
	for(auto p = head; p != NULL; p = p->next) 
		cout << p->val << " ";
	cout << endl;
	
	return 0;
}
