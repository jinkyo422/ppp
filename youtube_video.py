import numpy as np
import cv2
import pafy
import os

def youtube_capture(url):
    
    video = pafy.new(url)
    title = video.title
    title = title.replace(" ", "")
    title = title[:10]

    now_dir = os.path.dirname(os.path.realpath(__file__)) + "/Pose_Estimation/sample_images/" + title
    os.mkdir(now_dir)

    best = video.getbest()

    cap = cv2.VideoCapture(best.url)
    now = 1
    while(True):
        retval, frame = cap.read()
        if not retval:
            break

        key = cv2.waitKey(25)
        if key == 27:  # press ESC
            break
        cv2.IMREAD_UNCHANGED
        cv2.imwrite(now_dir + "/" + title + "_{:0>5}".format(str(now)) + ".png", frame)
        now = now + 1

    cv2.destroyAllWindows()
    print('Capture Finish!! Title = ' + title)
    return title
