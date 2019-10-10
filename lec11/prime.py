def is_prime(num,trace=False):
    found_factor = False
    i = 2
    while i < num:
        if num % i == 0:
            found_factor = True
            if (trace == True):
                print('One of the factor of',num,'is',i,'.')
            break
        i += 1
    return not found_factor


num = int(input('Please input one integer:'))


if is_prime(num,True) == False:
    print(num,'is not a prime.')
else:
    print(num,'is a prime.')

start = int(input('Please give a start interger:'))
end = int(input('Please give a end interger:'))
def find_prime(start,end):
    primes = list(filter(is_prime,list(range(start,end+1))))
    return primes
print(find_prime(start,end))
