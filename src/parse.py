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
    #First line is network size so keep everything except it
    epochs = epochs_str.splitlines()[1:]
    
    
    epoch_values = [int(epoch.split(" ")[2]) for epoch in epochs]
        
    return max(epoch_values)
    


def main():
    filename = sys.argv[1]
    f = open(filename)
    content = f.read()
    chunks = content.split("#")
    #Remove unnecessary lines
    nets = [i for i in chunks if i != ".\n" and i != ""][1:]
    for net in nets:
        #Print first line i.e. the size of the network
        print(net.split('\n', 1)[0])
        print(find_max_epoch_value(net))
    
    
    

if __name__ == "__main__":
    main()