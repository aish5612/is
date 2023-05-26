def operation(s):
    ans_xor =""
    ans_and = ""
    for char in s:
        char_and = chr(ord(char) & 127)
        char_xor = chr(ord(char) ^ 127)

        ans_xor += char_xor
        ans_and += char_and

    print(ans_xor)
    print(ans_and)

operation("hello world")
