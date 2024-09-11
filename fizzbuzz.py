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

def main():
    print(fizzbuzz(15))
main()