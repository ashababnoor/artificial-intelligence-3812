import cv2
import os
from os.path import isfile, join

def convert_pictures_to_video(pathIn, pathOut, fps, time):
    '''
    this function converts images to videos
    '''

    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    for i in range(len(files)):
        filename = pathIn + files[i]
        print('Now reading:', filename)

        '''reading images'''
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)

        if i == len(files) - 1:
            time *= 5

        for k in range(time):
            frame_array.append(img)

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    
    out.release()

# creating the video

directory = 'k-means_clustering/'
pathIn = directory + 'cluster_images/'
pathOut = directory + 'video/cluster_transformation.mp4'
fps = 24
time = 12

convert_pictures_to_video(pathIn, pathOut, fps, time)