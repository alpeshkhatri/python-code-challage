def __replace_3_5(n):
    ret = n
    if n % 3 == 0 :
        ret = 'Fizz'
    if n % 5 == 0:
        ret = 'Buzz'
    if n % (3 * 5) == 0 :
        ret = 'FizzBuzz'
    return ret

def fizz_buzz(n):
    return [__replace_3_5(i) for i in range(1,n+1)]

def is_fizz_buzz(sequence):
    print(fizz_buzz(len(sequence)+1))
    return sequence == fizz_buzz(len(sequence))

is_fizz_buzz([1, 2, "Fizz", 4])
