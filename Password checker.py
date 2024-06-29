import re
password=input("Enter your password:")
print("\n")
length=len(password)

special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
lowercase=0;uppercase=0;num=0;spl=0
for char in password:
    if(char.islower()):
        lowercase+=1
    elif(char.isupper()):
        uppercase+=1
    elif(char.isdigit()):
        num+=1 
    else:
      spl+=1  

if(length>=8 and lowercase>0 and uppercase>0 and num>0 and spl>0):

    print("Strong Password !!")
elif(length>=8 and (lowercase>0 or uppercase>0) and (num>0 or spl>0)):

    print("Moderate Password !!")

elif(length>=8 and (lowercase>0 or uppercase>0 or num>0 or  spl>0)):

    print("Weak Password !!")

else:
    print("Invalid password.Password didn't meet the necessary requirements.")    

print("\nPassword strength identified successfully\n")    