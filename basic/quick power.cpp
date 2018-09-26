// 这样干在leetcode上会超时
// 原因出在n上，需要把n转换成无符号数，否则可能出现移位后变成0xFFFF之类的情况，陷入死循环
class Solution {
public:
    const double precision = 0.0000000000000001f;
    
    bool isEqual(const double x, const double y){
        return (abs(x - y) <= precision);
    }
    
    double myPow(double x, int n) {
        bool reverse = false;
        if(isEqual(x, 0)) return 0.0f;
        if(isEqual(x, 1.0f) || n == 0) return 1.0f;
        if(n < 0) {
            n = -n;
            reverse = true;
        }
        double res = 1.0f, base = x;
        while(n){
            if(n & 1)
                res *= base;
            base *= base;
            n >>= 1;
        }
        return res;
    }
};
