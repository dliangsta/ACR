# https://github.com/pytorch/examples/blob/master/mnist/main.py
import os
import torch

from torchvision import datasets, transforms
from torch.utils.data import Dataset
from glob import glob

def get_normalizing_transform():
    return transforms.Normalize((0.1307,), (0.3081,))

def get_default_transform():
    return transforms.Compose([
        transforms.ToTensor(),
        get_normalizing_transform(),
    ])

def get_default_train_data():
    return datasets.MNIST(root='./data', train=True, download=True, transform=get_default_transform())

def get_default_test_data():
    return datasets.MNIST(root='./data', train=False, transform=get_default_transform())


class AlternativeDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.fns = list(glob(os.path.join(self.data_dir, "*")))
        print(os.path.join(self.data_dir, "*"))
        self.transform = transforms.Compose([get_normalizing_transform()])
            

    def __len__(self):
        return len(self.fns)

    def fn_to_label(self, fn):
        return int(fn.split("/")[-1][0])

    def __getitem__(self, idx):
        fn = self.fns[idx]
        label = self.fn_to_label(fn)
        tensor =  self.transform(torch.load(fn))
        return tensor, label

def get_alternative_data(data_dir):
    return AlternativeDataset(data_dir)
