# ---------------------------------------------------------------#
#   astroNN.nn.numpy: tools written with numpy instead of tf
# ---------------------------------------------------------------#
import astropy.units as u
import numpy as np
from astroNN.config import MAGIC_NUMBER


def sigmoid(x):
    """
    NAME: sigmoid
    PURPOSE: numpy implementation of tf.sigmoid
    INPUT:
        x (ndarray): input
    OUTPUT:
        (ndarray)
    HISTORY:
        2018-Apr-11 - Written - Henry Leung (University of Toronto)
    """
    return 1 / (1 + np.exp(-x))


def sigmoid_inv(x):
    """
    NAME: sigmoid_inv
    PURPOSE: numpy implementation of tf.sigmoid inverse
    INPUT:
        x (ndarray): input
    OUTPUT:
        (ndarray)
    HISTORY:
        2018-Apr-11 - Written - Henry Leung (University of Toronto)
    """
    return np.log(x / (1 - x))


def l1(x, l1=0.):
    """
    NAME: l1
    PURPOSE: numpy implementation of tf.keras.regularizers.l1
    INPUT:
        x (ndarray): input
    OUTPUT:
        (ndarray)
    HISTORY:
        2018-Apr-11 - Written - Henry Leung (University of Toronto)
    """
    l1_x = 0.
    l1_x += np.sum(l1 * np.abs(x))
    return l1_x


def l2(x, l2=0.):
    """
    NAME: l2
    PURPOSE: numpy implementation of tf.keras.regularizers.l2
    INPUT:
        x (ndarray): input
    OUTPUT:
        (ndarray) representing regularising term
    HISTORY:
        2018-Apr-11 - Written - Henry Leung (University of Toronto)
    """
    l2_x = 0.
    l2_x += np.sum(l2 * np.square(x))
    return l2_x


def relu(x):
    """
    NAME: relu
    PURPOSE: numpy implementation of tf.nn.relu
    INPUT:
        x (ndarray): input
    OUTPUT:
        (ndarray) representing activated ndarray
    HISTORY:
        2018-Apr-11 - Written - Henry Leung (University of Toronto)
    """
    return x * (x > 0)


def mean_absolute_percentage_error(x, y, axis=None):
    """
    NAME: mean_absolute_percentage_error
    PURPOSE:
        mean_absolute_percentage_error using numpy abs(x-y)/y
        preserve magic_number
    INPUT:
        x (ndarray, astropy quantity): prediction
        y (ndarray, astropy quantity): ground truth
        axis (int): numpy axis
    OUTPUT:
        (ndarray) representing activated ndarray
    HISTORY:
        2018-Apr-11 - Written - Henry Leung (University of Toronto)
    """
    if type(x) == u.quantity.Quantity:
        x = x.value
    if type(y) == u.quantity.Quantity:
        y = y.value

    return np.ma.array(np.abs((x-y)/y)*100., mask=[(x == MAGIC_NUMBER) | (y == MAGIC_NUMBER)]).mean(axis=axis)


def mean_absolute_error(x, y, axis=None):
    """
    NAME: mean_absolute_error
    PURPOSE:
        mean_absolute_error using numpy abs(x-y)/y
        preserve magic_number
    INPUT:
        x (ndarray, astropy quantity): prediction
        y (ndarray, astropy quantity): ground truth
        axis (int): numpy axis
    OUTPUT:
        (ndarray) representing activated ndarray
    HISTORY:
        2018-Apr-11 - Written - Henry Leung (University of Toronto)
    """
    if type(x) == u.quantity.Quantity:
        x = x.value
    if type(y) == u.quantity.Quantity:
        y = y.value

    return np.ma.array(np.abs(x-y), mask=[(x == MAGIC_NUMBER) | (y == MAGIC_NUMBER)]).mean(axis=axis)