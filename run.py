from math import *
import time
import os
import sys
import random


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def banner():
    clr()
    logo = """
       \033[93m_________    __   __________ \033[94m  ______
      \033[93m/ ____/   |  / /  / ____/  _/ \033[94m /_  __/
     \033[93m/ /   / /| | / /  / /    / ____\033[94m__/ /
    \033[93m/ /___/ ___ |/ /__/ /____/ /____\033[94m_/ /
    \033[93m\____/_/  |_/_____\____/___/    \033[94m/_/
     \033[93m                           \033[94mV1.3
     By Yash And Yuvi....
    """
    print(logo)

def entree():
    print("\nWelcome To Calci Terminal...")
    print("\tLets Start Calculating")


def exeet():
    print("\nThanks For Using Calci Terminal..")
    print("\tWe Hope To See You Again")
    exit()

def max_reach():
    clr()
    banner()
    print("Maximum Attempts Tried\nPlease Restart The Program To Continue")
    input("Press Enter To Exit...")
    exeet()

def cal_anime():
    asd = 1,0.2,1.3,1.5,0.7,0.5,0.9,0.6,1.1
    lst1 = 1,2,3,4,5,6,7,8,9,10,11
    lst2 = 12,13,14,15,16,17,18,19,20,21,22
    lst3 = 23,24,25,26,27,28,29,30,31,32,33
    lst4 = 34,35,36,37,38,39,40,41,42,43,44
    lst5 = 45,46,47,48,49,50,51,52,53,54,55
    lst6 = 56,57,58,59,60,61,62,63,64,65,66
    lst7 = 67,68,69,70,71,72,73,74,75,76,77
    lst8 = 78,79,80,81,82,83,84,85,86,87,88
    lst9 = 89,90,91,92,93,94,95,96,97,98,99
    lst0 = 100
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[----------] 0%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[=---------] " + str(random.choice(lst1)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[==--------] " + str(random.choice(lst2)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[===-------] " + str(random.choice(lst3)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[====------] " + str(random.choice(lst4)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[=====-----] " + str(random.choice(lst5)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[======----] " + str(random.choice(lst6)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[=======---] " + str(random.choice(lst7)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[========--] " + str(random.choice(lst8)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[=========-] " + str(random.choice(lst9)) + "%")
    time.sleep(random.choice(asd))
    banner()
    entree()
    print("\n\n\n")
    print("Loading Calci-T Server Please Wait..")
    print("[==========] " + str(lst0) + "%")
    print("Loading Succesful")
    input("Press Enter To Continue")


def calculate():

    cal_anime()
    clr()
    banner()
    entree()
    print()
    print("What You Want To Do..")
    print("1.Addition/Substraction/Multiplication/Division")
    print("2.Square/Cube/Table/Roots And X Raise To Y \n3.Exit")

    qwer = 1
    while True and qwer <=3:
        try:
            po = input("Enter your Choice: ")
            if po == '1':
                i = 1
                while True and i <= 3:
                    try:
                        print("1.Addition(+)        2.Substraction(-)")
                        print("3.Multiplication(*)  4.Division(/)")
                        OP = input("Enter Operator: ")

                        if OP == "+" or OP == "Add" or OP == "add" or OP == '1':
                            num1 = float(input("Enter A Number: "))
                            num2 = float(input("Enter Second number: " + str(num1) + " + "))
                            result = num1 + num2
                            print(str(num1) + " + " + str(num2) + " = " + str(result))
                            i += i
                            input("Press Enter To Exit...")
                            exeet()


                        elif OP == "-" or OP == "sub" or OP == "Sub" or OP == '2':
                            num1 = float(input("Enter A Number: "))
                            num2 = float(input("Enter Second number: " + str(num1) + " - "))
                            result = num1 - num2
                            print(str(num1) + " - " + str(num2) + " = " + str(result))
                            i += i
                            input("Press Enter To Exit...")
                            exeet()

                        elif OP == "*" or OP == "mul" or OP == "Mul" or OP == '3':
                            num1 = float(input("Enter A Number: "))
                            num2 = float(input("Enter Second number: " + str(num1) + " X "))
                            result = num1 * num2
                            print(str(num1) + " X " + str(num2) + " = " + str(result))
                            i += i
                            input("Press Enter To Exit...")
                            exeet()

                        elif OP == "/" or OP == "div" or OP == "Div" or OP == '4':
                            try:
                                num1 = float(input("Enter A Number: "))
                                num2 = float(input("Enter Second number: " + str(num1) + " / "))
                                result = num1 / num2
                                print(str(num1) + " / " + str(num2) + " = " + str(result))
                                i += i
                                input("Press Enter To Exit...")
                                exeet()
                            except ZeroDivisionError:
                                print("You Cant Divide any Number By Zero...")
                                continue


                        else:
                            print("Inavlid Operator...")
                            i += i
                            continue
                    except KeyboardInterrupt:
                        print("We Received A Cancel Request\n\tCtrl+C Was Pressed...\nExitting The Terminal")
                        banner()
                        exeet()
                    except ValueError:
                        print("Warning !!!\nA Value-Error Detected\nYou Have Entered A Wrong Value")
                        print('Try Again')
                        i += i
                        continue

                max_reach()

            elif po == "2":
                i = 1
                while True and i <= 3:
                    try:
                        calcu = """
                        1.Square A Number.
                        2.Find Square Root.
                        3.Cube A Number.
                        4.Find Cube Root.
                        5.Check Perfect Cube.
                        6.Write Table.
                        7.Raise To
                        8.Exit
                        """
                        print(calcu)
                        zx = input("Enter Your Choice: ")
                        asx = 1
                        while True and asx <= 3:
                            if zx == "1":
                                a = 1
                                while True and a <= 3:
                                    try:
                                        def square(num):
                                            return num * num

                                        x = float(input("Enter The Number You Want To Square: "))
                                        result = square(x)
                                        print("The Square of " + str(x) + " is " + str(result))
                                        a += a
                                        input("Press Enter To Exit...")
                                        exeet()
                                    except ValueError:
                                        print("Invalid Entry")
                                        a += a
                                        continue
                                max_reach()

                            elif zx == "2":
                                b = 1
                                while True and b <= 3 :
                                    try:
                                        N1 = float(input("Enter the number to find its square root: "))
                                        result = sqrt(N1)
                                        print("The Square Root Of " + str(N1) + " Is " + str(result))
                                        b += b
                                        input("Press Enter To Exit...")
                                        exeet()
                                    except ValueError:
                                        print("Invalid Entry\nCan't Find Root of negative Numbers")
                                        b += b
                                        continue
                                max_reach()

                            elif zx == "3":
                                a = 1
                                while True and a <= 3:
                                    try:
                                        def find_cube(num):
                                            return num * num * num

                                        x = float(input("Enter The Number You Want To Cube: "))
                                        result = find_cube(x)
                                        print("The Cube Of " + str(x) + " Is " + str(result))
                                        input("Press Enter To Exit...")
                                        exeet()
                                    except ValueError:
                                        print("Invalid Entry")
                                        continue
                                max_reach()

                            elif zx == "4":
                                a = 1
                                while True and a <= 3:
                                    try:
                                        x = int(input("Enter the number to find its cube root: "))
                                        if x > 0:
                                            ans = x ** (1 / 3)

                                        else:
                                            ans = -((-x) ** (1 / 3))
                                        print('Cube root of ' + str(x) + ' is ' + str(ans))
                                        input("Press Enter To Exit...")
                                        exeet()
                                    except ValueError:
                                        print("Invalid Entry")
                                        continue
                                max_reach()

                            elif zx == "5":
                                a = 1
                                while True and a <= 3:
                                    try:
                                        def is_perfect_cube(x):
                                            x = abs(x)
                                            return int(round(x ** (1 / 3))) ** 3 == x

                                        x = float(input("Enter The Number: "))

                                        if is_perfect_cube(x) is True:
                                            print(str(x) + " is a perfect Cube.")
                                            input("Press Enter To Exit...")
                                            exeet()
                                        else:
                                            print(str(x) + " is not a perfect Cube.")
                                            input("Press Enter To Exit...")
                                            exeet()
                                    except ValueError:
                                        print("Invalid Entry..")
                                        continue
                                max_reach()

                            elif zx == "6":
                                a = 1
                                while True and a <= 3:
                                    try:
                                        qwas = int(input('Who\'s Table You Want To Write: '))
                                        zxc = int(input("How Many Times You Want To Write: "))
                                        qaz = 1
                                        while (qaz <= zxc):
                                            print(qwas, 'x', qaz, '=', qwas * qaz)
                                            qaz += 1
                                        input("Press Enter To Exit...")
                                        exeet()
                                    except ValueError:
                                        print("Invalid Entry..")
                                        continue
                                max_reach()

                            elif zx == "7":
                                a = 1
                                while True and a <= 3:
                                    try:
                                        bs = int(input('Enter Base Number: '))
                                        idx = int(input('Enter Index Number: ' + str(bs) + " raise to "))
                                        print('The Answer is: ' + str(bs ** idx))
                                        input("Press Enter To Exit")
                                        exeet()
                                    except ValueError:
                                        print("Invalid Entry..")
                                        continue
                                max_reach()

                            elif zx == "8":
                                clr()
                                banner()
                                exeet()

                            else:
                                print("Invalid Input...\nPlease Select numbers between 1-8")
                                asx += asx
                                continue

                    except KeyboardInterrupt:
                        print("We Received A Cancel Request\n\tCtrl+C Was Pressed...\nExitting The Terminal")
                        exeet()
                        
                    except ValueError:
                        print("Warning !!!\nA Value-Error Detected\nYou Have Entered A Wrong Value")
                        print('Try Again')
                        continue
                max_reach()

            elif po == "3" :
                clr()
                banner()
                exeet()

            else:
                print("Inavlid Input...")
                qwer +=  qwer
                continue

            max_reach()
        except TypeError:
            print("An Typing Error Has Occured\nPlease Check What You Entered")
            input("Press Enter To Continue...")
            continue
            
        except KeyboardInterrupt:
            print("We Received A Cancel Request\n\tCtrl+C Was Pressed...\nExitting The Terminal")
            exeet()
            
        except ValueError:
            print("Warning !!!\nA Value-Error Detected\nYou Have Entered A Wrong Value")
            print('Try Again')
            i += i
            continue
            
        except ZeroDivisionError:
            print("You Cant Divide any Number By Zero...")
            continue
            
    max_reach()

calculate()
