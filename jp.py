import requests as rs
import pyautogui as pg
import time as t

file_list = [
    'AddTwoMatrix.java',
    'AddTwoNumbers.java',
    'ArithmeticException_Demo.java',
    'ArrayIndexOutOfBound_Demo.java',
    'calc.java',
    'Calculator.java',
    'callbyref.java',
    'CopyConstructor.java',
    'Daughter.java',
    'DefaultConstructor.java',
    'ExArraySort.java',
    'ExceptionDemo.java',
    'ExceptionDemo2.java',
    #'fact.class',
    'fact.java',
    'fibo.java',
    'Finally.java',
    'JavaExample.java',
    #'links.py',
    #'links.txt',
    'Main.java',
    'MyClient.java',
    'MyServer.java',
    'Odd_Even.java',
    'Recursion.java',
    #'res.py',
    #'script.py',
    #'script1.py',
    'string.java',
    'Student.java',
    'Sum.java',
    'SumOfNNumbers.java',
    'TestInheritance.java',
    'TestInheritance2.java',
    'TestInheritance3.java',
    'Threadexample.java'
]

#file = open("links.txt")

#for i in file:
#    file_list.append(i.strip())

#print(file_list)
c = 'y'
while c.lower() == 'y':        
    #print(file_list)
    for index, file in enumerate(file_list):
        print(f"{index} {file}")

    file_index = int(input("Enter the number to read the file: "))
    
    file_ = file_list[file_index]
    url = 'https://rockleaks.netlify.app/jp/' + file_
    res = rs.get(url)
    
    file_content = res.content.decode('utf-8')
    print(file_content)    

    c1 = input("Do you want to write this content in other file? (Y/N): ")
    if c1 == 'y':
        pg.hotkey('win', 'r')
        pg.write("notepad")
        pg.press("enter")
        t.sleep(1)
        pg.write(file_content, interval = 0.0025)
    c = input("Do you want to try again? (Y/N): ")

#file.close()