import tensorflow as tf

# Create TensorFlow object called hello_constant
x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.int32)

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    z = sess.run(tf.subtract(tf.divide(x,y), 1), feed_dict = {x: 10, y: 2})
    print(z)

# TODO: Convert the following to TensorFlow:
# x = 10
# y = 2
# z = x/y - 1

# TODO: Print z from a session