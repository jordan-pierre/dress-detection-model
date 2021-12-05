'''
Copy images that contain dresses from the wider data set to a new directory
'''

import shutil

def main():
    dress_reference_file = 'data/images_names_with_dress.txt'
    
    original_dir = '/home/jordan/Downloads/imaterialist-fashion-2019-FGVC6/train/'
    target_dir = 'images/dress_train/'

    # Read names from reference 
    dress_image_names_set = set()
    with open(dress_reference_file) as dress_file:
        for line in dress_file:
            dress_image_names_set.add(line.rstrip())
    
    # Copy images to target directory
    for image_file in sorted(dress_image_names_set):
        shutil.copyfile(original_dir + image_file, target_dir + image_file)


if __name__=='__main__':
    main()