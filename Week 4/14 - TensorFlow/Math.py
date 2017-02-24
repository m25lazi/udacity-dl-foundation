# Taken from Udacity's Quiz
# TODO: Convert the following to TensorFlow:
# x = 10
# y = 2
# z = x/y - 1

# TODO: Print z from a session

# Solution
import tensorflow as tf

x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x, y), tf.cast(tf.constant(1), tf.float64))

with tf.Session() as sess:
    output = sess.run(z) 
    print(output)