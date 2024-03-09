# -*- coding: utf-8 -*-
"""
Turn your user into a L33t H4xor, converting the text entered by the user into "leetspeak".
a -> 4
b -> 8
e -> 3
l -> 1
o -> 0
s -> 5
t -> 7
for example:
Enter some text: I like to eat eggs and spam.
I lik3 70 347 3gg5 4nd 5p4m.
"""
text = input("Enter some text: ")
new_text = text.replace('a','4')
new_text = new_text.replace('b','8')
new_text = new_text.replace('e','3')
new_text = new_text.replace('l','1')
new_text = new_text.replace('o','0')
new_text = new_text.replace('s','5')
new_text = new_text.replace('t','7')
print(new_text)



