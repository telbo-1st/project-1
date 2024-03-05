#problem1
"""
introduction
#With the help of this Python script, users may easily convert numerical data between several #bases, such as Decimal, Binary, Octal, and Hexadecimal.
It functions as a flexible Numbering System Converter.The application handles different numeral systems with meticulous attention to detail by using a set
of functions that are specifically designed for each conversion. A menu system organizes the user interface and directs users.
#by choosing the bases for the input and output. 
This converter offers a simple way to convert numbers between binary and hexadecimal systems, regardless of whether you're working with common decimal numbers or delving deeper into their nuances. For individuals looking to investigate or incorporate similar conversion functions in their applications, the code is easily comprehensible due to its thoughtful commenting.

"""
def decimal_to_binary():
    decimal_num = int(input("enter decimal number"))
    binary_num = ""
    while decimal_num > 0:
        result = decimal_num % 2
        binary_num = str(result)+binary_num
        decimal_num = decimal_num//2
    print("Your binary number is ", binary_num)
# decimal to octal function
def decimal_to_octal ():
    decimal_number = int(input("enter decimal number"))
    octal_number = ""
    while decimal_number > 0:
        result = decimal_number % 8
        octal_number = str(result) + octal_number
        decimal_number = decimal_number//8
    print("Your octal number is ", octal_number)
#decimal to hexa function:
def decimal_to_hexadecimal():
    decimal_number=int(input("enter decimal number"))
    hexa_number=""
    while decimal_number>0:
      result=decimal_number%16
      if result==10 :
        result="A"
      elif result==11:
        result="B"
      elif result==12:
        result="C"
      elif result==13:
        result="D"
      elif result==14:
        result="E"
      elif result==15:
        result="F"
      elif result==16:
        result="G"
      else:
        result=result

      hexa_number=str(result)+hexa_number
      decimal_number=decimal_number//16
    print( "Your hexadecimal number " , hexa_number)
#octal to decimal function
def octal_to_decimal():
     octal_number=int(input("enter octal number"))
     power=0
     decimal_number=0
     while octal_number>0:
        res= octal_number%10
        decimal_number=decimal_number+res*(8**power)
        octal_number=octal_number//10
        power=power+1
     print("Your decimal number is " , decimal_number)

#octaal to hexa
def octal_to_hexa():
     octal_number=int(input("enter octal number"))
     power=0
     decimal_number=0
     while octal_number>0:
        res= octal_number%10
        decimal_number=decimal_number+res*(8**power)
        octal_number=octal_number//10
        power=power+1
     deci =decimal_number
     hexa_nomber=""
     while deci>0:
      result=deci%16
      if result==10 :
        result="A"
      elif result==11:
        result="B"
      elif result==12:
        result="C"
      elif result==13:
        result="D"
      elif result==14:
        result="E"
      elif result==15:
        result="F"
      elif result==16:
        result="G"
      else:
        result=result

      hexa_nomber=str(result)+hexa_nomber
      deci=deci//16
     print("Your hexadecimal number is ",hexa_nomber)
#octal to binary function:
def octal_to_binary():
    octal_number=int(input("enter octal number"))
    power=0
    decimal_number=0
    while octal_number>0:
        res= octal_number%10
        decimal_number=decimal_number+res*(8**power)
        octal_number=octal_number//10
        power=power+1
    deci=decimal_number
    binary_number = ""
    while deci> 0:
        result = deci % 2
        binary_number = str(result)+binary_number
        deci = deci//2
    print( "Your binary number is ",binary_number)
#binary to hexa function:
def binary_to_hexa():
     binary_number=int(input("enter binary number"))
     power=0
     decimal_number=0
     while binary_number>0:
        res= binary_number%10
        decimal_number=decimal_number+res*(2**power)
        binary_number=binary_number//10
        power=power+1
     deci=decimal_number
     hexa_number=""
     while deci>0:
      result=deci%16
      if result==10 :
        result="A"
      elif result==11:
        result="B"
      elif result==12:
        result="C"
      elif result==13:
        result="D"
      elif result==14:
        result="E"
      elif result==15:
        result="F"
      elif result==16:
        result="G"
      else:
        result=result

      hexa_number=str(result)+hexa_number
      deci=deci//16
     print("your hexa deciamal number is ",hexa_number)
#binary to octal function
def binary_to_octal():
    base = 2
    binary =list(input("Enter your binary number: "))
    length = len(binary)
    #number refer to decimal number
    number = 0
    #power means the weight or the power of the base
    power = 0
    for digit in reversed(binary):
        number += int(digit) * (base ** power)
        power += 1
    decimal_number=number
    octal_number = ""
    while decimal_number > 0:
        result = decimal_number % 8
        octal_number = str(result) + octal_number
        decimal_number = decimal_number//8
    print("Your octal number is ", octal_number)
#binary to decimal function
def binary_to_decimal():
    base = 2
    binary =list(input("Enter your binary number: "))
    length = len(binary)
    #number refer to decimal number
    number = 0
    #power means the weight or the power of the base
    power = 0
    for digit in reversed(binary):
        number += int(digit) * (base ** power)
        power += 1
    print( "your decimal number is ",number)
#hexa to octal
def hexadecimal_to_octal():
    base = 16
    hexa = list(input("Enter your hexadecimal number: "))
    # number refer to decimal number
    number = 0
    letter = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    for digit in hexa:
        if digit in letter:
            number = number * base + letter[digit]
        else:
            number = number * base + int(digit)
    decimal_number = number
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number = decimal_number//8
    print("the octal number: ", octal_number)
#hexa to binary function
def hexa_to_binary():
    base = 16
    hexa = list(input("Enter your hexadecimal number: "))
    #number refer to decimal number
    number = 0
    letter = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for digit in hexa:
        if digit in letter:
            number = number * base + letter[digit]
        else:
            number = number * base + int(digit)

    decimal = number
    binary=""
    while(decimal > 0):
        result = decimal%2
        binary=str(result)+binary
        decimal = decimal//2
    print("your binary number: ", binary)
#hexa to decimal function
def hexa_to_decimal():
    base = 16
    hexa = list(input("Enter your hexadecimal number: "))
    # number refer to decimal number
    number = 0
    letter = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for digit in hexa:
        if digit in letter:
            number = number * base + letter[digit]
        else:
            number = number * base + int(digit)
    print("your decimal number is ", number)
def menu1():
    print("Enter [A] if you want to insert a new number")
    print("Enter [B] if you want to exite")

print("**Welcome to numbering system converter**")
menu1()
choice = input("Please choose A OR B")
while choice !="B":
    if choice=="A" or choice== "a":

        print("1) DECIMAL")
        print("2) BINARY")
        print("3) OCTAL")
        print("4) HEXADECIMAL")
        choice1= input("Please choose the num system you want to convert from ")
        print("======================================")
        if choice1=="1":
            print("Please choose the numbering system you want to convert to")
            print("1) BINARY")
            print("2) OCTAL")
            print("3) HEXADECIMAL")
            choice1in1 = input("Please choose from 1-3")
            if choice1in1=="1":
                decimal_to_binary()
            elif choice1in1=="2":
                decimal_to_octal()
            elif choice1in1 == "3":
                decimal_to_hexadecimal()
        elif choice1=="2":
            print("Please choose the numbering system you want to convert to")
            print("1)DECIMAL")
            print("2)OCTAL")
            print("3)HEXADECIMAL")
            choice2in1=input("please choose from 1-3")
            if choice2in1=="1":
                binary_to_decimal()
            elif choice2in1=="2":
                binary_to_octal()
            elif choice2in1=="3":
                binary_to_hexa()
        elif choice1=="3":
            print("please choose the numbering system you want to convert to ")
            print("1)BINARY")
            print("2)HEXA")
            print("3)DECIMAL")
            choice3in1=input("please choose from 1-3")
            if choice3in1=="1":
                octal_to_binary()
            elif choice3in1=="2":
                octal_to_hexa()
            elif choice3in1=="3":
                octal_to_decimal()
        elif choice1=="4":
            print("please choose the numbering system u want to convert to")
            print("1)Decimal ")
            print("2) binary")
            print("3)Octal")
            choice4in1=input("please choose from 1-3")
            if choice4in1=="1":
                hexa_to_decimal()
            elif choice4in1=="2":
                hexa_to_binary()
            elif choice4in1=="3":
                hexadecimal_to_octal()
                print("===========================")
    else:
        print("please selesct a valid choice")
    menu1()
    choice=input("please choose [A] or [B]")
print("thank you")
