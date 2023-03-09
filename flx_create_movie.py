import json
import os # so i can clear console.
clear = lambda: os.system('cls') # clears console when clear() is ran.
clear()

def easter_egg():
    i = 1
    while i <= 100:
        print(i * "\nALLEN AKBAR\n************")
        i = i + 1

print("\n**********************\n")
print("NEMFLIX - Movie JSON Writer\n***********\nBy: Nemz, flippN, Pugz, RoffeG, Lz.'²")
print("\n**********************\n\n")
# print("\n----------------------\n")

# start = input("\033[1;35;0mCreate new movie? (Yes/No/help/54):\033[1;36;0m ")
# https://stackoverflow.com/questions/17771287/python-octal-escape-character-033-from-a-dictionary-value-translates-in-a-prin
start = input("Create new movie? (Yes | No | help |54): ")

if start.lower() == "yes" or "y":
    que2 = input("Options: Basic | Advanced: ")
    if que2.lower() == "basic" or "b":
        movCat = input("\nmovie category:\n")
        movNam = input("\nMovie Name:\n")
        movDes = input("\nMovie Description:\n")
        movYea = input("\nMovie Year:\n")
        movTim = input("\nMovie Time:\n")
        movNamTrim = movNam.lower().replace(" ", "_")
        movCatTrim = movCat[0:3].lower()
        # print(movCatTrim)

        infoJson = {
            "movNam": movNam,
            "movDes": movDes,
            "movYea": int(movYea),
            "movTim": movTim,
            "movPth":   "/browse/mov/"+movCatTrim+"/nocat/"+movNamTrim+".html",
            "movImg":   "/pub/covr/"+movCatTrim+"/nocat/"+movNamTrim+".webp",
            "movImgBg": "/pub/covr/"+movCatTrim+"/nocat/"+movNamTrim+"_bg.webp",
            "movVidBg": "/pub/covr/"+movCatTrim+"/nocat/"+movNamTrim+"_vid.webp",
            "movIcoNm": 1,
            "movIcoNw": 1,
            "movIco4k": 0,
            "movIcoCc": 0
        }
        json_obj = json.dumps(infoJson, indent=4)
        with open(movNamTrim+".json", "w") as outfile:
            outfile.write(json_obj) & print("\nNEMFLIX: " + movNamTrim+".json has been created!\n")
        
        # print("\n", infoJson)

    if que2.lower() == "advanced" or "a":
        #mov4k  = input("4k Version: (1 = y, 0 = n)\n")
        print("Coming soon.")
elif start.lower() == "no" or "n":
    print("\nOkay..?\n")
elif start.lower() == "help" or "h":
    print("\nMovie Categories:\n(Action, Adventure, Drama, Documentaries, Comedy, Horror, Family, Disney, Dreamworks, Pixar, Marvel, Dc Comics, Star Wars, Animated X Cartoon, Videos)\n")
elif start.lower() == "54":
    easter_egg()
else: print("wtf?") 
    
