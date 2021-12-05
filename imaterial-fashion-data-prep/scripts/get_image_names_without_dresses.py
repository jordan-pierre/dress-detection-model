# Create list of files that do not contain dresses
data_dir = 'data/'

# Set of all images
print('Reading all images file...')
all_image_names_set = set()
with open(data_dir + 'all_image_names_distinct.txt') as all_file:
    for line in all_file:
        all_image_names_set.add(line.rstrip())

# Set of images with dresses
print('Reading dress images file...')
dress_image_names_set = set()
with open(data_dir + 'images_names_with_dress.txt') as dress_file:
    for line in dress_file:
        dress_image_names_set.add(line.rstrip())

# Set of images without dresses
no_dress_image_names_set = all_image_names_set.difference(dress_image_names_set)

# Save images without dresses to txt file
print('Writing to file.')
with open(data_dir + 'image_names_without_dress.txt', 'w') as non_dress_file:
    for name in sorted(no_dress_image_names_set):
        non_dress_file.write(name + '\n')

