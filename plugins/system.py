def commandExec(cmd):
    if(cmd == "Hello"):
        return "Hello Dear!"
    elif(cmd == "What's your name?"):
        return "My name is Rust-bot!"
    elif(cmd == "Save me"):
        name = input("What's your name? ")
        return "Hello "+name+"!"
