# a = 3
# b = 6

# def fab(n):
# 	if 0 <= n < a*b:
# 		return n
# 	else:
# 		return sum(fab(n - b*i) for i in range(1, a+1))

def f36(n):
	if 0 <= n < 18:
		return n
	else:
		return f36(n - 6) + f36(n - 12) + f36(n - 18)
	


if __name__ == "__main__":
	for i in range(72):
		print(f36(i), end = "\t")
		if (i+1) % 6 == 0:
			print()