import os
import numpy as np
src_dir = '/home/jaehwlee/Genre_classification/keras-sincnet/original_data/GTZAN/genres/'
save_dir = '/home/jaehwlee/Genre_classification/keras-sincnet/data_lists/labels.npy'
genres = {'metal': 0, 'disco': 1, 'classical': 2, 'hiphop': 3, 'jazz': 4,
          'country': 5, 'pop': 6, 'blues': 7, 'reggae': 8, 'rock': 9}
key_dir = 'GTZAN/genres/'
labels = dict()
for x, y in genres.items():
    folder = src_dir + x
    for root, subdirs, files in os.walk(folder):
        for file1 in files:
            #file_name = folder + "/" + file1
            #print(file_name)
            #print(files)
            my_key = key_dir +x +'/'+ file1
            labels[my_key] = y
        
np.save(save_dir, labels)

print(len(labels))
