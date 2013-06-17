__author__ = 'will'
import random


def primes(n):

    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = range(3, n+1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]


def rand_prime():

    nprimes = random.randint(10, 1000)
    found_primes = primes(nprimes)
    return random.choice(found_primes)


def safe_reveal(encoded_answer, choice):

    doors = set([1, 2, 3])
    answer = decode_answer(encoded_answer)
    doors.discard(answer)
    try:
        doors.discard(choice)
    except KeyError:
        pass

    return random.choice(list(doors))


def encode_answer(correct):

    return correct*rand_prime()


def decode_answer(secret):

    if (secret % 3) == 0:
        return 3
    elif (secret % 2) == 0:
        return 2
    else:
        return 1