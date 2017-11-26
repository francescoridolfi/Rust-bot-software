import os, sys, ast

class Manager():
    path = "plugins"

    def setpath(self, path):
        self.path = path
    
    def load(self):
        paths = os.listdir(self.path)
        plugins = []
        for file in paths:
            if(file.endswith(".rbp")):
                plugins.append(file)

        info = {}
        
        for plugin in plugins:
            f = open(self.path+"/"+plugin,"r")
            pl = f.read()
            f.close()

            pl = ast.literal_eval(pl)

            info[plugin] = pl
        return info

    def cmd(self, plugin, cmd):
        plugins = self.load()
        main = plugins[plugin]["main"]
        sys.path.insert(0,self.path)

        pl = __import__(main)
        
        return pl.commandExec(cmd)
        
        
            
            
            
            
            
                
                
