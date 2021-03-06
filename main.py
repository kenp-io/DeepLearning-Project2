import torch
import activation
import layer
import sequential
import loss
import math
import optimizer


def test_accuracy(model, test_input, test_target):

    output = model(test_input)

    output[output >= 0] = 1
    output[output < 0] = -1
    goodValue = torch.full((len(output), 1), 0)
    goodValue[output == test_target] = 1
    return goodValue.sum()/len(goodValue)

if __name__=="__main__":

    #criterion = loss.LossBCE()
    criterion = loss.LossMSE()
    model = sequential.Sequential(
                layer.Linear(2, 25),
                activation.ReLU(),
                layer.Linear(25, 50),
                activation.ReLU(),
                layer.Linear(50, 50),
                activation.ReLU(),
                layer.Linear(50, 25),
                activation.ReLU(),
                layer.Linear(25, 1),
                activation.Tanh()
                #activation.Sigmoid()
            )

    train_input = torch.rand((1000,2))
    train_target = torch.rand((1000,1))
    train_target[((train_input-0.5)**2).sum(1) < 1/(2*math.pi)] = -1
    train_target[((train_input-0.5)**2).sum(1) >= 1/(2*math.pi)] = 1

    test_input = torch.rand((1000,2))
    test_target = torch.rand((1000,1))
    test_target[((test_input-0.5)**2).sum(1) < 1/(2*math.pi)] = -1
    test_target[((test_input-0.5)**2).sum(1) >= 1/(2*math.pi)] = 1

    #Normalization
    mu, std = train_input.mean(0), train_input.std(0)
    train_input.sub_(mu).div_(std)
    test_input.sub_(mu).div_(std)

    epochs = 10000
    ps = model.parameters()
    optim = optimizer.SGD(model.parameters())
    for i in range(epochs):

        output = model(train_input)

        optim.zero_grad()
        gradwrrtxL = criterion.backward(output, train_target)

        model.backward(gradwrrtxL)

        optim.step()


        if i % 10 == 0:
            test_accuracyV = test_accuracy(model, test_input, test_target)
            print(criterion.forward(output, train_target), test_accuracyV, test_accuracy(model, train_input, train_target))
