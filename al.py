for swap in swaps:
    # Perform the swap operation on the input tensor.
    input_tensor = tf.map_fn(swap, input_tensor)
