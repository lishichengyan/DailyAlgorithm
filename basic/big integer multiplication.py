# 模拟竖式乘法
# https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
def multiply(self, num1: str, num2: str) -> str:
	# special case
	if num1 == "0" or num2 == "0":
		return "0"

	# general case
	cache = collections.defaultdict(list)
	n1, n2 = len(num1), len(num2)

	# num2 should be shorter
	if n2 > n1:
		num1, num2 = num2, num1

	# multiply digit by digit and cache the intermediate results
	slot_no = 0
	for i in num2[::-1]:
		carry_mul = 0
		pos = slot_no
		for j in num1[::-1]:
			cur_prod = int(i) * int(j) + carry_mul
			carry_mul, cur_digit = divmod(cur_prod, 10)
			cache[pos].append(cur_digit)
			pos += 1
		if carry_mul:
			cache[pos].append(carry_mul)
		slot_no += 1

	# add numbers in the cache
	carry_add = 0
	res = ""
	for key in cache:
		cur_sum = sum(cache[key]) + carry_add
		carry_add, cur_rem = divmod(cur_sum, 10)
		res = str(cur_rem) + res
	return str(carry_add) + res if carry_add else res
 
 # see https://en.wikipedia.org/wiki/Multiplication_algorithm
 
