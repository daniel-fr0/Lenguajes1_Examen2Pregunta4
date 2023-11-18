def f36tail(n, acc=list(range(18))):
	if n < 18:
		return acc[n]
	else:
		return f36tail(n - 1, acc[1:] + [acc[0] + acc[6] + acc[12]])
	


if __name__ == "__main__":
	for i in range(72):
		print(f36tail(i), end = "\t")
		if (i+1) % 6 == 0:
			print()