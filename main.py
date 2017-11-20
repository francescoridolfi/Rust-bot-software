import os
import rustbotPlugin.Manager as plm
print("""
   ___           __    ___       __ 
  / _ \__ _____ / /_  / _ )___  / /_
 / , _/ // (_-</ __/ / _  / _ \/ __/
/_/|_|\_,_/___/\__/ /____/\___/\__/ 
                                    
""")


print('Loading plugins: ')
plugins = plm.load("plugins")

if(plugins != {}):
    print("No plugins found!")
