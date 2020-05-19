import os
from datetime import datetime
from scipy.io import loadmat

def load_data(wiki_dir, dataset='wiki'):
    # Load the .mat metadata file
    metadata = loadmat(os.path.join(wiki_dir,"{}.mat".format(dataset)))
    
    # Load the list of all files
    full_path = metadata[dataset][0, 0]['full_path'][0]

    # List of matlab serial date numbers
    dob = metadata[dataset][0, 0]['dob'][0]

    # List of years when photo was taken 
    photo_taken = metadata[dataset][0, 0]['photo_taken'][0]

    # Calculate age for all dobs
    age = [calculate_age(photo_taken[i], dob[i]) for i in range(len(dob))]

    # Create a list of tuples containing a pair of image and corresponding age
    images = []
    age_list = []
    for index, image_path in enumerate(full_path):
        images.append(image_path[0])
        age_list.append(age[index])

    # Return the list of all images and ages
    return images, age_list

def calculate_age(taken, dob):
    birth = datetime.fromordinal(max(int(dob) - 366, 1))

    # assume the photo was taken in the middle of the year
    if birth.month < 7:
        return taken - birth.year
    else:
        return taken - birth.year - 1
        

