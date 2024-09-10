class Fizzbuzz:
    def __init__(self, fb_list = None) -> None:
        if fb_list is None:
            fb_list = []
        self.fb_list = fb_list

    def fizzbuzz(self, num = 0):
        if num < 0 or num > pow(10, 4):
            raise ValueError('invalid number')
        for i in range(1, num+1):
            if i % 3 == 0 and i % 5 == 0:
                self.fb_list.append('FizzBuzz')
            elif i % 3 == 0 and i % 5 != 0:
                self.fb_list.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                self.fb_list.append('Buzz')
            elif i % 3 != 0 and i % 5 != 0:
                self.fb_list.append(str(i))
        return self.fb_list
    

def main():

    # simple test of fizzbuzz.fizzbuzz method
    def fizzbuzz_test(item: Fizzbuzz, num = 0):
        try:
            item.fizzbuzz(num)
            print(item.fb_list)
        except ValueError as e:
            print({e})

    item1 = Fizzbuzz()
    item2 = Fizzbuzz()

    # expect no errors
    fizzbuzz_test(item1, 5)

    # expect ValueError caught
    fizzbuzz_test(item1, -1)

    # expect ValueError caught
    fizzbuzz_test(item1, pow(10, 5))

        # expect no errors
    fizzbuzz_test(item2, 9)

    # expect ValueError caught
    fizzbuzz_test(item2, -1)

    # expect ValueError caught
    fizzbuzz_test(item2, pow(10, 5))

main()