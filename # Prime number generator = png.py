# Prime number generator = png

def prime_number_generator(limit):                              # This function returns a list of prime numbers between 1 and limit
    is_prime = [True] * (limit +1)                              # is_prime is a list of booleans with length limit + 1
    is_prime[0] = is_prime[1] = False                           # 0 and 1 are not prime numbers

    for i in range(2, int(limit ** 0.5) +1):                    # This loop will check if any number in the list is a prime number
        if is_prime[i]:                                         # If the number is prime, then it will check if any number in the range of i*i to limit is a prime number
            for j in range(i*i, limit +1, i):                   # This loop will check if any number in the range of i*i to limit is a prime number
                is_prime[j] = False                             # If the number is not prime, then it will set the value of is_prime[j] to False

    primes = [i for i in range(2, limit +1) if is_prime[i]]     # This list will contain all the prime numbers between 1 and limit
    return primes                                               # This function will return the list of prime numbers between 1 and limit

pn = int(input("Enter a number: "))

if pn >= 2:
    prime_numbers = prime_number_generator(pn)
    print(f"The prime numbers between 1 and {pn} are: {prime_numbers}")
else:
    print("Please enter a number greater than or equal to 2")