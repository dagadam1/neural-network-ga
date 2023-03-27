import network
import mnist_loader
from time import process_time

# Hyper-parameters
epochs = 50
mini_batch_size = 10
eta = 4.0 # eta = learning_rate

runs = 5

networks_to_test = [5, 10, 30, 50, 70, 90, 120, 784]

#The seeds are "popped" from these lists. That means the seeds at the ends will be used first.
parameters_seeds = [8323988, 6856221, 3484827, 2202620, 3325501, 3909291, 3738380, 3010278, 753857, 6842634]

data_seeds = [9378532, 5329960, 5517929, 6653044, 5284670, 1346193, 4037161, 4498556, 8215724, 3467963]

def seed_random(parameters_seed, data_seed):
    network.random.seed(data_seed)
    network.np.random.seed(parameters_seed)
    
def timer(function, *args):
    """Runs a function and measures the time it takes.

    Args:
        function (callable): The function to run.

    Returns:
        (func_return, time) (any, num): 'func_return' is the return value of the funtion. 'time' is the time it took to run.
    """
    start = process_time()
    func_return = function(*args)
    stop = process_time()
    return (func_return, stop - start)
    

def train_net(hidden_layer_size, parameters_seed, data_seed):
    """Train a network consisting of one input layer with 784 neurons,
    one output layer with 10 neurons, and one hidden layer
    with 'hidden_layer_size' neurons.

    Args:
        hidden_layer_size (int): number of neurons in the hidden layer
    """
    seed_random(parameters_seed, data_seed)
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    
    print(f"#Network size: [784, {hidden_layer_size}, 10]")
    net = network.Network([784, hidden_layer_size, 10])
    net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)
    print(f"Final epoch completed! \nWeights: {net.weights} \nBiases: {net.biases}")
    print("#.")

def main():
    assert len(parameters_seeds) >= runs and len(data_seeds) >= runs, f"Not enough seeds for {runs} runs!"
    
    for i in range(runs):
        
        current_parameters_seed = parameters_seeds.pop()
        current_data_seed = data_seeds.pop()
        print(f"\
##Running networks. Run nr. {i+1}/{runs}. \
Current random seed data: {current_data_seed} Current random seed parameters: {current_parameters_seed} \
Global hyper-parameters: epochs = {epochs}, mini_batch_size = {mini_batch_size}, eta = {eta}")
        
        for size in networks_to_test:
            print(f"(Time: {timer(train_net, size, current_parameters_seed, current_data_seed)[1]})") 
        
        print("##.")
    
    
if __name__ == "__main__":
    main()
