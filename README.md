# video_to_bvh

## requirement

* python 2.7
* tensorflow 1.13.1
* keras 2.3.1

## usage

1. bash make_folders.sh

2. bash install_requirement.sh

3. download model
* wget https://people.eecs.berkeley.edu/~kanazawa/cachedir/hmr/models.tar.gz && tar -xf models.tar.gz && mv models hmr/
* wget -nc --directory-prefix=./Pose_Estimation/keras/ 		https://www.dropbox.com/s/llpxd14is7gyj0z/model.h5

3. python main.py
