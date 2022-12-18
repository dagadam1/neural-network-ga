import network
import mnist_loader

# Hyper-parameters
epochs = 3
mini_batch_size = 10
eta = 3.0

random_seed = 31415
network.random.seed(random_seed)
network.np.random.seed(random_seed)

def train_net(hidden_layer_size):
    """Train a network consitsting of one input layer with 784 neurons,
    one output layer with 10 neurons, and one hidden layer
    with 'hidden_layer_size' neurons.

    Args:
        hidden_layer_size (int): number of neurons in the hidden layer
    """
    
    net = network.Network([784, hidden_layer_size, 10])
    net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)
    
    print(net)

def main():
    
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

    train_net(30)
    
if __name__ == "__main__":
    main()