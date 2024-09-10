function fizzbuzz(num = 0) {
    if((num < 0) || (num > Math.pow(10, 4))) {
        throw RangeError;
    }
    let fizz_list = [];
    
    for (i = 1; i <= num; i++)
    if((i % 3 == 0) && (i % 5 == 0)) {
        fizz_list.push("fizzbuzz");
    } else if(i % 3 == 0) {
        fizz_list.push("fizz");
    } else if(i % 5 == 0) {
        fizz_list.push("buzz");
    } else if((i % 3 != 0) && (i % 5 != 0))  {
        fizz_list.push(i.toString());
    }

    return fizz_list;
}

function test_fizzbuzz(num = 0) {
    try {
        console.log("The result is [" + fizzbuzz(num).join(", ") + "]");
    } catch (error) {
        console.error("Invalid Number");
    }
        
}

function main() {
    // expect [1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz]
    test_fizzbuzz(15);

    // expect error catch
    test_fizzbuzz(-1);

    // expect error catch
    test_fizzbuzz(Math.pow(10, 20));
}

main()
