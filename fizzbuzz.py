


def fizzbuzz(num = 0):
    fizz_list = []

    if num < 0 or num > pow(10, 4):
        raise ValueError('invalid number')
    
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_list.append('FizzBuzz')
        elif i % 3 == 0:
            fizz_list.append('Fizz')
        elif i % 5 == 0:
            fizz_list.append('Buzz')
        elif i % 3 != 0 and i % 5 != 0:
            fizz_list.append(str(i))
    return fizz_list

# quick function to test fizzbuzz
def test_fizzbuzz(num = 0):
    try:
        print(fizzbuzz(num))
    except ValueError as e:
        print({e})    
    

def main():
    # expect [1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz]
    test_fizzbuzz(15)

    # expect caught ValueError
    test_fizzbuzz(-1)

    # expect caught ValueError
    test_fizzbuzz(pow(10, 16))


main()