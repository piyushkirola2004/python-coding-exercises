class AllPrograms:

    #1 Prime Check
    def _prime_checker(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_checker(self):
        try:
            num = int(input("Enter the number : "))
            if self._prime_checker(num):
                print(f"{num} is a prime number")
            else:
                print(f"{num} is not a prime number")
        except ValueError:
            print("Please Enter a valid integer")

    #2 Reverse String
    def _reverse_string_1(self, string):
        reverse = ""
        for i in string:
            reverse = i + reverse
        return reverse

    def reverse(self):
        try:
            string = input("Enter any string : ")
            if string.isalpha():
                reversed_str = self._reverse_string_1(string)
                print(f"The reverse of {string} is : {reversed_str}")
            else:
                print(f"Please enter the string!")
                
        except Exception as e:
            print(e)

    #3 Palindrome Check
    def _reverse_string_2(self, string):
        reverse = ""
        for i in string:
            reverse = i + reverse
        return reverse

    def palindrome(self):
        try:
            string = input("Enter any string : ")
            if string.isalpha():
                reversed_str = self._reverse_string_2(string)
                print(f"The reverse of {string} is : {reversed_str}")
                
                if reversed_str == string:
                    print("This string is Palindrome")
                else:
                    print("This is not a palindrome")
            else:
                print(f"Please enter the string!")
                
        except Exception as e:
            print(e)

    #4 Factorial
    def _factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self._factorial(n - 1)

    def factorial(self):
        try:
            num = int(input("Enter any number :"))
            fact = self._factorial(num)
            
            print(f"The Factorial of {num} is : {fact}")
            
        except ValueError as ve:
            print(ve)
            
        except Exception as e:
            print(f"Error: {e}")

    #5 Second Largest Number
    def _second_largest_number(self, numbers):
        if numbers[0] > numbers[1]:
            largest = numbers[0]
            second_largest = numbers[1]
        
        else:
            largest = numbers[1]
            second_largest = numbers[0]
        
        for i in range(2, len(numbers)):
            if numbers[i] > largest:
                second_largest = largest
                largest = numbers[i]
            elif numbers[i] > second_largest and numbers[i] != largest:
                second_largest = numbers[i]
        
        print("The list is:", numbers)
        print("The second largest element is:", second_largest)

    def second_largest_number(self):
        try:
            num = [12, 45, 7, 89, 23, 67, 90, 34]
            self._second_largest_number(num)
            
        except Exception as e:
            print(e)

    #6 Anagram Check
    def _anagram_check(self, str1, str2):
        if sorted(str1) == sorted(str2):
            print("They are Anagram")
        else:
            print("They are not Anagram")

    def anagram(self):
        try:
            str1 = input("Enter First string :")
            str2 = input("Enter Second string :")
            self._anagram_check(str1, str2)
            
        except Exception as e:
            print(e)

    #7 Count Vowels
    def _count_vowels(self, string):
        count = 0
    
        for i in string:
            if i in "aeiouAEIOU":
                count += 1
        print(f"The Total vowels count in {string} is : {count}")

    def count_vowels(self):
        try:
            string = input("Enter any string :")
            self._count_vowels(string)
        
        except Exception as e:
            print(e)

    #8 Sum of Digits
    def _sum_digits(self, num):
        if num < 0:
            raise ValueError("Negative numbers are not allowed")
        
        total = 0
        while num > 0:
            digit = num % 10
            total += digit
            num //= 10 
    
        print(f"The sum of digits is : {total}")

    def sum_digits(self):
        try:
            num = int(input("Enter a number :"))
            self._sum_digits(num)
            
        except Exception as e:
            print(e)

    #9 Fibonacci Sequence
    def _fibonacci_sequence(self, n):
        if n < 0:
            raise ValueError("The value cannot be negative")
        elif n == 0:
            print("No items to display")
            return
        else:
            print(f"The Fibonacci sequence up to {n}th term is:")
            a, b = 0, 1
            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b

    def fibonacci_sequence(self):
        try:
            term = int(input("Enter the term up to which Fibonacci Sequences display : "))
            self._fibonacci_sequence(term)
            
        except Exception as e:
            print(e)

    #10 Remove Duplicates from a list
    def _remove_duplicate(self, number):
        unique = []
        for i in number:
            if i not in unique:
                unique.append(i)
        print("List without Duplicates are :", unique)
    
    def remove_duplicate(self):
        try:
            num = list(map(int, input("Enter the number in list are :").split()))
            self._remove_duplicate(num)
            
        except Exception as e:
            print(e)

    #11 Check for Leap Year
    def _check_leap_year(self, n):
        if n < 0:
            raise ValueError("The year cannot be Negative")
        if n % 400 == 0:
            print("It is a Leap year")
        elif n % 100 == 0:
            print("It is not a leap year")
        elif n % 4 == 0:
            print("It is a Leap year")
        else:
            print("It is not a leap year")
            
    def check_leap_year(self):
        try:
            year = int(input("Enter the year to check :"))
            self._check_leap_year(year)
            
        except Exception as e:
            print(e)

    #12 Calculate Power without Using ** Operator
    def _power(self, a, b):
        if b < 0:
            raise ValueError("Exponent cannot be negative")
        result = 1
        for i in range(b):
            result *= a
        print(f"{a} to the power of {b} is : {result}")
      
    def power(self):
        try:
            x = int(input("Enter the Value of x :"))
            y = int(input("Enter the Value of y :"))
            self._power(x,y)
            
        except Exception as e:
            print(e)

    #13 Generate List of Even Numbers
    def _even_numbers(self, n):
        even_num = []
        if n < 0:
            raise ValueError("The value of n cannot be negative")
        if n > 0:
            for i in range(1,n + 1):
                if i % 2 == 0:
                    even_num.append(i)
            print(f"The list containing even up to {n} number is : {even_num}")
            
    def even_numbers(self):
        try:
            num = int(input("Enter the value of num :"))
            self._even_numbers(num)
            
        except Exception as e:
                print(e)

    #14 Reverse Words in a Sentence
    def _reverse_words(self, s):
        words = s.split()
        reverse_sentence = words[::-1]
        return " ".join(reverse_sentence)

    def reverse_words(self):
        try:
            sentence = input("Enter the sentence :")
            rev = self._reverse_words(sentence)
            print(f"The reverse order of sentence are : {rev}")
            
        except Exception as e:
            print(e)

    #15 Calculate GCD Using Euclidean Algorithm
    def _gcd_recursive(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Please Input correct numbers")
        if b == 0:
            return a
        else:
            return self._gcd_recursive(b, a % b)

    def _gcd(self, a, b):
        original_a = a
        original_b = b
        
        result = self._gcd_recursive(a, b)
        
        print(f"The GCD of {original_a} and {original_b} is : {result}")
        
    def gcd_recursive(self):
        try:
            num1 = int(input("Enter the First number :"))
            num2 = int(input("Enter the Second number :"))
            
            self._gcd(num1, num2)
            
        except Exception as e:
            print(e)

    #16 Convert Decimal to Binary
    def _decimal_to_binary(self, n):
        if isinstance(n, int):
            binary = bin(n)[2:]
            print(f"The Decimal to Binary is : {binary}")
        else:
            print("Please! Input the Decimal Number")
            
    def decimal_to_binary(self):
        try:
            decimal = int(input("Enter a Decimal Number :"))
            self._decimal_to_binary(decimal)
            
        except Exception as e:
            print(e)

    #17 Factorial Using Recursion
    def _factorial_recursion(self, number):
        if not isinstance(number , int):
            raise ValueError("Input must be Integer Value")

        if number < 0:
            raise ValueError("Factorial is not defined for Negative Numbers")

        if number == 0 or number == 1:
            return 1
    
        return number * self._factorial_recursion(number - 1)

    def factorial_recursion(self):
        try:
            number = int(input("Enter the number :"))
            result = self._factorial_recursion(number)
            print(f"The Factorial of {number} is : {result}")
            
        except Exception as e:
            print(e)

    #18 Find Largest Element in a List Using for Loop
    def _largest_number(self, n):

        largest = n[0]
        
        for i in n:
            if i > largest:
                largest = i

        print(f"The Largest number from the list is {largest}")
    
    def largest_number(self):
        try:
            number = list(map(int ,input("Enter the numbers in list :").split()))
            self._largest_number(number)
            
        except Exception as e:
            print(e)

    #19 Count Occurrences of Each Character in a String
    def _count(self, string):
        if not string:
            raise ValueError("Input cannot be empty")
    
        count_dict = {}
        
        for ch in string:
            if ch.isalpha():
                ch = ch.lower()
                count_dict[ch] = count_dict.get(ch, 0) + 1
            
        print("The Occurrences of each character are")
        print(count_dict)
    
    def count(self):
        try:
            string = input("Enter the string :")
            self._count(string)
            
        except Exception as e:
            print(e)

    #20 Find Intersection of Two Lists without using set operations
    def _intersection_list(self, a, b, list_3):
        for i in a:
            if i in b and i not in list_3:
                list_3.append(i)
    
        print(f"The Intersection of both list are {list_3}")
    
    def intersection_list(self):
        try:
            list_1 = list(map(int, input("Enter the number for intersection :").split()))
            list_2 = list(map(int, input("Enter the number for intersection :").split()))
            list_3 = []
            self._intersection_list(list_1, list_2, list_3)
            
        except Exception as e:
            print(e)

    #21 Remove All Whitespace from a String
    def _remove_whitespace(self, s):
        s1 = s.replace(" ", "")
        s2 = s1.replace("\n", "")
        s3 = s2.replace("\t", "")
        return s3
    
    def whitespace(self):
        try:
            paragraph = input("Enter any paragraph :")
            result = self._remove_whitespace(paragraph)
            print(result)
            
        except Exception as e:
            print(e)

    #22 Calculate Sum of a List of Numbers Using Recursion
    def _sum_list(self, lst):
        if not lst:
            return 0
        return lst[0] + self._sum_list(lst[1:])
    
    def sum_list(self):
        try:
            numbers = list(map(int, input("Enter the numbers in list for sum :").split()))
            total = self._sum_list(numbers)
            print(f"Sum of the list is : {total}")
            
        except Exception as e:
            print(e)

    #23 Find All Prime Numbers up to n
    def _is_prime_numbers(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
          
    def is_prime_numbers(self):
        try:
            num = int(input("Enter the number :"))
            primes = [i for i in range(2, num + 1) if self._is_prime_numbers(i)]
            print(primes)
            
        except Exception as e:
            print(e)

    #24 Merge Two Sorted Lists
    def _merge_sorted_list(self, a, b):
        merge_list = sorted(set(x for lst in (b,a) for x in lst))
        print(merge_list)
    
    def merge_sorted_list(self):
        try:
            list_1 = list(map(int, input("Enter the number in a list_1 :").split()))
            list_2 = list(map(int, input("Enter the number in a list_2 :").split()))
            self._merge_sorted_list(list_1,list_2)
            
        except Exception as e:
            print(e)

    #25 Check if List is Sorted in Ascending Order
    def _sorted_list(self, n):
        for i in range(len(n) - 1):
            if n[i] > n[i+1]:
                print("List is not in Ascending order")
                break
        else:
            print("List is in Asccending order")
    
    def sorted_list(self):
        try:
            lst = list(map(int, input("Enter the number in list :").split()))
            self._sorted_list(lst)
            
        except Exception as e:
            print(e)

    #26 Count Frequency of Each Word in a Text File
    def _frequency_word(self):
        word_count = {}
    
        with open("file.txt", 'r') as f:
            file = f.read().lower().split()
        
        for word in file:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        for word,count in word_count.items():
            print(word, ":", count)
    
    def frequency_word(self):
        try:
            self._frequency_word()
            
        except Exception as e:
            print("Error: The file 'file.txt' was not found.")

    #27 Find Missing Number in Consecutive List
    def _missing_consecutive_num(self):

        list1 = list(map(int, input("Enter the Number in the list :").split()))
        if len(list1) < 2:
            print("List must have at least 2 numbers")
            return
        list1.sort()
        num = int(input("Enter the Number for common difference :"))
    
        print("Missing Number")
        for i in range(len(list1) - 1):
            current = list1[i] + num
            next_num = list1[i + 1]
            while current < next_num:
                print(current, end=" ")
                current += num
        print()
    
    def missing_consecutive_num(self):
        try:
            self._missing_consecutive_num()
            
        except Exception as e:
            print(e)

    #28 Calculate Sum of Squares of First n Natural Numbers
    def _sum_squares(self):
        num = int(input("Enter the number up to :"))
        total = 0
        
        for i in range(1, num + 1):
            square_i = i**2
            total += square_i
            i += 1
        print(f"The Sum of Square up to {num}th is : {total}")
    
    def sum_squares(self):
        try:
            self._sum_squares()
        except Exception as e:
            print(e)

    #29 Reverse Integer
    def _rev_int(self):
        num = int(input("Enter the Number :"))
        rev = 0
        if num < 0:
            sign = -1
        else:
            sign = 1
            
        num = abs(num)
        
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10
            
        rev = rev * sign
        print(f"The Reverse of number is : {rev}")
    
    def rev_int(self):
        try:
            self._rev_int()
        
        except Exception as e:
            print(e)

    #30 Find the Longest Word in a Sentence
    def _longest_word(self):
        input_str = input("Enter the sentence :")

        words = input_str.split()
        
        longest_word = ""
        max_length = 0
        
        for word in words:
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word
        
        print(f"Longest word from the sentence is : {longest_word}")
        
    def longest_word(self):
        try:
            self._longest_word()
            
        except Exception as e:
            print(e)

    #31 Check if a Number is a Power of 2
    def _num_power(self):
        input_num = int(input("Enter the number: "))

        if input_num <= 0:
            print("Number must be positive")
        else:
            num = input_num
            while num > 1:
                if num % 2 != 0:
                    print(f"{input_num} is NOT a power of 2")
                    break
                num = num // 2
            else:
                print(f"{input_num} is a power of 2")
    
    def num_power(self):
        try:
            self._num_power()
            
        except Exception as e:
            print(e)

    #32 Flatten a Nested List
    def _flatten(self, lst):

        result = []
        for i in lst:
            if isinstance(i, list):
                result.extend(self._flatten(i))
            else:
                result.append(i)
        return result
        
    def flatten(self):
        try:
            numbers_list = [1, [2, [3, 4], 5], 6]
            flat_list = self._flatten(numbers_list)
            print(flat_list)
            
        except Exception as e:
            print(e)

    #33 Find Pairs with Given Sum in a List
    def _find_pairs(self, lst, target):
        pairs = []
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] + lst[j] == target:
                    pairs.append((lst[i], lst[j]))
        return pairs

    def find_pairs(self):
        try:
            list_nums = list(map(int, input("Enter the number in a list :").split()))
            target = int(input("Enter the target to achieve the pairs :"))
            result = self._find_pairs(list_nums, target)
            print(f"Pairs with sum {target} are : {result}")
            
        except Exception as e:
            print(e)

    #34 Check if Two Strings are Rotations of Each Other
    def _rotation_checker(self, str1, str2):
    
        if len(str1) != len(str2):
            print("They are not rotation words")
            
        else:
            for i in range(len(str1)):
                rotated = str1[i:] + str1[:i]
                
                if rotated == str2:
                    print("They are rotation words")
                    return
            print("They are not rotation words")
    
    def rotation_checker(self):
        try:
            string1 = input("Enter the Frist String :")
            string2 = input("Enter the Seoond String :")
            self._rotation_checker(string1, string2)
            
        except Exception as e:
            print(e)
            
    #35 Convert List of Tuples to Dictionary
    def _tuple_dict(self, lst):
        output = dict(map(lambda x: (x[0], x[1]), lst))
        print(output)
        
    def tuple_dict(self):
        try:
            lst = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
            self._tuple_dict(lst)
            
        except Exception as e:
            print(e)
    
    #36 Find the Median of a List of Numbers
    def _median(self, numbers):
        numbers.sort()
        
        length = len(numbers)
    
        if length % 2 != 0:
            index = (length + 1) // 2
            print(f"The Median for Odd Numbers is : {numbers[index-1]}")
        
        else:
            median = (numbers[length//2 - 1] + numbers[length//2]) / 2
            print(f"The Median for Even Numbers is : {median}")

    def median(self):
        try:
            numbers = list(map(int, input("Enter numbers separated by space: ").split()))
            self._median(numbers)
            
        except Exception as e:
            print(e)
    
    #37 Sort Dictionary by Value
    def _sorted_dict(self, fruits):
        sorted_fruits = dict(sorted(fruits.items(), key = lambda item: item[1]))
        print(sorted_fruits)
        
    def sorted_dict(self):
        try:
            fruits = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
            self._sorted_dict(fruits)

        except Exception as e:
            print(e)
    
    #38 Generate a List of Prime Numbers Using Sieve of Eratosthenes
    def _list_prime_numbers(self, term):
        if term <= 0:
            raise ValueError("Input Number cannot be zero or negative")

        primes = []
        for num in range(2, term + 1):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)  
        return primes

    def list_prime_numbers(self):
        try:
            term = int(input("Enter the Number term till :"))
            primes = self._list_prime_numbers(term)

            print(f"Prime Numbers till {term} are : {primes}")

        except Exception as e:
            print(e)
            
    #39 Convert Binary to Decimal
    def _binary_to_decimal(self, n):
        if isinstance(n, str) and all(ch in '01' for ch in n):
            decimal = int(n ,2)
            print(f"The Decimal value of {n} is : {decimal}")

        else:
            print("Please! Input the Binary Number (only 0s and 1s)")

    def binary_to_decimal(self):
        try:
            binary = input("Enter a Binary Number :")
            self._binary_to_decimal(binary)

        except Exception as e:
            print(e)

    #40 Check if Subsequence Exists in List
    def _subsequence_list(self, larger_list, smaller_list):
        if all(item in larger_list for item in smaller_list):
            print("True, the input list is in the larger list")

        else:
            print("False, the input list is not in the larger list")

    def subsequence_list(self):
        try:
            larger_list = list(map(int, input("Enter elements of the larger list : ").split()))
            smaller_list = list(map(int, input("Enter elements of the smaller list : ").split()))
            self._subsequence_list(larger_list, smaller_list)

        except Exception as e:
            print(e)

    #41 Find Common Elements in Three Lists
    def _common_elements_list(self, list_1, list_2, list_3):
        for element in list_1:
            if element in list_2 and element in list_3:
                print(f"The Common Element in among three list is : {element}")

    def common_elements_list(self):
        try:
            list_1 = list(map(int, input("Enter elements in the list 1 : ").split()))
            list_2 = list(map(int, input("Enter elements in the list 2 : ").split()))
            list_3 = list(map(int, input("Enter elements in the list 3 : ").split()))
            self._common_elements_list(list_1, list_2, list_3)

        except Exception as e:
            print(e)

    #42 Swap Two Variables Without Temporary Variable
    def _swapping_numbers(self, num_1, num_2):
        if isinstance(num_1, int) and isinstance(num_2, int):
            print("Before Swapping Values are :")
            print(f"Num_1 : {num_1}")
            print(f"Num_2 : {num_2}")
            
            num_1, num_2 = num_2, num_1
            
            print("After Swapping Values are :")
            print(f"Num_1 : {num_1}")
            print(f"Num_2 : {num_2}")
            
        else:
            print("Please! Input the Number")

    def swapping_numbers(self):
        try:
            num_1 = int(input("Enter the number 1 : "))
            num_2 = int(input("Enter the number 2 : "))
            self._swapping_numbers(num_1, num_2)

        except Exception as e:
            print(e)

    #43 Remove Nth Occurrence of a Character from a String
    def _remove_oucuurence(self, string, position, char):
        modify_string = string.split(" ")
        print(f"Before : {modify_string}")
        
        if len(modify_string) >= position:
            word = modify_string[position - 1]
            modify_string[position - 1] = word.removeprefix(char)

        else:
            print("Invalid Position! No such word Exists")
            
        print(f"After : {modify_string}")

    def remove_oucuurence(self):
        try:
            string = input("Enter the string : ")
            position = int(input("Enter the Position to remove character : "))
            char = input("Enter the character to remove : ")
            self._remove_oucuurence(string, position, char)

        except Exception as e:
            print(e)

    #44 Find the First Non-Repeated Character in a String
    def _first_non_repeated_character(self, string):
        if not isinstance(string, str) or not string.isalpha():
            raise ValueError("Input must be an Alphabets, Nothing Else")
            
        for i in range(len(string)):
            letter = string[i]
        
            if letter not in string[:i] and letter not in string[i + 1:]:
                print(f"The First non-repeated character in {string} is : {letter}")
                break
        else:
            print(f"None! There are no non-repeated characters in {string} ")


    def first_non_repeated_character(self):
        try:
            string = input("Enter the string : ")
            self._first_non_repeated_character(string)

        except Exception as e:
            print(e)
            
    #45 Check if String Contains Only Digits
    def _digits_checks(self, string):
        is_number = True
        
        for ch in string:
            if ch not in "0123456789":
                is_number = False
                break
        
        if is_number:
            print("Input String contains Numbers")
            
        else:
            print("Input String does not Contains any Numbers")

    def digits_checks(self):
        try:
            string = input("Enter any string : ")
            self._digits_checks(string)

        except Exception as e:
            print(e)

    #46 Check if Number is Armstrong Number
    def _armstrong_number_check(self, number):
        total = 0

        for i in str(number):
            total += int(i) ** 3

        if total == number:
            print(f"{number} is an Armstrong Number")

        else:
            print(f"{number} is not an Armstromg Number")

    def armstrong_number_check(self):
        try:
            number = int(input("Enter the number to check :"))
            self._armstrong_number_check(number)

        except Exception as e:
            print(e)

    #47 Generate All Subsets of a Set
    def _generate_subsets(self, numbers):
        subsets = [[]]
        
        for num in numbers:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [num])
            subsets.extend(new_subsets)
        print(subsets)

    def generate_subsets(self):
        try:
            numbers = list(map(int, input("Enter the number for a list : ").split()))
            self._generate_subsets(numbers)

        except Exception as e:
            print(e)