import requests
import colorama
import os
from mcuuid import MCUUID

colorama.init()

BLUE = colorama.Fore.LIGHTBLUE_EX
WHITE = colorama.Fore.WHITE
LIME = colorama.Fore.LIGHTGREEN_EX

gamemodes = ["survival", "skyblock", "earth"]
global LINKED

def checkLinked():
    global LINKED
    with open("user", "r") as ign:
        if ign.read() == "":
            LINKED = "link"
        else:
            LINKED = "unlink"
        
def printBanner():
    os.system("cls")
    print(" ")
    print(" ")
    print(f"{BLUE}     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗ {WHITE}███████╗ █████╗ ██╗     ███████╗███████╗")
    print(f"{BLUE}     ████╗ ████║██╔══██╗████╗  ██║██╔══██╗{WHITE}██╔════╝██╔══██╗██║     ██╔════╝██╔════╝   {BLUE} - by wholeheartedness")
    print(f"{BLUE}     ██╔████╔██║███████║██╔██╗ ██║███████║{WHITE}███████╗███████║██║     █████╗  ███████╗   {BLUE} - github.com/wholeheartedness")
    print(f"{BLUE}     ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║{WHITE}╚════██║██╔══██║██║     ██╔══╝  ╚════██║   {BLUE} - v1.1")
    print(f"{BLUE}     ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║{WHITE}███████║██║  ██║███████╗███████╗███████║   {BLUE} - written in python 3.8.0")
    print(f"{BLUE}     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝{WHITE}╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝")
    print(" ")

def printOptions():
    global LINKED
    checkLinked()
    with open("user", "r") as ign:
        ign = ign.read()

    if LINKED == "unlink":
        print(f"{BLUE}     Logged in as {LIME + ign}")
        print(" ")
    print(f"{BLUE}     [1] search for SVA IDs")
    print(f"{WHITE}     [2] get average price of an SVA on a gamemode")
    print(f"{BLUE}     [3] get total count of an SVA on a gamemode")
    print(f"{WHITE}     [4] {LINKED} a minecraft account")
    print(f"{BLUE}     [5] get stats of linked account")
    print(f"{WHITE}     [6] help")
    print(f"{BLUE}     [7] exit")
    print(" ")

def searchForSva(SVAList: list, queryAll: str):
    # seperate query into sections
    queryList = [i.lower() for i in queryAll.split("||")]
    finalList = []
    for SVA in SVAList:
        count = 0
        for query in queryList:
            if query  in SVA:
                count += 1
                

            if count == len(queryList):
                finalList.append(SVA)
    
    return finalList

def pause():
    print(f" {WHITE}")
    input("     Press enter to continue...")

while True:
    try:
        printBanner()
        printOptions()
        choice = input("     choice: ")
        printBanner()

        if choice == "1":
            gamemode = input("     gamemode: ")
            if gamemode in gamemodes:
                SVAs = f"https://api.manacube.com/api/svas/{gamemode}"

                SVAList = []
                SVAData = requests.get(SVAs).json()
                for SVA in SVAData:
                    SVAList.append(SVA["itemType"])

                SVAList = list(dict.fromkeys(SVAList))

                query = input("     query (seperate queries by '||'): ")
                print(f"{BLUE} ")
                for SVA in searchForSva(SVAList, query):
                    print("     " + SVA)
                pause()
            else:
                print(" ")
                print(f"{BLUE}     Invalid gamemode, use the {WHITE}help{BLUE} option to find a list of gamemodes and more.")
                pause()
        
        elif choice == "2":
            gamemode = input("     gamemode: ")
            if gamemode in gamemodes:
                SVA = input("     SVA: ")
                SVAs = f"https://api.manacube.com/api/svas/{gamemode}"

                SVAList = []
                SVAData = requests.get(SVAs).json()
                for item in SVAData:
                    SVAList.append(item["itemType"])

                SVAList = list(dict.fromkeys(SVAList))
                if SVA in SVAList:
                    sales = f"https://api.manacube.com/api/svas/sales/{gamemode}/{SVA}"

                    try:
                        salesData = requests.get(sales).json()
                        salesData[0]
                        print(" ")
                        print(f"{BLUE}     ---------- {WHITE + SVA + BLUE} ----------")
                        print(" ")
                        print(f"     average value : {WHITE + str(round(salesData[0]['averageValue'], 2))} cubits")
                        print(f"{BLUE}     times sold : {WHITE + str(salesData[0]['timesSold'])}")
                        print(" ")
                        print(f"{BLUE}     -----------{'-'*len(SVA)}-----------")
                        pause()
                    except IndexError:
                        print(" ")
                        print(f"{BLUE}     no sales found for {WHITE + SVA}")
                        pause()

                else:
                    print(" ")
                    print(f"{BLUE}     Invalid SVA ID, use the {WHITE}search{BLUE} option to find the correct ID.")
                    pause()
            else:
                print(" ")
                print(f"{BLUE}     Invalid gamemode, use the {WHITE}help{BLUE} option to find a list of gamemodes and more.")
                pause()

        elif choice == "3":
            gamemode = input("     gamemode: ")
            if gamemode in gamemodes:
                SVA = input("     SVA: ")
                SVAs = f"https://api.manacube.com/api/svas/{gamemode}"

                SVAList = []
                SVAData = requests.get(SVAs).json()
                for item in SVAData:
                    SVAList.append(item["itemType"])

                SVAList = list(dict.fromkeys(SVAList))
                if SVA in SVAList:
                    circulation = requests.get(f"https://api.manacube.com/api/svas/circulation/{gamemode}/{SVA}").json()
                    
                    print(" ")
                    print(f"     {BLUE}There are currently {WHITE + str(circulation)} {str(SVA) + BLUE} on {gamemode}.")
                    pause()

                else:
                    print(" ")
                    print(f"{BLUE}     Invalid SVA ID, use the {WHITE}search{BLUE} option to find the correct ID.")
                    pause()
            else:
                print(" ")
                print(f"{BLUE}     Invalid gamemode, use the {WHITE}help{BLUE} option to find a list of gamemodes and more.")
                pause()

        elif choice == "4":
            with open("user", "w") as ign:
                if LINKED == "link":
                    username = input("     username: ")
                    try:
                        player = MCUUID(name=username)
                        uuidList = list(player.uuid)
                        uuidList.insert(8, "-")
                        uuidList.insert(13, "-")
                        uuidList.insert(18, "-")
                        uuidList.insert(23, "-")
                        uuid = "".join(uuidList)
                        test = requests.get(f"https://api.manacube.com/api/cubits/{uuid}").json()
                        print(" ")
                        print(f"{BLUE}     {LIME + username + BLUE} has been linked.")
                        ign.write(username)
                    except ValueError:
                        print(f"{BLUE}     Invalid username, please enter a valid username.")

                    checkLinked()

                elif LINKED == "unlink":
                    with open("user", "r") as user:
                        accountName = user.read()
                        ign.write("")
                        checkLinked()
                        print(f"{BLUE}     Successfully unlinked the account.")
                        
            pause()

        elif choice == "5":
            print("     Working...")
            if LINKED == "unlink":
                with open("user", "r") as user:
                    accountName = user.read()
                    player = MCUUID(name=accountName)
                    uuidList = list(player.uuid)
                    uuidList.insert(8, "-")
                    uuidList.insert(13, "-")
                    uuidList.insert(18, "-")
                    uuidList.insert(23, "-")
                    uuid = "".join(uuidList)

                    cubits = requests.get(f"https://api.manacube.com/api/cubits/{uuid}").json()
                    try:
                        cubits["status"]
                        cubits = 0.0
                    except:
                        pass

                    survivalSVAs = requests.get(f"https://api.manacube.com/api/svas/survival/{uuid}").json()
                    skyblockSVAs = requests.get(f"https://api.manacube.com/api/svas/skyblock/{uuid}").json()
                    earthSVAs = requests.get(f"https://api.manacube.com/api/svas/earth/{uuid}").json()
                    try:
                        guild = requests.get(f"https://api.manacube.com/api/guilds/player/{uuid}").json()
                        guildName = guild["tag"]
                        guildRank = guild["rank"]
                        guildLevel = guild["level"]
                        members = []
                        for member in guild["members"]:
                            members.append((member["name"], member["rank"]))

                    except:
                        guildName = "None"

                    try:
                        friends = requests.get(f"https://api.manacube.com/api/friends/{uuid}").json()
                        friendsList = []
                        for player in friends:
                            friendsList.append(player["name"])
                    except TypeError:
                        friendsList = ["None"]
                    patrons = requests.get(f"https://api.manacube.com/api/patrons/patrons").json()
                    patronPlus = requests.get(f"https://api.manacube.com/api/patrons/patronsplus").json()

                    for player in patrons:
                        if uuid == player["uuid"]:
                            isPatron = "Yes"
                        else:
                            isPatron = "No"

                    for player in patronPlus:
                        if uuid == player["uuid"]:
                            isPatronPlus = "Yes"
                        else:
                            isPatronPlus = "No"

                    

                    printBanner()

                    print(f"{BLUE}     ---------- {WHITE}General{BLUE} ----------")
                    print(" ")
                    print(f"{BLUE}     Cubit balance: " + str(cubits))
                    print(f"{WHITE}     is patron: " + isPatron)
                    print(f"{BLUE}     is patron plus: " + isPatronPlus)
                    print(f"{WHITE}     friends: " + BLUE + ", ".join(friendsList))
                    if guildName != "None":
                        print(" ")
                        print(f"{BLUE}     ---------- {WHITE}Guild{BLUE} ----------")
                        print(" ")
                        print(f"{BLUE}     guild name: " + guildName)
                        print(f"{WHITE}     guild rank: " + str(guildRank))
                        print(f"{BLUE}     guild level: " + str(guildLevel))
                        print(f"{WHITE}     guild members: ", end="")
                        for member in members:
                            print(f"{BLUE + member[0]}: {WHITE + member[1] + BLUE}, ", end="")

                        print("")

                    print(" ")
                    print(f"{BLUE}     ---------- {WHITE}SVAs{BLUE} ----------")
                    print(" ")
                    print(f"{BLUE}     {WHITE}survival{BLUE} SVAs: \n")
                    for SVA in survivalSVAs:
                        print(f"{WHITE}     - {BLUE + SVA['itemType']}")
                    print(" ")

                    print(f"{BLUE}     {WHITE}skyblock{BLUE} SVAs: \n")
                    for SVA in skyblockSVAs:
                        print(f"{WHITE}     - {BLUE + SVA['itemType']}")
                    print(" ")

                    print(f"{BLUE}     {WHITE}earth{BLUE} SVAs: \n")
                    for SVA in earthSVAs:
                        print(f"{WHITE}     - {BLUE + SVA['itemType']}")
                    print(" ")


            else:
                print(" ")
                print(f"{BLUE}     You must link an account first, use the {WHITE}link{BLUE} option.")
            
            pause()

        elif choice == "6":
            print(f"{BLUE}     ---------- {WHITE}General help{BLUE} ----------")
            print(" ")
            print(f"{BLUE}      - This program is used to get sell information about SVAs on manacube.")
            print(f"{WHITE}      - Possible gamemodes are: survival, skyblock and earth")
            print(f"{BLUE}      - To use the other features of the program you must know the SVA ID which can be found with the search option")
            print(f"{WHITE}      - The search feature is not perfect as the mana id is not the exact name as what appears in game")
            print(" ")
            print(f"{BLUE}     ---------- {WHITE}Searching for SVA IDs{BLUE} ----------")
            print(" ")
            print(f"{BLUE}      - To search for SVA IDs, use the search option.")
            print(f"{WHITE}      - Seperate queries with '||' to search via multiple filters at once.")
            print(f"{BLUE}      - Possible queries include:")
            print(f"{WHITE}      - 'mv' to filter by mineville SVAs")
            print(f"{BLUE}      - '17/19/20/21/22' to filter by years (does not include every SVA made in that year because mana is annoying)")
            print(f"{WHITE}      - 'manasets' to only show sets")
            print(f"{BLUE}      - 'gadgets' to only show gadgets")
            print(f"{WHITE}      - 'wildtools' to filter by special effect tools (Ex: trench tools or sell wands)")
            print(f"{BLUE}      - press enter in the query field to find all SVAs on a specific gamemode")
            pause()

        elif choice == "7":
            os.system("cls")
            exit(0)

    except KeyboardInterrupt:
        pass