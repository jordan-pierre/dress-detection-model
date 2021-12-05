'''
Copy rows from original train.csv that contain images with dresses.

NOTE: This copies all rows that describe files that contain a dress -- not just the dress label, 
      so 1 image might have a row that lables a dress and another row that labels a cardigan, for example.
      Depending on the performance of the dress detection model, I might want to come back to this to only include rows
      that specifically label the dress portion.
'''

# Create set of image names to whitelist
dress_reference_file = 'data/images_names_with_dress.txt'
dress_image_names_set = set()
with open(dress_reference_file) as dress_file:
    for line in dress_file:
        dress_image_names_set.add(line.rstrip())

# Copy line to new file if file from row is in the whitelist
read_file = 'data/train.csv'
write_file = 'data/train-filered.csv'
with open(read_file, 'r') as f_read, open(write_file, 'w') as f_write:
    f_write.write('ImageId,EncodedPixels,Height,Width,ClassId\n') # header row
    for line in f_read:
        row_file_name = line.split(',')[0]
        if row_file_name in dress_image_names_set:
            f_write.write(line)
