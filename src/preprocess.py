import os

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "../rawdata")
OUTPUT_DIR = os.path.join(BASE_DIR, "../dataset")
TRAIN_DIR_NAME = "mnist_png/training"
TEST_DIR_NAME = "mnist_png/testing"


def preprocess(data_dir):
    dataset = datasets.ImageFolder(
        root=data_dir,
        transform=transforms.Compose(
            [
                transforms.Grayscale(),
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,)),
            ]
        ),
    )
    print(f"preprocess: {data_dir}")
    return dataset


def save_data(data, output_dir, filename):
    data_loader = DataLoader(data, batch_size=len(data))
    data_loaded = next(iter(data_loader))
    torch.save(data_loaded, os.path.join(output_dir, filename))


def main():
    training_dir = os.path.join(RAW_DATA_DIR, TRAIN_DIR_NAME)
    test_dir = os.path.join(RAW_DATA_DIR, TEST_DIR_NAME)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    training_data = preprocess(training_dir)
    test_data = preprocess(test_dir)

    save_data(training_data, OUTPUT_DIR, filename="training.pt")
    save_data(test_data, OUTPUT_DIR, filename="test.pt")


if __name__ == "__main__":
    main()
