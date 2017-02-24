# Tensor Flow

We’ll use TensorFlow to classify images from the notMNIST dataset - a dataset of images of English letters from A to J

## Installation
We'll use conda:
```
conda create -n tensorflow python=3.5
source activate tensorflow
conda install pandas matplotlib jupyter notebook scipy scikit-learn
conda install -c conda-forge tensorflow
```


## Hello World
As usual! Start by printing Hello World in console.

`python HelloWorld.py`

### Understanding Hello World

In TensorFlow, data isn’t stored as integers, floats, or strings. These values are encapsulated in an object called a tensor. `hello_constant` here is a 0-dimensional string tensor.
More tensors in variety of sizes:
```
# A is a 0-dimensional int32 tensor
A = tf.constant(1234) 

# B is a 1-dimensional int32 tensor
B = tf.constant([123,456,789]) 

# C is a 2-dimensional int32 tensor
C = tf.constant([ [123,456,789], [222,333,444] ])
```


## Session
TensorFlow’s api is built around the idea of a computational graph, a way of visualizing a mathematical process.
A "TensorFlow Session", is an environment for running a graph. The session is in charge of allocating the operations to GPU(s) and/or CPU(s), including remote machines.
```
with tf.Session() as sess:
    output = sess.run(hello_constant)
```

The code has already created the tensor, hello_constant, from the previous lines. The next step is to evaluate the tensor in a session.

The code creates a session instance, sess, using tf.Session. The sess.run() function then evaluates the tensor and returns the results.

## Feeding data
When you want to feed a non-constant, use `tf.placeholder()` and `feed_dict`.
`tf.placeholder()` - Returns a tensor that gets its value from data passed to the tf.session.run() function, allowing you to set the input right before the session runs.

Example:
```
x = tf.placeholder(tf.string)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'}) // Tensor x set to string 'Hello World'
```

```
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
```

## Math

We can use math operations to process the input
```
x = tf.add(5, 2)  # 7
x = tf.subtract(10, 4) # 6
y = tf.multiply(2, 5)  # 10
```

### Converting types
It may be necessary to convert between types to make certain operators work together.

```
tf.subtract(tf.constant(2.0),tf.constant(1))  # Fails with ValueError: Tensor conversion requested dtype float32 for Tensor with dtype int32
tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))   # 1
```

Check `Math.py`

[More Math operations](https://www.tensorflow.org/api_guides/python/math_ops)

# Neural Nets using TensorFlow

## Variables
The goal of training a neural network is to modify weights and biases to best predict the labels. In order to use weights and bias, you'll need a Tensor that can be modified. This leaves out `tf.placeholder()` and `tf.constant()`, since those Tensors can't be modified. This is where `tf.Variable` class comes in.

## Initialization
```
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
```

Use the `tf.truncated_normal()` function to generate random numbers from a normal distribution. returns a tensor with random values from a normal distribution whose magnitude is no more than 2 standard deviations from the mean.

```
n_features = 120
n_labels = 5
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))
```

```
n_labels = 5
bias = tf.Variable(tf.zeros(n_labels))
```


## Softmax

`x = tf.nn.softmax([2.0, 1.0, 0.2])`

Try `python Softmax.py`

