import tensorflow as tf

# Create TensorFlow object called hello_constant
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(x, feed_dict={x: 'Hello World', y: 123, z: 45.67})
    print(output)
