def gcd(a,b):
	if a == 0:
		return b
	return gcd(b%a,a)
a = int(input())
b = int(input())
print(gcd(a,b))