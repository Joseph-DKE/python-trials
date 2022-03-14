def largest_prime_factor(n):
    i = 2
    while i < n**(1/2):
        if n % i ==0:
            n = n/i
        else:
            i +=1
    print(n)
largest_prime_factor(600851475143)