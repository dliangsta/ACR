# ACR

### Guidelines
Welcome to the project. In order to share your model and make this project scalable, we require that you adhere to the following guidelines.

1. Create a zip file with the following items:
   1. A `README` with any instructions you have that are outside of this guideline.
   2. Your code.
   3. A small example dataset to evaluate the code on.
   4. Any weights you want to share.
   5. A `environment.yml` file. You should create a conda environment with the dependencies you will need and export it as `environment.yml` with the command `conda env export > environment.yml`. We highly prefer models written in PyTorch but can try to work with models written in different frameworks. See [this link](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment) for details on exporting conda environments.
   6. A `preprocess.sh` executable that will allow us to preprocess our files in the way that you did. We should be able to run it with `./preprocess.sh path-to-our-data output-data-path`. Include any simple data format / directory structure requirements in your `README`. Note that if you want to allow arguments to be passed from the shell script to your python script, you can use `python script.py $@` in your shell script as described [here](https://stackoverflow.com/questions/46364143/pass-arguments-to-python-from-bash-script).
   7. A `train.sh` executable that will allow us to train a model using your code on our own (preprocessed) data. 
   8. A `test.sh` executable that will allow us to evaluate our trained model or your trained model on our own (preprocessed) data.
2. Upload the zip file to Google Drive and make sure that anyone with the link can view and download the zip file.
3. Fill out [this submission form](https://forms.gle/txfwdN4m15iX5FmB8).

### Testing
Suppose your zip is `your-directory.zip`, your conda environment is `your-environment`, your data is in `example-data`, and another person's data is in `my-data`.
On a fresh Ubuntu VM with the latest version of CUDA and CUDNN, we should be able to run your code in `your-directory.zip` with conda environment `your-environment` with the following steps:
```
unzip your-directory.zip
cd your-directory
chmod +x *.sh

conda env create -f environment.yml
conda activate your-environment

./preprocess.sh ./my-data ./my-preprocessed-data
./preprocess.sh ./example-data ./example-preprocessed-data

./train.sh ./example-preprocessed-data
./test.sh ./example-preprocessed-data

./train.sh ./my-preprocessed-data
./test.sh ./my-preprocessed-data
```

### Example
We have provided an example for you, please [take a look](https://github.com/dliangsta/ACR/tree/master/example).
