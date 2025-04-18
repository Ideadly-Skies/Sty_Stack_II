def reverse_some_chars(s, chars):
    # transform chars to dict keys 
    char_dict = dict.fromkeys(chars, "") 

    # append target to stack 
    stack = [] 
    for char in s:
        # O(1) lookup for target string
        if char in char_dict:
            stack.append(char)

    # reverse string
    reverse_str = ""
    for char in s:
        # O(1) lookup for target string
        if char in char_dict:
            reverse_str += stack.pop()
        else:
            reverse_str += char
    
    # reverse_str order 
    return reverse_str 

if __name__ == "__main__":
    print(reverse_some_chars("computer", ["a", "e", "i", "o", "u"])) # -> 'cemputor'