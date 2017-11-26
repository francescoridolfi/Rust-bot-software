import os
import rustbotPlugin
import time

def cmdInPlugin(cmd,plugins):
    for k in plugins:
        if(cmd in plugins[k]["commands"]):
            return k
    return None

def start():
    print("""
       ___           __    ___       __ 
      / _ \__ _____ / /_  / _ )___  / /_
     / , _/ // (_-</ __/ / _  / _ \/ __/
    /_/|_|\_,_/___/\__/ /____/\___/\__/ 
                                        
    """)

    plm = rustbotPlugin.Manager
    print("==================")
    print('Loading plugins: ')
    plm().setpath("plugins")
    plugins = plm().load()

    if(plugins == {}):
        print("No plugins found!")
    else:
        i=1
        for k in plugins:
            print(str(i)+". "+plugins[k]["name"] + ": " + plugins[k]["desc"])
            i=i+1
        print("All plugins loaded!")

    print("==================")
    print("Rust-bot is now waiting for you!")


    while True:
        msg = input("> ")

        if(msg == "reload"):
            print("Reloading...")
            start()
        elif(msg == "bye"):
            print("Byee")
            time.sleep(2)
            exit()
            
        pl = cmdInPlugin(msg, plugins)
        if(pl != None):
            res=plm().cmd(pl,msg)
            print(res)

start()


