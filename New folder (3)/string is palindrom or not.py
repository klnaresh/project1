# to chech whether string is palindrome

original_name=input('enter the original name:')
changed =(original_name[::-1])
if original_name == changed:
    print("entered name is palindrom")
else:
    print("entered name is not palindrom")
