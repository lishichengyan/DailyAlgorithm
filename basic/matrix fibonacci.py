# 矩阵 + 快速幂
def mul_mat(F, M):
    x =  F[0][0]*M[0][0] + F[0][1]*M[1][0] 
    y =  F[0][0]*M[0][1] + F[0][1]*M[1][1] 
    z =  F[1][0]*M[0][0] + F[1][1]*M[1][0] 
    w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]
    
    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w

def fast_exp(n):
    res = [[1,1],[1,0]]
    fib_mat = [[1,1],[1,0]]
    while n:
        if n&1:
            mul_mat(res, fib_mat)
        mul_mat(fib_mat, fib_mat)
        n >>= 1
    return res

def fib4(n):
    """
    --              --    --   --
    |F_(n+1)  F_(n)  |    |1   1|^(n)
    |                | =  |     |
    |F_(n)    F_(n-1)|    |1   0|
    --              --    --   --
    """
    res = fast_exp(n)
    return res[0][1]
