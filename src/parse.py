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
    #Dictionary cotaining all the types of networks and a list of their highest epochs.
    summary: dict[str, list[int]] = {}
    
    filename = sys.argv[1]
    f = open(filename)
    content = f.read()
    
    #Find runs
    runs = content.split("##")
    #Only keep necessary lines and remove dots, for example
    runs = [i for i in runs if i != ".\n" and i != ""][0:] 
    
    for run in runs:
        #Print from index 18 in the string of this run, to the first newline character.
        #This is the info about this run.
        print(run[18:run.find("\n")], end="\n\n")
        #Find network tests
        chunks = run.split("#")
        #Only keep necessary lines and remove dots, for example
        nets = [i for i in chunks if i != ".\n" and i != ""][1:]
        for net in nets:
            #Some of the lines in 'nets' are timers
            #Check if this line is a timer and if so, print it and continue to the next line
            if net.find("(Time: ") != -1:
                print(net[2:])
                continue
            
            #Find the first line i.e. the size of the network 
            size = net.split('\n', 1)[0]
            
            #Find highest epoch
            max_epoch_value = find_max_epoch_value(net)
            
            #Add this network's highest epoch to the summary
            if size in summary.keys():
                summary[size].append(max_epoch_value)
            else:
                summary[size] = [max_epoch_value]
            
            print(size)
            print(find_max_epoch_value(net))
    
    print(summary)
    

if __name__ == "__main__":
    main()