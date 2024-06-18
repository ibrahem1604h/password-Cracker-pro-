import string
import random
leters=[]
numer=[]
sumply=[] 
time_try=0
name=input("Enter your password: ")

for x in name:
   if (x not in string.punctuation) and (x not in string.digits) :
      leters.append(x)
   elif (x not in string.ascii_letters) and (x not in 
      string.punctuation) :
      numer.append(x)
   elif (x not in string.ascii_letters) and (x not in string.digits) :
      sumply.append(x)

x=len(leters)
y=len(numer)
z=len(sumply)

lete=int(x)
numbers= int(y)
symbols= int(z)

while True:
   char= random.choices(string.ascii_letters, k=lete)
   num= random.choices(string.digits, k=numbers)
   sym= random.choices(string.punctuation, k=symbols)
      
   password= char + num + sym
   random.shuffle(password)
   passwords="".join(password)

   time_try+=1
   
   if passwords == name:
      print(password)
      print(f"The generated password matches the input password! {time_try}")
      break
