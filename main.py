import youtube_video
import sys
import os
import subprocess
from hmr import csv_join
import threading

images_path = 'Pose_Estimation/sample_images'
jsons_path = 'Pose_Estimation/sample_jsons'
title = ' '

def imageToJson(a, b):
    subprocess.call('python2 two_d_pose_estimation.py ' + str(a) + ' ' + str(b) + ' ' +title, shell=True)

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
    size = len(sample_images)
    thread_count = 4
    threads = []

    for i in range(thread_count):
        thread = threading.Thread(target=imageToJson, args=(i*size/thread_count, (i+1)*size/thread_count, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        
    print('Multithreading Finish!!!')

    os.chdir('..')

    print('Multithreading about json to csv')
    images_path = 'Pose_Estimation/sample_images/' + title
    jsons_path = 'Pose_Estimation/sample_jsons/' + title
    sample_jsons = os.listdir(jsons_path)
    sample_jsons.sort(key=lambda x: (x.split('/')[-1].split('.')[0]))
    size = len(sample_jsons)
    thread_count = 36
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
    urlList.append('https://youtu.be/lWs7wDOdTYM') #pt
    # urlList.append('https://www.youtube.com/watch?v=xRuXDojcbgk')
    # urlList.append('https://www.youtube.com/watch?v=swRNeYw1JkY')
    # urlList.append('https://www.youtube.com/watch?v=kEVW_Xv3TqY')
    # urlList.append('https://www.youtube.com/watch?v=s4Yh35JyC2E')
    # urlList.append('https://www.youtube.com/watch?v=mKXtVQnqhB4')
    # urlList.append('https://www.youtube.com/watch?v=ezoZfZK75zA')
    # urlList.append('https://www.youtube.com/watch?v=JYsusrFHGdg')
    # urlList.append('https://www.youtube.com/watch?v=vAFCrMgJrmI')
    # urlList.append('https://www.youtube.com/watch?v=0SNnCr0-9AQ')
    # urlList.append('https://www.youtube.com/watch?v=ID1KMP2AKfc')
    # urlList.append('https://www.youtube.com/watch?v=2f1mpyYAulw')
    # urlList.append('https://www.youtube.com/watch?v=j_WizUnWyQk')
    # urlList.append('https://www.youtube.com/watch?v=M8PX2E88Ufo')
    # urlList.append('https://www.youtube.com/watch?v=5MUjkisuHB8')
    # urlList.append('https://www.youtube.com/watch?v=rsFzLJT9rzA')

    for url in urlList:
        main(url)
