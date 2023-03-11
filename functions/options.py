# OPTIONS (BASIC | ADVANCED | HELP | EASTER EGG - "54")
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
    GREEN_FLICKER = "\33[5m"

def opt_bas(): # basic
        opt_bas.movCat = input(f"{clr.CYAN}\nmovie category:\n{clr.GREEN}").lower()
        opt_bas.movNam = input(f"{clr.CYAN}\nMovie Name:\n{clr.GREEN}")
        opt_bas.movDes = input(f"{clr.CYAN}\nMovie Description:\n{clr.GREEN}")
        opt_bas.movYea = input(f"{clr.CYAN}\nMovie Year:\n{clr.GREEN}")
        opt_bas.movTim = input(f"{clr.CYAN}\nMovie Time:\n{clr.GREEN}")
        opt_bas.movNamTrim = opt_bas.movNam.replace(" ", "_")
        opt_bas.movCatTrim = opt_bas.movCat[0:3].lower()

def opt_adv(): # advanced
        opt_adv.movCat = input(f"{clr.CYAN}\nmovie category:\n{clr.GREEN}").lower()
        opt_adv.movNam = input(f"{clr.CYAN}\nMovie Name:\n{clr.GREEN}")
        opt_adv.movDes = input(f"{clr.CYAN}\nMovie Description:\n{clr.GREEN}")
        opt_adv.movYea = input(f"{clr.CYAN}\nMovie Year:\n{clr.GREEN}")
        opt_adv.movTim = input(f"{clr.CYAN}\nMovie Time:\n{clr.GREEN}")
        opt_adv.movIco4k = input(f"{clr.CYAN}\n4k movie?\n- (Yes=1, No=0)\n{clr.GREEN}")
        opt_adv.movIcoCc = input(f"{clr.CYAN}\nDoes the movie have subtitles available?\n- (Yes=1, No=0)\n{clr.GREEN}")
        opt_adv.movNamTrim = opt_adv.movNam.replace(" ", "_")
        opt_adv.movCatTrim = opt_adv.movCat[0:3].lower()
#      opt_adv.movMetCc = input(f"{clr.CYAN}\nEnter all subtitles available")

def opt_help():
     print(f"{clr.CYAN}\nMovie Categories:\n(Action, Adventure, Drama, Documentaries, Comedy, Horror, Family, Disney, Dreamworks, Pixar, Marvel, Dc Comics, Star Wars, Animated X Cartoon, Videos)\n")
#      print("""""")
def opt_easter_egg():
    i = 1
    while i <= 500:
        print(i * f"{clr.GREEN_FLICKER}\nNEMFLIX\n************")
        i = i + 1