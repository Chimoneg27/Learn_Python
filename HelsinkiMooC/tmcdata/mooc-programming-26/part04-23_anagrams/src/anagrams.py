# Write your solution here
def anagrams(wrd1, wrd2):
   sort1 = sorted(wrd1)
   sort2 = sorted(wrd2)
   if sort1 == sort2:
     return True
   else:
     return False

if __name__ == "__main__":
    print(anagrams("tame", "meta"))
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) 
    print(anagrams("tabby", "batty"))