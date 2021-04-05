def getNge(arr: List[int]) -> List[int]:
    s = []  # 单调栈
    tot = len(arr)
    nge = [-1] * tot  # 初始时用-1表示没有
    for i in range(tot):
        # 维护一个单调递减栈，找到第一个比栈顶大的元素下标
        while s and arr[s[-1]] < arr[i]:
            cur_idx = arr.pop()
            nge[cur_idx] = i
        s.append(i)
    return nge


def getNle(arr: List[int]) -> List[int]:
    s = []
    tot = len(arr)
    nle = [-1] * tot  # 初始时用-1表示没有
    for i in range(tot):
        while s and arr[s[-1]] > arr[i]:
            cur_idx = arr.pop()
            nle[cur_idx] = i
        s.append(i)
    return nle

def getPle(arr: List[int]) -> List[int]:
    s = []
    tot = len(arr)
    ple = [-1] * tot
    for i in range(0, tot):
        while s and arr[s[-1]] > arr[i]:
            s.pop()
        ple[i] = s[-1] if len(s) != 0 else -1
        s.append(i)
    return ple

def getPge(arr: List[int]) -> List[int]:
    s = []
    tot = len(arr)
    pge = [-1] * tot
    for i in range(0, tot):
        while s and arr[s[-1]] < arr[i]:
            s.pop()
        pge[i] = s[-1] if len(s) != 0 else -1
        s.append(i)
    return pge
