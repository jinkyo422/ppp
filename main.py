import youtube_video
import sys
import os
import subprocess
from hmr import csv_join
import threading
import multiprocessing
import time

images_path = 'Pose_Estimation/sample_images'
jsons_path = 'Pose_Estimation/sample_jsons'
title = ' '

def jsonToCsv(images, jsons):
    for i in range(len(images)):
        subprocess.call('python2 hmr/demo.py --img_path ' + images_path + '/' + images[i] + ' --json_path ' + jsons_path + '/' + jsons[i], shell=True)

def main(url):

    global images_path, jsons_path, title

    title = youtube_video.youtube_capture(url)

    os.chdir('Pose_Estimation')
    from Pose_Estimation import two_d_pose_estimation
    now_dir = os.path.dirname(os.path.realpath(__file__)) + "/sample_jsons/" + title
    os.mkdir(now_dir)

    print('Multithreading about image to json')
    images_path = 'sample_images/' + title
    sample_images = os.listdir(images_path)
    sample_images.sort(key=lambda x: (x.split('/')[-1].split('.')[0]))

    two_d_pose_estimation.imageToJson(title)

    print('Multithreading Finish!!!')

    os.chdir('..')

    print('Multithreading about json to csv')
    images_path = 'Pose_Estimation/sample_images/' + title
    jsons_path = 'Pose_Estimation/sample_jsons/' + title
    sample_jsons = os.listdir(jsons_path)
    sample_jsons.sort(key=lambda x: (x.split('/')[-1].split('.')[0]))
    size = len(sample_jsons)
    thread_count = 20
    threads = []

    now_dir = os.path.dirname(os.path.realpath(__file__)) + "/hmr/output/csv/" + title
    os.mkdir(now_dir)
    now_dir = os.path.dirname(os.path.realpath(__file__)) + "/hmr/output/images/" + title
    os.mkdir(now_dir)

    for i in range(thread_count):
        thread = threading.Thread(target=jsonToCsv, args=(sample_images[i*size/thread_count:(i+1)*size/thread_count], sample_jsons[i*size/thread_count:(i+1)*size/thread_count], ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('Multithreading Finish!!!')

    csv_join.join_csv(title)
    subprocess.call('blender -b hmr/csv_to_bvh.blend -noaudio --python hmr/csv_to_bvh.py ' + title, shell=True)

if __name__ == '__main__':
    urlList = []
    # urlList.append('https://www.youtube.com/watch?v=VP5UPUSDC4M&ab_channel=pigmie') #BACKHANDSPRING
    # urlList.append('https://youtu.be/lWs7wDOdTYM') #pt
    # urlList.append('https://youtu.be/z3jUHGaKOxE')
    # urlList.append('https://youtu.be/tkcFmkmKRdM')
    # urlList.append('https://youtu.be/UZAa_Qu0LvU')
    # urlList.append('https://youtu.be/qN_YheWcXek')
    # urlList.append('https://youtu.be/VtoxgqJh3Nw')
    # urlList.append('https://youtu.be/oTFstcVkPEo')
    # urlList.append('https://youtu.be/yw9Q6UhiWlU')
    urlList.append('https://youtu.be/bzZNYJNAbEM')
    urlList.append('https://youtu.be/Y0Gr09B5Uk8')
    urlList.append('https://youtu.be/iEZmNyeHg4I')
    urlList.append('https://youtu.be/5JLEpEB1N3g')
    urlList.append('https://youtu.be/q24O3zYFf9E')
    urlList.append('https://youtu.be/uKWpaK18OJs')
    urlList.append('https://youtu.be/H78mpMup8Wo')

    for url in urlList:
        main(url)
