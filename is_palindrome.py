def is_palindrome(input_string):
	reverse = ""
	input_string = input_string.lower().replace(" ", "")
	length = len(input_string)
	for i in range(length):
		value = length - i - 1
		reverse = reverse + input_string[value]
	if reverse == input_string:
		return True
	else:
		return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
