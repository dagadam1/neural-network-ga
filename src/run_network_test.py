import network
import mnist_loader

# Hyper-parameters
epochs = 30
mini_batch_size = 10
eta = 3.0

random_seed = 31415
network.random.seed(random_seed)
network.np.random.seed(random_seed)

def train_net(sizes):
    net = network.Network(sizes)
    net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()


net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
