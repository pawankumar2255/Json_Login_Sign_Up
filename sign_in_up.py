import json
print("sign_in and sign_up page")
print("""1.  sign_up,
        2.sign_in""")
in_or_up = int(input(""" If you have account already .   enter   1. 
                    otherwise .  enter   2
                    """))
if in_or_up == 1:
    list_s = ["username","password"]
    dict = {}
    dict0 = {}
    for chs in list_s:
        if chs == "username":
            for d in range(3):
                rd = input("enter " + chs + ":   ")
                if rd[-10:] != "@gmail.com":
                    if d ==2:
                        print("you crossed the limit")
                        break
                    elif d!=2:
                        continue
                else:
                    dict[chs] = rd
                    break
            continue
        if chs == "password":
            for l in range(3):
                rd = input("enter " + chs + ":   ")
                if len(rd)>=6 and len(rd)<=12:
                    if  ( "A" in rd or "B" in rd or "C" in rd or "D" in rd or "E" in rd or "F" in rd or "G"in rd or "H" in rd or "I" in rd or "J" in rd or "K" in rd or "L" in rd or "M" in rd or "N" in rd or "O" in rd or "P" in rd or "Q" in rd or "R" in rd or "S" in rd or "T" in rd or "U" in rd or "V" in rd or "W" in rd or "X" in rd or "Y" in rd or "Z" in rd ) and ("a" in rd or "b" in rd or "c" in rd or "d" in rd or "e" in rd or "f" in rd or "g" in rd or "h" in rd or "i" in rd or "j" in rd or "k" in rd or "l" in rd or "m" in rd or "n" in rd or "o" in rd or "p" in rd or "q" in rd or "r" in rd or "s" in rd or "t" in rd or "u" in rd or "v" in rd or "w" in rd or "x" in rd or "y" in rd or "z" in rd ) and ("0" in rd or "1" in rd or "2" in rd or "3" in rd or "4" in rd or "5" in rd or "6" in rd or "7" in rd or "8" in rd or "9" in rd) and ("@" in rd or "#" in rd or "$" in rd or "&" in rd):
                        break
                else:
                    if l==2:
                        print("you are crossed the limit")
                    continue
        dict[chs] = rd
        dict0["username"]=dict
        with open("sign_detail.json","w") as file:
            json.dump(dict0,file,indent=4)
    with open("sign_detail.json") as file:
        f=json.load(file)
    f["username"]=dict
    with open("sign_detail.json","r+") as file:
        json.dump(f,file,indent=4)
    print("you accont is created successfully")
elif in_or_up == 2:
    with open("sign_detail.json") as file:
        f = json.load(file)
        for tur in range(5):
            u_or_e=input("enter username :    ")
            pas = input("enter your password  :   ")
                
            if u_or_e == f["username"]["username"] and pas == f["username"]["password"]:
                print("you are signed in successfully")
                break
            else:
                print("incorrect password  please re  enter yuour details")
                continue
        else:
            print("you are crossed the limit of entering correct details please try after some time")