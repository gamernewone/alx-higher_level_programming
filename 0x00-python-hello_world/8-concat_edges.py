#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.index("object"):(str.index("programming") + 11)] + str[(str.index('with') - 1):(str.index('with') + 5)] +  str[:6]
print(str)
