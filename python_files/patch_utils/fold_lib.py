import tensorflow as tf
import numpy as np
import math

# takes as an input ordered start, end points, rotated patches
# returns rotated patches with fold. All empty cells are labeled as -2
# All coordinates are specified from the left-bottom point

@tf.function
def _simple_fold_neightbours(patches, x_start, y_start, x_end, y_end, thickness):
    # add 2
    pathces_plus_2 = tf.add(patches, 2)
    
    # cast variables to float
    x_start_f, y_start_f = tf.cast(x_start, dtype=tf.float32), tf.cast(y_start, dtype=tf.float32)
    x_end_f, y_end_f =  tf.cast(x_end, dtype=tf.float32), tf.cast(y_end, dtype=tf.float32)
    thickness_f = tf.cast(thickness, dtype=tf.float32)
    
    # if a, b are parameters of the line: y = ax + b,
    # find 1/a
    one_div_a = (x_end_f - x_start_f) / (y_end_f - y_start_f) 
    
    # get (x, y) thickness representation
    angle = - tf.math.atan((y_end_f - y_start_f) / (x_end_f - x_start_f))
    projected_x = thickness_f * tf.cos(math.pi/2.0 - angle)
    projected_y = thickness_f * tf.sin(math.pi/2.0 - angle)
    
    # cast variables to int
    projected_x_i = tf.cast(projected_x, dtype=tf.int32)
    projected_y_i = tf.cast(projected_y, dtype=tf.int32)

    # get starting point of right border
    right_border_start = x_start_f + thickness_f / tf.cos(math.pi/2.0 - angle)
    
    # get left border
    left_border = tf.cast(tf.range(x_start_f, x_end_f, delta=-one_div_a, dtype=tf.float32), dtype=tf.int32)
    left_border_appendix = x_end * tf.ones(x_end - tf.shape(left_border), dtype=tf.int32)
    full_size_left_border = tf.concat((left_border, left_border_appendix), 0)
    
    # get right border
    right_border = tf.cast(tf.range(right_border_start, x_end_f, delta=-one_div_a, dtype=tf.float32), dtype=tf.int32)
    right_border_appendix = x_end * tf.ones(x_end - tf.shape(right_border), dtype=tf.int32)
    full_size_right_border = tf.concat((right_border, right_border_appendix), 0)

    # produce left mask
    left_mask = tf.expand_dims(tf.expand_dims(tf.sequence_mask(full_size_left_border, x_end, dtype=tf.float32), 0), 3)
    left_mask_expanded = tf.broadcast_to(left_mask, [tf.shape(patches)[0], x_end, x_end, tf.shape(patches)[3]])
    
    # produce right mask
    right_mask_inverse = tf.expand_dims(tf.expand_dims(tf.sequence_mask(full_size_right_border, x_end, dtype=tf.float32), 
                                                       0), 
                                        3)
    right_mask = tf.math.abs(right_mask_inverse - 1)
    right_mask_expanded = tf.broadcast_to(right_mask, [tf.shape(patches)[0], x_end, x_end, tf.shape(patches)[3]])
    
    # get masked
    left_part = pathces_plus_2 * left_mask_expanded
    right_part = pathces_plus_2 * right_mask_expanded
    
    # shift right part
    half_shifted_right_part = tf.roll(right_part, shift=(-projected_x_i), axis=(2))
    shifted_right_part = tf.roll(half_shifted_right_part, shift=(projected_y_i), axis=(1))
    
    
    # get folded patch
    folded_patch = left_part + shifted_right_part - 2

    return folded_patch
    



@tf.function
def _order_neightbouts(patches, x_start, y_start, x_end, y_end):
    # cast variables to float
    x_start_f, y_start_f = tf.cast(x_start, dtype=tf.float32), tf.cast(y_start, dtype=tf.float32)
    x_end_f, y_end_f =  tf.cast(x_end, dtype=tf.float32), tf.cast(y_end, dtype=tf.float32)
    
    center = tf.cast(tf.shape(patches)[1], dtype=tf.float32) /2
    
    # calculate vector product of start and end ponints with respect
    v_prod = (x_start_f - center) * (y_end_f - center) - (x_end_f - center) * (y_start_f - center)
    
    
    # init returning functions
    def f_x_start(): return x_start
    def f_y_start(): return y_start
    def f_x_end(): return x_end
    def f_y_end(): return y_end
    
    x_start_right_order = tf.cond(v_prod < 0, f_x_start, f_x_end)
    y_start_right_order = tf.cond(v_prod < 0, f_y_start, f_y_end)
    x_end_right_order = tf.cond(v_prod < 0, f_x_end, f_x_start)
    y_end_right_order = tf.cond(v_prod < 0, f_y_end, f_y_start)
    
    return x_start_right_order, y_start_right_order, x_end_right_order, y_end_right_order



# takes as an input unordered start, end points, unrotated patches
# returns unrotated patches with fold. All empty cells are labeled as -2
# All coordinates are specified from the left-bottom point


def universal_fold_neightbours(patches, x_start, y_start, x_end, y_end, thickness):
    # get the right order of starting and ending points
    x_start_right_order, y_start_right_order, x_end_right_order, y_end_right_order = _order_neightbouts(patches, 
                                                                                                        x_start, 
                                                                                                        y_start, 
                                                                                                        x_end, 
                                                                                                        y_end)

    # rotate functions return rotated_patches, x_start_top, y_start_top, x_end_left, y_end_left, case
    # for positive values rotation rotates counter-clockwise
    def remain(): return patches, x_start_right_order, y_start_right_order, x_end_right_order, y_end_right_order, 0
    def rotate_counter_clockwise_1(): return tf.contrib.image.rotate(patches, math.pi/2), \
                                             tf.shape(patches)[1] - y_start_right_order, \
                                             tf.shape(patches)[2], \
                                             tf.shape(patches)[1], \
                                             x_end_right_order, \
                                             1
    def rotate_counter_clockwise_2(): return tf.contrib.image.rotate(patches, math.pi), \
                                             tf.shape(patches)[1] - x_start_right_order, \
                                             tf.shape(patches)[2], \
                                             tf.shape(patches)[1], \
                                             tf.shape(patches)[2] - y_end_right_order, \
                                             2
    def rotate_counter_clockwise_3(): return tf.contrib.image.rotate(patches, 3*math.pi/2), \
                                             y_start_right_order, \
                                             tf.shape(patches)[2], \
                                             tf.shape(patches)[1], \
                                             tf.shape(patches)[2] - x_end_right_order, \
                                             3
    
    def cases_0_or_2(): return tf.cond(tf.math.equal(y_start_right_order, tf.shape(patches)[1]),
                                       remain,
                                       rotate_counter_clockwise_2)
    
    def cases_1_or_3(): return tf.cond(tf.math.equal(x_start_right_order, tf.shape(patches)[1]),
                                       rotate_counter_clockwise_1,
                                       rotate_counter_clockwise_3)
    
    # rotate
    state = tf.math.logical_or(tf.math.equal(y_start_right_order, 0), tf.math.equal(y_start_right_order, tf.shape(patches)[1]))
    rotated_patches, x_start_top, y_start_top, x_end_left, y_end_left, case = tf.cond(state,
                                                                                      cases_0_or_2,
                                                                                      cases_1_or_3)
    
    # make a fold
    folded_unrotated_patch = _simple_fold_neightbours(rotated_patches, x_start_top, y_start_top, x_end_left, y_end_left, thickness)
    
    # unrotate
    def unrotate_0_or_2(): return tf.cond(tf.math.equal(case, 0),
                                          lambda: tf.contrib.image.rotate(folded_unrotated_patch, 0),
                                          lambda: tf.contrib.image.rotate(folded_unrotated_patch, -math.pi))
    
    def unrotate_1_or_3(): return tf.cond(tf.math.equal(case, 1),
                                          lambda: tf.contrib.image.rotate(folded_unrotated_patch, -math.pi/2),
                                          lambda: tf.contrib.image.rotate(folded_unrotated_patch, -3*math.pi/2))
    
    
    folded_unrotated_patch = tf.cond(tf.math.logical_or(tf.math.equal(case, 0), tf.math.equal(case, 2)),
                                     unrotate_0_or_2,
                                     unrotate_1_or_3)
    
    
    return folded_unrotated_patch
        

