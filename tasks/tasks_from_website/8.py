# является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково
# читаются слева направо и справа налево

# 1)
def is_palindrome(string):
    return string == ''.join(reversed(string))

print(is_palindrome('abba'))

# 2)
def is_palindrome2(string):
    return string == string[::-1]

print(is_palindrome2('abba'))