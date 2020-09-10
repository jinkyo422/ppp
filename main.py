import youtube_video
import sys
import os
import subprocess
from hmr import csv_join
import threading
os.chdir('Pose_Estimation')
from Pose_Estimation import two_d_pose_estimation

images_path = 'Pose_Estimation/sample_images'
jsons_path = 'Pose_Estimation/sample_jsons'

def threadCall(image, json):
    subprocess.call('python2 hmr/demo.py --img_path ' + images_path + '/' + image + ' --json_path ' + jsons_path + '/' + json, shell=True)

def main(url):

    title = youtube_video.youtube_capture(url)
    print('Capture Finish!!!')

    two_d_pose_estimation.imageToJson()

    os.chdir('..')

    print('Multithreading about json to csv')
    sample_images = os.listdir(images_path)
    sample_jsons = os.listdir(jsons_path)
    thread_count = len(sample_jsons)
    threads = []

    for i in range(thread_count):
        thread = threading.Thread(target=threadCall, args=(sample_images[i], sample_jsons[i], ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print('Multithreading Finish!!!')

    csv_join.join_csv(title)
    subprocess.call('blender -b hmr/csv_to_bvh.blend -noaudio --python hmr/csv_to_bvh.py ' + title, shell=True)

if __name__ == '__main__':
    # main(sys.argv[1])
    # main('https://youtu.be/lWs7wDOdTYM')

    urlList = []
    urlList.append('https://youtu.be/lWs7wDOdTYM') #pt

    for url in urlList:
        main(url)