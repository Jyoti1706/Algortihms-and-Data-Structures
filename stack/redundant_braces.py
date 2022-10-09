class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
		stack = []
		for d in A:
			if d != ")":
				stack.append(d)
			else:
				count = 0
				while stack[-1] != "(":
					popped = stack.pop()
					if popped in "*+-/":
						count += 1
				stack.pop()
				if count == 0:
					return 1
		return 0

data = "(b+(a+b))"
sol = Solution()
print(sol.braces(data))