str=input()
str=str.strip()
str=str.lower()
str=str.capitalize()
strl=str.split()
str=' '.join(strl)
str = str.replace(" ,", ",").replace(" ;", ";").replace(" :", ":").replace(" .", ".")
print(str)