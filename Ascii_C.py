#!/data/data/com.termux/files/usr/bin/python3
#Author prince kumar
# Date 25 dec
# Simple text to ascii converyter
#import all requirements..
import pyfiglet
import os
#Define some color-----------------
r = "\033[31;1m"
g = "\033[32;1m"
y = "\033[33;1m"
p = "\033[35;1m"
w = "\033[0;1m"
#let's make  a banner dor this tool--------------------
def banner():
    os.system('clear')
    print(g)
    print(""" 

   _   _   _   _   _   _   _  {} |
 {} / \ / \ / \ / \ / \ / \ / \ {} |
 {}( a | s | c | i | i | _ | c ) {}| Made by prince
  {}\_/ \_/ \_/ \_/ \_/ \_/ \_/  {}|

  {} Youtube https://m.youtube.com/c/Princeweb


    """.format(r, g, r, g, r, g, r, p))
banner()
#Make a Lists of Fonts-------------------------------
print()
print("""{}[{}01{}]{}  Default      {}[{}11{}]{}  Dotmatrix""".format(y, w, y, p, y, w, y, p))
print("""{}[{}02{}]{}  Slant        {}[{}12{}]{}  Bubble""".format(y, w, y, p, y, w, y, p))
print("""{}[{}03{}]{}  3-D          {}[{}13{}]{}  Bulbhead""".format(y, w, y, p, y, w, y, p))
print("""{}[{}04{}]{}  3×5          {}[{}14{}]{}  Digital""".format(y, w, y, p, y, w, y, p))
print("""{}[{}05{}]{}  5lineoblique""".format(y, w, y, p))
print("""{}[{}06{}]{}  Alphabet""".format(y, w, y, p))
print("""{}[{}07{}]{}  Doh""".format(y, w, y, p))
print("""{}[{}08{}]{}  letters""".format(y, w, y, p))
print("""{}[{}09{}]{}  Isometric1""".format(y, w, y, p))
print("""{}[{}10{}]{}  Alligaror""".format(y, w, y, p))
print()
print("{} Choose any font:\r ".format(r))
optn =int(input())


#Handle font requests------------------------------
if optn == 1:
    print()
    text = input("Enter a text to show: ")
    print()
    res = pyfiglet.figlet_format(text)
    print("{} {}".format(g, res))  
elif optn == 2:
    print()        
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "slant" )     
    print("{} {}".format(g, res))
elif optn == 3:
    print()
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "3-d" )
    print("{} {}".format(g, res))
elif optn == 4:
    print()
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "3x5" )
    print("{} {}".format(g, res))
elif optn == 5:
    print()
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "5lineoblique" )
    print("{} {}".format(g, res))
elif optn == 6:
    print()
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "alphabet" )                  
    print("{} {}".format(g, res))
elif optn == 7:
    print()
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "doh" )            
    print("{} {}".format(g, res))
elif optn == 8:
    text = input("Enter a text to show: ")
    print()
    res = pyfiglet.figlet_format(text, font = "latter" )                                                     
    print("{} {}".format(g, res))
elif optn == 9:
    print()
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "isometric1" )
    print("{} {}".format(g, res))
elif optn == 10:
    print()
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "alligator" )  
    print("{} {}".format(g, res))
elif optn == 11:
    print()            
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "dotmatrix" )                                         
    print("{} {}".format(g, res))
elif optn == 12:
    print()            
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "bubble" )         
    print("{} {}".format(g, res))
elif optn == 13:
    print()           
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "bulbhead" )                                                        
    print("{} {}".format(g, res))
elif optn == 14:
    print()       
    text = input("Enter a text to show: ")
    res = pyfiglet.figlet_format(text, font = "digital" )                                                      
    print("{} {}".format(g, res))
elif optn == 15:
    print()
    youtube = "https://m.youtube.com/c/Princeweb"
    ins = "https://instagram.com/sirprincekrvert"
    print("""   {}i am prince kumar i a junior mechanical engineer  
    {} Youtube {} {}
    Instagram {}
    """.format(w, g, youtube,  y, ins))
else:
    print()
    print("{}[{}!{}]{} Invalid option..".format(w, r, w, y))
