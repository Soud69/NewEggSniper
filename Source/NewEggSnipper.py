try:
    import requests
    import datetime
    import time
    import colorama
    import os
    from os import system
    from colorama import Fore

    colorama.init(autoreset=True)
    system("title " + "Soud Was Here - @_agf - Soud#0737")
except Exception as m:
    print("Error Found:")
    print(m)
    input()
    exit()
print("""
    ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
    ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
    ╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
    ░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
                              """, Fore.GREEN + "Credit @_agf - Soud#0737\nThis is simple tool by Soud to Check NewEgg Product if In Stock",
      Fore.RED + "\n                    FREE AND NOT FOR SELL\n\n")
noe = int(input("[Choose Mode]\n1) Send To Telegram\n2) Send To Discord\n3) Nothing\n>> "))
if noe == 1:
    bottoken = str(input("Enter BotToken: "))
    yourod = str(input("Enter Your ID: "))
elif noe == 2:
    webhook = str(input("Enter Webhook: "))
elif noe == 3:
    pass
else:
    print("Wrong Mode, Closing")
    time.sleep(3)
    exit()

pid = str(input("Enter Product URL\n>> "))
if "https://www.newegg.com/global/" in pid:
    pass
else:
    print("Not Newegg URL, Closing")
    time.sleep(3)
    exit()
while 1:
    try:
        req = requests.get(pid)
        time.sleep(3)
        if "OUT OF STOCK.</strong>" in req.text:
            print(Fore.RED+"Out Of Stock: ", pid)
        elif "In stock.</strong>" in req.text:
            x = datetime.datetime.now()
            time = x.strftime("%x %X")
            print(Fore.GREEN+f"In Stock: {pid}\nTime: {time}")
            if noe == 1:
                reqq = requests.get(
                    f"https://api.telegram.org/bot{bottoken}/sendmessage?chat_id={yourod}&text=Found Product\n{pid}\nTime: {time}\nBy @Soud69 - Soud#0737")
                print("Done Sent to Telegram.\n")
                input()
                exit()
            elif noe == 2:
                discordsend = {
                    "content": 69,
                    "embeds": [
                        {
                            "title": f"Found: {pid}",
                            "description": f"Success Found: {pid}\nAt: {time}\nBy #Daddy Soud",
                            "color": 13605911,
                            "author": {
                                "name": "Soud Newegg Sniper",
                                "url": "https://instagram.com/_agf",
                                "icon_url": "https://media3.giphy.com/media/CPlkqEvq8gRDW/giphy.gif"
                            },
                            "footer": {
                                "text": "Made By Soud - Soud#0737"
                            },
                            "timestamp": time,
                            "image": {
                                "url": "https://66.media.tumblr.com/e407db5c879927b5ae85d1ffabf385c4/tumblr_pbnj5bfkr91vtm42eo3_500.gif"
                            }
                        }
                    ],
                    "username": "Instagram Swap [Soud]",
                    "avatar_url": "https://c4.wallpaperflare.com/wallpaper/744/280/893/death-note-l-2500x1600-anime-death-note-hd-art-wallpaper-preview.jpg"
                }
                disc = requests.post(webhook, json=discordsend)
                print("Done Sent to Discord.\n")
                input()
                exit()
            elif noe == 3:
                print("Done Checking.\n")
                time.sleep(3)
                exit()
    except Exception as m:
        print(Fore.RED+"Error Found:")
        print(m)
        input("Press Enter To Exit")
        exit()
    else:
        print(Fore.RED+f"Error!\n{pid}\n{req.text}")
