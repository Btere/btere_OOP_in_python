from dataclasses import dataclass
from typing import List, Tuple


import torch
import torch.nn as nn
from torch.optim.optimizer import Optimizer
from torch.optim import SGD
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

@dataclass
class TrainingModel:
    epoch: int = 5
    learning_rate: float = 0.01



# 1. Data Preparation
def read_data() -> torch.Tensor:
    """read dataset

    Returns:
        torch.Tensor
    """
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
    return train_dataset

def dataloader(train_data, batch_size: int = 64, shuffle: bool = True) -> Tuple[DataLoader, DataLoader]:
    """_summary_

    Args:
        train_data: dataset for training
        batch_size: size of data to be passed into the model, defaults to 64.
        shuffle: Defaults to True.

    Returns:
        Tuple[DataLoader, DataLoader]: 
    """
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=shuffle)
    return train_loader

# 2. Model Definition
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)  # Flatten the input tensor
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# 5. Training Loop
def train_model(model: SimpleNN, training_model: TrainingModel) -> Tuple[float, float]:
    """training model

    Args:
        model: the main model
        criterion (nn.CrossEntropyLoss)
        optimizer (Optimizer.SGD):
        training_model (TrainingModel):

    Returns:
        Tuple[float, float]:
    """
    model.train()
    #model = SimpleNN()

    #3 loss function
    criterion = nn.CrossEntropyLoss()
    # 4. Optimizer
    optimizer = SGD(model.parameters(), lr=training_model.learning_rate)

    for epoch in range(training_model.epoch):
        running_loss = 0.0
        correct: int = 0
        total: int = 0
        for batch_idx, (image_inputs, labels_input) in enumerate(dataloader):
        # Move inputs and labels to the device (if using GPU)
            image_inputs, labels_input = image_inputs.to('cpu'), labels_input.to('cpu')  # Change 'cpu' to 'cuda' if using GPU

        # Zero the parameter gradients
            optimizer.zero_grad()

        # Forward pass
            prediction_by_model = model(image_inputs)
            loss = criterion(prediction_by_model, labels_input)

        # Backward pass and optimize
            loss.backward()
            optimizer.step()
        
        # Print statistics
            running_loss += loss.item()
            predicted = prediction_by_model.argmax(axis=1)
            #labels = torch.argmax(labels_input, dim=1)
            correct += (predicted == labels_input).sum().item() ## Count correct predictions
            total += labels_input.size(0) # # Update the total number of samples
    average_loss = running_loss / len(dataloader)
    print(f'Epoch [{epoch + 1}/{training_model.epoch}], Loss: {average_loss:.4f}')
    accuracy = 100 * correct / total
    print(f'Accuracy: {accuracy:.2f}%')
        
    print("Finished Training")

def validate_on_unseen_data(model, val_loader, criterion):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
    
    average_loss = running_loss / len(val_loader)
    accuracy = 100 * correct / total
    return average_loss, accuracy


def evaluate_model_performamce(model, test_loader, criterion):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
    
    average_loss = running_loss / len(test_loader)
    accuracy = 100 * correct / total
    return average_loss, accuracy



if __name__ == "__main__":
    df = read_data()
    dataloader = dataloader(df)
    model = SimpleNN()
    model_training = train_model(model,training_model=TrainingModel)
