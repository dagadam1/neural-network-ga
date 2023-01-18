import sys 

def find_max_epoch_value(net: str):
    """Takes the output from a network from the test program and
    finds the epoch with the highest number of correct results

    Args:
        net (str): Network output to find biggest epoch of

    Returns:
        int: The value of the highest epoch
    """
    
    #Only keep everything before "Final epoch completed!"
    epochs_str = net.split("Final epoch completed!")[0]
    #First line is network size so take everything except it
    epochs = epochs_str.splitlines()[1:]
    
    for epoch in epochs:
        epoch.
        
    return net
    


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