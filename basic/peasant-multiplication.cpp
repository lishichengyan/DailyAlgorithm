#include<iostream>
using namespace std;

/*
* the basic idea:
* let's take 13 * 19 for example, 19 = 10011 (in its binary form)
* therefore 13 * 19 = 13 * 10011 = 13 * (1*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0)
* from the equation we can see only when the bit is 1 will we actually do multiplication
*
*/
int peasantMultiplication(int a, int b){
	int prod = 0;
	while(b){
		if(b & 1){ // if b is odd
			prod += a;
		}
		b >>= 1; // b = floor(b/2)
		a <<= 1; // a = a+a
	}
	return prod;
} 

int main(){
	cout<<peasantMultiplication(233,2); // 466
	return 0;
}
