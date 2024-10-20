# Python3 Program to find the 
# Greatest Common divisor
# of two number which is 
# in given range


# Return the greatest common 
# divisor of two numbers
def gcd(a, b):
	if(b == 0):
		return a;
	return gcd(b, a % b);

# Return the greatest common 
# divisor of a and b which
# lie in the given range.
def maxDivisorRange(a, b, l, h):
	g = gcd(a, b);
	res = -1;
	# Loop from 1 to
	# sqrt(GCD(a, b).
	i = l;
	while(i * i <= g and i <= h):
		# if i divides the GCD(a, b),
		# then find maximum of three
		# numbers res, i and g/i
		if(g % i == 0):
			res = max(res,max(i, g/i));
		i+=1;
	return int(res);

# Driver Code
if __name__ == "__main__":
	a = 3; 
	b = 27; 
	l = 1; 
	h = 5;

	print(maxDivisorRange(a, b, l, h));

# This code is contributed by mits
