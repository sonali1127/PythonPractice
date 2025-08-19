a="Sonali                           "
upper=a.upper()
lower=a.lower()
strip=a.rstrip(" ")#strips the trailing characters at the last
replace=a.replace("Sonali","sonali")
split=a.split(" ")#makes  string as a list
capitalize=a.capitalize()#makes upper letter capitalized
center=a.center(50) #makes the string center
count = a.count("s") #counts all the occurence
end=a.endswith("i")
start=a.startswith("s")
find = a.find("s")#finds the occurence of first value if not it gives -1
#It is similar to the find, the index() but we are finding should be mandately(compulsory) present
# otherwise it throws an error
throw= a.index("s")
alnum=a.isalnum()# all should should aplha or numeric but not any symbols
alpha = a.isalpha() #if all numbers be letters/alphabets
al=a.islower()
print = a.isprintable()#prints true if all can be printed otherwise false(/n,/t..)
space =a.isspace()
titl=a.istitle()
swap=a.swapcase()
a=a.title()# makes capital of all first letter in word
