a1=[1, 5, 8, 9, 10];
a2=[5, 8, 9, 10, 12, 20, 40, 60, 70];
num=int(input("enter the number to check:"));#input the number to check
a3=0
a4=0
if num in a1:#check if num in a1
    a3=1
if num in a2:#check if num in a2
        a4=1
        if a3==a4:# num in a1 and a2 print if no then skip
            print("number", str(num) + "found in both array")
elif num in a1:# ii num in a1 print
    print("number",str(num)+"found in array_one")
elif num in a2:#if number in a2 print
    print("number",str(num)+ "found in array_two",)








