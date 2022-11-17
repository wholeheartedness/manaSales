import requests
import colorama
import os
from re import search
colorama.init()

BLUE = colorama.Fore.LIGHTBLUE_EX
WHITE = colorama.Fore.WHITE

gamemodes = requests.get("https://api.manacube.com/api/statistics/gamemodes").json()

def printBanner():
    os.system("cls")
    print(" ")
    print(" ")
    print(f"{BLUE}     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗ {WHITE}███████╗ █████╗ ██╗     ███████╗███████╗")
    print(f"{BLUE}     ████╗ ████║██╔══██╗████╗  ██║██╔══██╗{WHITE}██╔════╝██╔══██╗██║     ██╔════╝██╔════╝   {BLUE} - by wholeheartedness")
    print(f"{BLUE}     ██╔████╔██║███████║██╔██╗ ██║███████║{WHITE}███████╗███████║██║     █████╗  ███████╗   {BLUE} - github.com/wholeheartedness")
    print(f"{BLUE}     ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║{WHITE}╚════██║██╔══██║██║     ██╔══╝  ╚════██║   {BLUE} - v1.0")
    print(f"{BLUE}     ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║{WHITE}███████║██║  ██║███████╗███████╗███████║   {BLUE} - written in python 3.8.0")
    print(f"{BLUE}     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝{WHITE}╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝")
    print(" ")

def printOptions():
    print(f"{BLUE}     [1] search for sva IDs")
    print(f"{WHITE}     [2] get average price of an sva on a gamemode")
    print(f"{BLUE}     [3] get total sva count on a gamemode")
    print(f"{WHITE}     [4] help")
    print(" ")

def searchForSva(svaList: list, queryAll: str):
    # seperate query into sections
    queryList = [i.lower() for i in queryAll.split("||")]
    finalList = []
    for sva in svaList:
        count = 0
        for query in queryList:
            if query  in sva:
                count += 1
                

            if count == len(queryList):
                finalList.append(sva)
    
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
                svas = f"https://api.manacube.com/api/svas/{gamemode}"

                svaList = []
                svaData = requests.get(svas).json()
                for sva in svaData:
                    svaList.append(sva["itemType"])

                svaList = list(dict.fromkeys(svaList))

                query = input("     query (seperate queries by '||'): ")
                print(f"{BLUE} ")
                for sva in searchForSva(svaList, query):
                    print("     " + sva)
                pause()
            else:
                print(" ")
                print(f"{BLUE}     Invalid gamemode, use the {WHITE}help{BLUE} option to find a list of gamemodes and more.")
                pause()
        
        elif choice == "2":
            gamemode = input("     gamemode: ")
            if gamemode in gamemodes:
                sva = input("     sva: ")
                svas = f"https://api.manacube.com/api/svas/{gamemode}"

                svaList = []
                svaData = requests.get(svas).json()
                for item in svaData:
                    svaList.append(item["itemType"])

                svaList = list(dict.fromkeys(svaList))
                if sva in svaList:
                    sales = f"https://api.manacube.com/api/svas/sales/{gamemode}/{sva}"

                    try:
                        salesData = requests.get(sales).json()
                        salesData[0]
                        print(" ")
                        print(f"{BLUE}     ---------- {WHITE + sva + BLUE} ----------")
                        print(" ")
                        print(f"     average value : {WHITE + str(round(salesData[0]['averageValue'], 2))} cubits")
                        print(f"{BLUE}     times sold : {WHITE + str(salesData[0]['timesSold'])}")
                        print(" ")
                        print(f"{BLUE}     -----------{'-'*len(sva)}-----------")
                        pause()
                    except IndexError:
                        print(" ")
                        print(f"{BLUE}     no sales found for {WHITE + sva}")
                        pause()

                else:
                    print(" ")
                    print(f"{BLUE}     Invalid sva ID, use the {WHITE}search{BLUE} option to find the correct ID.")
                    pause()
            else:
                print(" ")
                print(f"{BLUE}     Invalid gamemode, use the {WHITE}help{BLUE} option to find a list of gamemodes and more.")
                pause()

        elif choice == "3":
            gamemode = input("     gamemode: ")
            if gamemode in gamemodes:
                sva = input("     sva: ")
                svas = f"https://api.manacube.com/api/svas/{gamemode}"

                svaList = []
                svaData = requests.get(svas).json()
                for item in svaData:
                    svaList.append(item["itemType"])

                svaList = list(dict.fromkeys(svaList))
                if sva in svaList:
                    circulation = requests.get(f"https://api.manacube.com/api/svas/circulation/{gamemode}/{sva}").json()
                    
                    print(" ")
                    print(f"     {BLUE}There are currently {WHITE + str(circulation)} {str(sva) + BLUE} on {gamemode}.")
                    pause()

                else:
                    print(" ")
                    print(f"{BLUE}     Invalid sva ID, use the {WHITE}search{BLUE} option to find the correct ID.")
                    pause()
            else:
                print(" ")
                print(f"{BLUE}     Invalid gamemode, use the {WHITE}help{BLUE} option to find a list of gamemodes and more.")
                pause()

        elif choice == "4":
            print(f"{BLUE}     ---------- {WHITE}General help{BLUE} ----------")
            print(" ")
            print(f"{BLUE}      - This program is used to get sell information about svas on manacube.")
            print(f"{WHITE}      - Possible gamemodes are: survival, skyblock and earth")
            print(f"{BLUE}      - To use the other features of the program you must know the sva ID which can be found with the search option")
            print(f"{WHITE}      - The search feature is not perfect as the mana id is not the exact name as what appears in game")
            print(" ")
            print(f"{BLUE}     ---------- {WHITE}Searching for sva IDs{BLUE} ----------")
            print(" ")
            print(f"{BLUE}      - To search for sva IDs, use the search option.")
            print(f"{WHITE}      - Seperate queries with '||' to search via multiple filters at once.")
            print(f"{BLUE}      - Possible queries include:")
            print(f"{WHITE}      - 'mv' to filter by mineville svas")
            print(f"{BLUE}      - '17/19/20/21/22' to filter by years (does not include every sva made in that year because mana is annoying)")
            print(f"{WHITE}      - 'manasets' to only show sets")
            print(f"{BLUE}      - 'gadgets' to only show gadgets")
            print(f"{WHITE}      - 'wildtools' to filter by special effect tools (Ex: trench tools or sell wands)")
            print(f"{BLUE}      - press enter in the query field to find all svas on a specific gamemode")
            pause()

    except KeyboardInterrupt:
        pass