import os, sys

class Manager():
    def load(self,folder)
        paths = os.listdir(folder)
        plugins = []
        for file in paths:
            if(file.endswith(".py")):
                dot_pos = len(file)-3
                plugins.append(file[:dot_pos])

        sys.path.insert(0, folder)

        info = {}
        
        for plugin in plugins:
            pl = __import__(plugin)

            main = pl.main
            events = pl.events
            author = pl.author
            name = pl.name
            version = pl.version
            short_desc = pl.short_desc

            info[plugin]["main"]=main
            info[plugin]["events"]=events
            info[plugin]["author"]=author
            info[plugin]["name"]=name
            info[plugin]["version"]=version
            info[plugin]["short_desc"]=short_desc

        return info
            
            
            
            
            
                
                
