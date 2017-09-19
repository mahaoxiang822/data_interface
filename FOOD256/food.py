"""
9/10/2017
Ulzee An

Interface to easily access FOOD256 data.
"""

import os, csv
from PIL import Image

FOOD_PATH = os.environ['FOOD256_PATH']

class FoodLabel:
	def __init__(self, label_id, label_name):
		self.id = label_id
		self.name = label_name

class FoodImage:
	def __init__(self, path, load = True):
		self.path = path
		self.data = Image.open(path) if load else None

	def rgb():
		pass

def labels():
	"""
	Returns all labels with corresponding readable names.
	"""


	# label_folders = [fName for fName in folders if '.' not in fName]

	labels = None

	with open(os.path.join(FOOD_PATH, 'data/category.txt'), 'rb') as cat_file:
		csv_stream = csv.reader(cat_file)
		labels_data = [row[0] for row in csv_stream][1:]
		labels = [FoodLabel(*tuple(row.split('\t'))) for row in labels_data]

	return labels

def examples(label, load_images = True, limit = None):
	"""
	Returns set of images belonging to the given label.
	"""
	image_files = [os.path.join(FOOD_PATH, 'data/%s/%s' % (label.id, fl)) for fl in os.listdir(os.path.join(FOOD_PATH, 'data/%s' % (label.id))) if '-filled.jpg' in fl]
	assert len(image_files) != 0

	if limit:
		image_files = image_files[:limit]

	if not load_images:
		return image_files

	images = [FoodImage(path, load_images) for path in image_files]

	return images

food = { 'labels': labels, 'examples': examples }

# def food_paths():
# 	return []

# def get_batch(indices):
# 	return []

# __all__ = ['get_labels', 'get_examples']

if __name__ == '__main__':
	labels = food_labels()
	print len(labels), labels[0]
	example1 = labels[0]

	examples = food_examples(example1)
	print len(examples), examples[0].path
