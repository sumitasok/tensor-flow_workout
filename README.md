# tensor-flow_workout

hello_world.py

> Print hello wowrld with tensor flow.

here hello_constant is a 0-dimentional string tensor

all values are encapsulated in an object called `tensor`


constants.py

output:

```
b'Hello World!'
1234
[1234  123]
[[1234  123]
 [ 123 1234]]
 ```

 **value of tensor never changes**

 tensor flow session - environment for running a computationsla graph.

 placeholder.py

 the placeholder allows to set the value at the time when tf.session.run() is called.

 tf datatypes
  - tf.strnig
  - tf.int32
  - tf.float32

math

   - tf.add(1,2)
   - tf.substract(1,2)
   - tf.multiply(1,2)

type cast

	- tf.cast(tf.constant(2.2), tf.int32)

tf.Variable

	> This can be modified as opposed to tf.Constant and tf.Placeholder

tf.truncated_normal(x, y)

session.run(tf.global_variables_initializer())

> is required for initializing all the variables.

tf.zeros(shape)

softmax activation function.