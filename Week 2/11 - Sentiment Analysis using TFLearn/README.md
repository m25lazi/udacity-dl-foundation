# TFLearn
TFLearn does a lot of things for you such as initializing weights, running the forward pass, and performing backpropagation to update the weights. You end up just defining the architecture of the network (number and type of layers, number of units, etc.) and how it is trained.

## Installing for conda

### Create conda environment
`conda create -n tflearn python=3.5`

### Activate the environment
`source activate tflearn`

### Install other dependencies for the notebook
`conda install numpy pandas jupyter notebook matplotlib`

### Install TFLearn and dependencies
```
conda install scipy h5py
pip install --user tensorflow
pip install  --user TFLearn
```