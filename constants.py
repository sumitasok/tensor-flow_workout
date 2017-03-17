import tensorflow as tf

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

d1tensor = tf.constant(1234)

d2tensor = tf.constant([1234,123])

d3tensor = tf.constant([[1234,123], [123,1234]])

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)

    output_d1 = sess.run(d1tensor)
    print(output_d1)

    output_d2 = sess.run(d2tensor)
    print(output_d2)

    output_d3 = sess.run(d3tensor)
    print(output_d3)
