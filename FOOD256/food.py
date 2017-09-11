"""
9/10/2017
Ulzee An

Interface to easily access FOOD256 data.
"""

import os, csv
from PIL import Image

class FoodLabel:
	def __init__(self, label_id, label_name):
		self.id = label_id
		self.name = label_name

def list_labels():
	"""
	Returns all labels with corresponding readable names.
	"""


	# label_folders = [fName for fName in folders if '.' not in fName]

	labels = None

	with open('./data/category.txt', 'rb') as cat_file:
		csv_stream = csv.reader(cat_file)
		labels_data = [row[0] for row in csv_stream][1:]
		labels = [FoodLabel(*tuple(row.split('\t'))) for row in labels_data]

	return labels

class FoodImage:
	def __init__(self, path, load = True):
		self.path = path
		self.data = Image.open(path) if load else None

	def rgb():
		pass

def get_examples(label, load_images = True):
	"""
	Returns set of images belonging to the given label.
	"""
	image_files = ['./data/%s/%s' % (label.id, fl) for fl in os.listdir('./data/%s' % (label.id)) if '-filled.jpg' in fl]
	assert len(image_files) != 0

	if not load_images:
		return image_files

	images = [FoodImage(path) for path in image_files]

	return images

if __name__ == '__main__':
	labels = list_labels()
	print len(labels), labels[0]
	example1 = labels[0]

	examples = get_examples(example1)
	print len(examples), examples[0].path
