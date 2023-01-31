word_list=['우영우','기러기','별똥별','파이썬']
def is_palindrome(word_list) :
    palindrome_list = []
    for word in word_list:
        if word == word[::-1]:
            palindrome_list.append(word)
    return palindrome_list
print(is_palindrome(word_list))
        