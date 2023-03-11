# OPTIONS (BASIC | ADVANCED | HELP | EASTER EGG - "54")
import os
import sys
import time
# sys.path.insert(1, "./terminal")
from terminal import clear, restart

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

def start():
      clear()
      print(f"{clr.BLUE}\n**********************\n{clr.RESET}")
      print(f"{clr.BLUE}NEMFLIX - Movie JSON Writer\n***********\nBy: 54, flippN, Pugz, RoffeG, Lz.'²{clr.RESET}")
      print(f"{clr.BLUE}\n**********************\n\n{clr.RESET}")
      start.first_que = input(f"{clr.BLUE}Create new movie? (Yes/No/help/54)\n{clr.CYAN}INPUT:{clr.GREEN} ").lower()

def opt_bas(): # basic
        opt_bas.movCat = input(f"{clr.BLUE}\nmovie category:\n{clr.CYAN}INPUT:{clr.GREEN} ").lower()
        opt_bas.movNam = input(f"{clr.BLUE}\nMovie Name:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_bas.movDes = input(f"{clr.BLUE}\nMovie Description:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_bas.movYea = input(f"{clr.BLUE}\nMovie Year:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_bas.movTim = input(f"{clr.BLUE}\nMovie Time:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_bas.movNamTrim = opt_bas.movNam.replace(" ", "_")
        opt_bas.movCatTrim = opt_bas.movCat[0:3].lower()

def opt_adv(): # advanced
        opt_adv.movCat = input(f"{clr.BLUE}\nmovie category:\n{clr.CYAN}INPUT:{clr.GREEN} ").lower()
        opt_adv.movNam = input(f"{clr.BLUE}\nMovie Name:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_adv.movDes = input(f"{clr.BLUE}\nMovie Description:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_adv.movYea = input(f"{clr.BLUE}\nMovie Year:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_adv.movTim = input(f"{clr.BLUE}\nMovie Time:\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_adv.movIco4k = input(f"{clr.BLUE}\n4k movie?\n- (Yes=1, No=0)\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_adv.movIcoCc = input(f"{clr.BLUE}\nDoes the movie have subtitles available?\n- (Yes=1, No=0)\n{clr.CYAN}INPUT:{clr.GREEN} ")
        opt_adv.movNamTrim = opt_adv.movNam.replace(" ", "_")
        opt_adv.movCatTrim = opt_adv.movCat[0:3].lower()
#      opt_adv.movMetCc = input(f"{clr.CYAN}\nEnter all subtitles available")

def opt_help():
     print(f"{clr.BLUE}\n**********************\nMovie Categories:\n{clr.CYAN}(Action, Adventure, Drama, Documentaries, Comedy, Horror, Family, Disney, Dreamworks, Pixar, Marvel, Dc Comics, Star Wars, Animated X Cartoon, Videos)\n{clr.BLUE}**********************\nCommands:\n{clr.CYAN}1. exit - terminates the process\n2. kill - terminates the process.\n{clr.BLUE}**********************\n\n{clr.RESET}")
     done_reading = input(f"{clr.BLUE}{clr.UNDERLINE}NEMFLIX{clr.RESET}{clr.BLUE}: {clr.CYAN}Type: \"done\", when done reading.\n{clr.CYAN}INPUT:{clr.GREEN} ").lower()
     if done_reading == "done":
        print(f"{clr.BLUE}{clr.UNDERLINE}NEMFLIX{clr.RESET}{clr.BLUE}: {clr.RED}{clr.FLICKER}RESTARTING..{clr.RESET}")
        time.sleep(4.5)
        clear()
        restart()

def opt_easter_egg():
    i = 1
    while i <= 500:
        print(i * f"{clr.FLICKER}\nNEMFLIX\n************")
        i = i + 1