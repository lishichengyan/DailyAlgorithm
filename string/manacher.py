# 647. Palindromic Substrings
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = '#' + '#'.join(s) + '#'
        pos = 0  # 目前最长回文的对称轴
        mr = 0  # 目前最长回文的右边界
        total = len(ss)
        rl = [0]*total
        # ml = 0
        for i, elem in enumerate(ss):
            if i < mr:
                rl[i] = min(rl[2*pos - i], mr-i)
            else:
                rl[i] = 1
            # 开始从i向两边扩展
            while i - rl[i] >= 0 and i + rl[i] < total and ss[i - rl[i]] == ss[ i + rl[i]]:
                rl[i] += 1
            # 更新mr和pos
            if rl[i] + i - 1 > mr:
                mr = rl[i] + i - 1
                pos = i
            # ml = max(ml, rl[i])  # 找最长的回文，最后要减1
        print(rl)
        for i in range(total):
            rl[i] -= 1
        return sum((v+1)/2 for v in rl)  # 计算字串有多少回文
