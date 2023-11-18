def f36iter(n):
	acc = list(range(18)) # Mismo acumulador que f36tail
	
	# La condicion negada del caso base de f36tail
	while n >= 18:
		# Actualiza el acumulador igual que f36tail
		acc = acc[1:] + [acc[0] + acc[6] + acc[12]]

		# Decrementa n al igual que f36tail
		n -= 1

	# Retorna lo mismo que el caso base de f36tail
	return acc[n]



if __name__ == "__main__":
	for i in range(72):
		print(f36iter(i), end = "\t")
		if (i+1) % 6 == 0:
			print()