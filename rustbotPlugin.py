import os, sys, ast

class Manager():
    def load(self,folder)
        paths = os.listdir(folder)
        plugins = []
        for file in paths:
            if(file.endswith(".rbp")):
                plugins.append(file)

        sys.path.insert(0, folder)

        info = {}
        
        for plugin in plugins:
            f = open(plugin,"r")
            pl = f.read()
            f.close()

            pl = ast.literal_eval(pl)

            info[plugin] = pl
        return info
            
            
            
            
            
                
                
