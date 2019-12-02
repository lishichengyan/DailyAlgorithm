# 渐进式分析记号
## Big-O
If there exists positive constants c and n0, such that when N>n0, f(N) <= cg(N), then f(x) = O(g(x)).
## Big-Omega
If there exists positive constants c and n0, such that when N>n0, f(N) >= cg(N), then f(x) = Ω(g(x)).
## Big-Theta
If f(x) = O(g(x)) and f(x) = Ω(g(x)), then f(x) = Θ(g(x))
## Small-O
If f(x) = O(g(x)) and f(x) != Ω(g(x)), then f(x) = o(g(x))
## Small-Omega
If f(x) = Ω(g(x)) and f(x) != Ω(g(x)), then f(x) = ω(g(x))
