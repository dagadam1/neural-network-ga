import network
import mnist_loader

# Hyper-parameters
epochs = 30
mini_batch_size = 10
eta = 3.0

parameters_random_seed = 27182
data_random_seed = 31415
def reset_random():
    network.random.seed(data_random_seed)
    network.np.random.seed(parameters_random_seed)

def train_net(hidden_layer_size):
    """Train a network consisting of one input layer with 784 neurons,
    one output layer with 10 neurons, and one hidden layer
    with 'hidden_layer_size' neurons.

    Args:
        hidden_layer_size (int): number of neurons in the hidden layer
    """
    reset_random()
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    
    print(f"#Network size: [784, {hidden_layer_size}, 10]")
    net = network.Network([784, hidden_layer_size, 10])
    net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)
    print(f"Final epoch completed! \nWeights: {net.weights} \nBiases: {net.biases}")
    print("#.")

def main():
    print(f"#Running networks. Random seed data: {data_random_seed} Random seed parameters: {parameters_random_seed} Global hyper-parameters: epochs = {epochs}, mini_batch_size = {mini_batch_size}, eta = {eta}")
    train_net(5)
    train_net(10)
    train_net(30)
    train_net(50)
    train_net(70)
    train_net(90)
    train_net(120)
    train_net(784)
    
    
if __name__ == "__main__":
    main()