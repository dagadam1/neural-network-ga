import sys 

def find_max_epoch(net: str):
    #Only keep everything before "Final epoch completed!"
    epochs_str = net.split("Final epoch completed!")[0]
    #First line is network size so take everything except it
    epochs = epochs_str.splitlines()[1:]
    
    for epoch in epochs:
        pass
    


def main():
    filename = sys.argv[1]
    f = open(filename)
    content = f.read()
    chunks = content.split("#")
    #Remove unnecessary lines
    nets = [i for i in chunks if i != ".\n" and i != ""]
    find_max_epoch(nets[1])
    
    
    

if __name__ == "__main__":
    main()