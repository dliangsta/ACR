import os
import argparse
import numpy as np
import torch
from PIL import Image
from glob import glob
from tqdm import tqdm
from torchvision.transforms import Resize


def get_new_fn(fn, data_dir, out_dir):
    assert data_dir in fn
    new_fn = fn.replace(data_dir, out_dir)
    new_fn = '.'.join(new_fn.split('.')[:-1]) + '.pt'
    return new_fn

def preprocess_image(fn, new_fn):
    # Assumes FN is a JPEG.
    img = Image.open(fn)
    img = Resize(28)(img)
    img = np.asarray(img, dtype=np.float)
    tensor = torch.from_numpy(img) / 256
    tensor = tensor.float().unsqueeze(dim=0)
    torch.save(tensor, new_fn)


def preprocess():
    parser = argparse.ArgumentParser(description='ACR Preprocess Example')
    parser.add_argument('data_dir', default='my-data')
    parser.add_argument('out_dir', default='my-preprocessed-data')
    parser.add_argument('--skip_existing', action='store_true')
    args = parser.parse_args()
    print(args)
    os.makedirs(args.out_dir, exist_ok=True)

    for fn in tqdm(glob(os.path.join(args.data_dir, '*'))):
        new_fn = get_new_fn(fn, args.data_dir, args.out_dir)
        if not os.path.isfile(new_fn) or not args.skip_existing:
            try:
                preprocess_image(fn, new_fn)
            except Exception as e:
                print("\n", fn, new_fn, e)


if __name__ == '__main__':
    preprocess()