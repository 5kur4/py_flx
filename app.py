# https://github.com/5kur4/py_flx
import json
import os
import sys # so we can import file from dir
import time
# clear = lambda: os.system('cls')
# clear()
os.system("title " + "NEMFLIX - Movie JSON Writer") # set terminal title
sys.path.insert(1, "./functions/") # find files in folder.
from options import start, opt_bas, opt_adv, opt_help, opt_easter_egg
from terminal import clear, restart, quit_app


class clr:
    WHITE = "\033[97m"
    GREY   = "\033[90m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    PURPLE = "\033[95m"
    YELLOW_WEIRD = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    FLICKER = "\33[5m"

# start = input(f"{clr.CYAN}Create new movie? (Yes/No/help/54): {clr.GREEN}").lower()
start()

if start.first_que == "yes":
    que2 = input(f"{clr.CYAN}Options: Basic | Advanced: {clr.GREEN}").lower()
    if que2 == "basic":
        opt_bas()
        infoJson = {
            "movNam": opt_bas.movNam,
            "movDes": opt_bas.movDes,
            "movYea": int(opt_bas.movYea),
            "movTim": opt_bas.movTim,
            "movPth":   "/browse/mov/"+opt_bas.movCatTrim+"/nocat/"+opt_bas.movNamTrim+".html",
            "movImg":   "/pub/covr/"+opt_bas.movCatTrim+"/nocat/"+opt_bas.movNamTrim+".webp",
            "movImgBg": "/pub/covr/"+opt_bas.movCatTrim+"/nocat/"+opt_bas.movNamTrim+"_bg.webp",
            "movVidBg": "/pub/covr/"+opt_bas.movCatTrim+"/nocat/"+opt_bas.movNamTrim+"_vid.webp",
            "movIcoNm": 1,
            "movIcoNw": 1,
            "movIco4k": 0,
            "movIcoCc": 0
        }
        json_obj = json.dumps(infoJson, indent=4)
        with open("./json/" + opt_bas.movCat + "/" + opt_bas.movNamTrim + ".json", "w") as outfile:
            outfile.write(json_obj);
            print(f"{clr.BLUE}\n***********\nNEMFLIX - \"" + opt_bas.movNamTrim+f".json\" has been created!\n***********\n\n{clr.RESET}")
            restart()
        
        # print("\n", infoJson)

    elif que2 == "advanced":
        # if
        opt_adv()
        jsonMeta = {
            "movNam": opt_adv.movNam,
            "movDes": opt_adv.movDes,
            "movYea": int(opt_adv.movYea),
            "movTim": opt_adv.movTim,
            "movPth":   "/browse/mov/"+opt_adv.movCatTrim+"/nocat/"+opt_adv.movNamTrim+".html",
            "movImg":   "/pub/covr/"+opt_adv.movCatTrim+"/nocat/"+opt_adv.movNamTrim+".webp",
            "movImgBg": "/pub/covr/"+opt_adv.movCatTrim+"/nocat/"+opt_adv.movNamTrim+"_bg.webp",
            "movVidBg": "/pub/covr/"+opt_adv.movCatTrim+"/nocat/"+opt_adv.movNamTrim+"_vid.webp",
            "movIcoNm": 1,
            "movIcoNw": 1,
            "movIco4k": int(opt_adv.movIco4k),
            "movIcoCc": int(opt_adv.movIcoCc)
        }
        writeMeta = json.dumps(jsonMeta, indent=4)
        with open("./json/" + opt_adv.movCat + "/" + opt_adv.movNamTrim + ".json", "w") as outfile:
            outfile.write(writeMeta);
            print(f"{clr.BLUE}\n***********\nNEMFLIX - \"" + opt_adv.movNamTrim+f".json\" has been created!\n***********\n\n{clr.RESET}")

elif start.first_que == "no":
    print(f"{clr.BLUE}{clr.UNDERLINE}NEMFLIX{clr.RESET}{clr.BLUE}: {clr.RED}{clr.FLICKER}EXITING...{clr.RESET}")
    quit_app()
    # print("\nOkay..?\n")
elif start.first_que == "help":
    opt_help()
elif start.first_que == "54":
    opt_easter_egg()
elif start.first_que == "kill" or start.first_que == "exit":
    print(f"\n{clr.BLUE}{clr.UNDERLINE}NEMFLIX{clr.RESET}{clr.BLUE} - {clr.RED}Terminating Process\n{clr.RESET}")
    quit_app()
else: print("wtf?") 
