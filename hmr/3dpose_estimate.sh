#!/bin/bash

for f in Pose_Estimation/sample_images/*; do

	filename=$(basename -- "$f")
  no_ext="${filename%.*}"
  
  echo "Processing $no_ext"
  
  python2 hmr/demo.py --img_path $f \
                     --json_path Pose_Estimation/sample_jsons/$no_ext.json  
  
done

echo "Done"
