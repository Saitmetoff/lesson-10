"""1"""

"""2"""

"""3"""

def find_smallest_and_largest(L, R, N):
    smallest = max(L, R)
    largest = min(L, R)
    while (largest + smallest) % N != 0:
        largest += 1
        smallest -= 1
    return smallest, largest

print(find_smallest_and_largest(1, 20, 5))
print(find_smallest_and_largest(100, 200, 10))


"""4"""

def remove_every_third(nums):
    result = []
    for i, num in enumerate(nums):
        if (i + 1) % 3 != 0:
            result.append(num)
    return result[::-1]

print(remove_every_third([10, 20, 30, 40, 50, 60, 70, 80, 90]))

"""5"""

def find_indices(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

numbers = [2, 7, 11, 15]
target = 9
print(find_indices(numbers, target))


"""6"""

def longest_unique_substring(s):
    start = max_length = 0
    used_chars = {}

    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_chars[char] = i

    return max_length

print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbbb"))
print(longest_unique_substring("pwwkew"))


"""7"""

def remove_every_third(nums):
    result = []
    while len(nums) >= 3:
        nums.pop(2)
    result.extend(nums)
    return result

print(remove_every_third([10, 20, 30, 40, 50, 60, 70, 80, 90]))



"""8"""

def generate_parentheses(n):
    def backtrack(S='', left=0, right=0):
        if len(S) == 2 * n:
            result.append(S)
            return
        if left < n:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)

    result = []
    backtrack()
    return result

print(generate_parentheses(3))
print(generate_parentheses(1))


"""9"""

def letter_combinations(digits):
    if not digits:
        return []

    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(combination, next_digits):
        if not next_digits:
            result.append(combination)
        else:
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    result = []
    backtrack('', digits)
    return result

print(letter_combinations("23"))


"""10"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test
print(gcd(12, 8))


"""11"""

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

print(gcd_recursive(12, 8))



"""12"""
def pal(num):
    return str(num) == str(num)[::-1]

# Test
print(pal(121))
print(pal(223))
