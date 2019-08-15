### StreetScroe2.0

- - -

This is the StreetScroe2.0 project.

Use `yeg_src/image_download/fetchImagesfromURL_multithread.py` to download from OpenStreetCam

Use `yeg_src/image_downlaod_osc/fetchImagesfromURL_multithread.py` to download from Google Streetview

put Google API Key and Secret in:  
`yeg_src/image_download/googleapikey.txt`  
`yeg_src/image_download/googleapisecret.txt`

use create_lmdb.py and caffe's creat mean image script to get the mean image.

Read more about mean image and how to train with caffe at
<https://chunml.github.io/ChunML.github.io/project/Training-Your-Own-Data-On-Caffe>

use workspace/dlcity/models/trial_model_1/train.sh to train with caffe

# dlcity
adopted Code for the ECCV 2016 paper "Deep Learning the City: Quantifying Urban Perception At A Global Scale"
