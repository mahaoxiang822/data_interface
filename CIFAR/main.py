"""
Ulzee An
9/5/2017
"""

import os
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

import cifar10
from cifar10 import num_classes

cifar10.maybe_download_and_extract()
class_names = cifar10.load_class_names()

print class_names