import time
from malebaby import male_dictionary
from femalebaby import female_dictionary
from famousmale import famous_males
from famousmale import famous_females

print("Project \"Codecademy\" python Baby names\n")
time.sleep(5)
print("List with over 2000 baby names to choose from , lists from\n https://www.verywellfamily.com/top-1000-baby-girl-names-2757832\n")
time.sleep(5)
print("Credits Schloz Jr,Carlos")

#input("Is your baby male or female ?\nIf you don't know type unknown \n" )
#input("Type the first letters of the name to see the names \nOr type all to see the whole list\n")
#input("If you wanna you can type famous and see the most famous names from both sex\nIf no you can type exit to leave the program\n")

def famous_male():
 counter = 0 
 temp = []
 res = dict()
 for key, val in famous_males.items():
    counter = 0  
    if val not in temp and counter <= 15:
     temp.append(val)
     res = val
     counter += 1
     print(str(res))  
def famous_female():
       
  counter_2 = 15 
  temp = []
  res = dict()
  for key, val in famous_females.items():
    if val not in temp:
        temp.append(val)
        res = val
    print(str(res))

time.sleep(8)

def find_baby():
 baby = input("Is your baby male or female ?\nIf you don't know type unknown \n").upper()
 if baby == "MALE":
   boy = input("Type the first letters of the name to see the names \nOr type all to see the whole list\n").upper()
   for key, val in male_dictionary.items():
    if boy in val.upper() and boy[0] == val[0]:   
      print("[{0}] - {1}".format(key, val))
    elif boy == "ALL":                    
      print("[{0}] - {1}".format(key, val))
        
   fmale = input("If you wanna you can type famous and see the most famous names for male sex\nIf not you can type exit to leave the program\nOr type any key to try again \n").upper()
   if fmale == "FAMOUS":
    famous_male()
    time.sleep(18)
   elif fmale == "EXIT":
    time.sleep(5) 
    quit() 
   else:
    print("try again")  
    find_baby() 
 elif baby == "FEMALE":
     girl = input("Type the first letters of the name to see the names \nOr type all to see the whole list\n").upper()
     for key, val in female_dictionary.items():
      if girl in val.upper() and girl[0] == val[0]:
       print("[{0}] - {1}".format(key, val))
      elif girl == "ALL":                    
       print("[{0}] - {1}".format(key, val))
     female = input("If you wanna you can type famous and see the most famous names for female sex\nIf not you can type exit to leave the program\nOr type any key to try again \n").upper()
     if female == "FAMOUS":
      famous_female()
      time.sleep(18)
     elif female == "EXIT":
       time.sleep(5) 
       quit() 
     else:
      print("try again")  
      find_baby()    
 elif baby == "UNKNOWN":    
     both = input("Type the first letters of the name to see the names \nOr type all to see the whole list\n").upper()
     for key, val in male_dictionary.items() :
      if both in val.upper() and both[0] == val[0]:
       print("[{0}] - {1}".format(key, val))
      elif both == "ALL":
        print("[{0}] - {1}".format(key, val)) 
     for key, val in female_dictionary.items() :
      if both in val.upper() and both[0] == val[0]:
       print("[{0}] - {1}".format(key, val))  
      elif both == "ALL":
       print("[{0}] - {1}".format(key, val))
     emale = input("If you wanna you can type famous and see the most famous names from both sex\nIf not you can type exit to leave the program\nOr type any key to try again \n").upper()
     if emale == "FAMOUS":
      famous_female()
      famous_male()
      time.sleep(18)
     elif emale == "EXIT":
      time.sleep(5) 
      quit() 
     else:
      print("try again")  
      find_baby() 
 else:
   print("Wrong answer try again")
   find_baby()  

find_baby()