# StreetScroe2.0

## Acknowledgement

* * *

The raw votes data is from data/votes/safe.csv from <https://github.com/abhimanyudubey/dlcity>

The model is from ECCV 2016 paper "Deep Learning the City: Quantifying Urban Perception At A Global Scale" <https://arxiv.org/abs/1608.01769>

adopted Code from <https://github.com/abhimanyudubey/dlcity>

the pre-trained weight `VGG_ILSVRC_19_layers.caffemodel` from Caffe Model Zoo' s [ILSVRC-2014 model (VGG team) with 19 weight layers](https://gist.github.com/ksimonyan/3785162f95cd2d5fee77#file-readme-md)

Download caffemodel [url](http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_19_layers.caffemodel)

## How to get data

* * *

1.  ### Convert Raw Data

    Use `python yeg_src/convert_format.py` to convert raw data to get training images list input
    and list of images with empty url.

2.  ### Get Image URLs and Download

    Fetch the urls for images and download

    -   Option 1:

        1.  Put Google Static Streeview API Key and Secret in:  
            `yeg_src/image_download/googleapikey.txt`  
            `yeg_src/image_download/googleapisecret.txt`

        2.  Run `cp yeg_data\images_list_emptyurl.csv yeg_data\images_list_osc.csv`  

        3.  Use `python yeg_src/image_download_osc/fetch_osc_api_url.py` to get urls for images from Google Streetview

        4.  Use `yeg_src/image_downlaod_osc/fetchImagesfromURL_multithread.py` to download from the url got from Google Streetview

        5.  Use 'yeg_src/cleanup_invalid_images.py' to clean up

    -   Option 2:  

        1.  Run `cp yeg_data\images_list_emptyurl.csv yeg_data\images_list.csv`  

        2.  Use `python yeg_src/image_download_osc/fetch_osc_api_url.py` to get urls for images from OpenStreetCam

        3.  Use `python yeg_src/image_download/fetchImagesfromURL_multithread.py` to download from the url got from OpenStreetCam

        4.  Use 'yeg_src/cleanup_invalid_images.py' to clean up

## [Caffe](https://github.com/BVLC/caffe)

Read more about mean image and how to install and train with caffe at ["Training With Your Own Dataset on Caffe"](https://chunml.github.io/ChunML.github.io/project/Training-Your-Own-Data-On-Caffe)

* * *

### [Installation instructions](http://caffe.berkeleyvision.org/installation.html)

### Mean Image

use `yeg_src/create_lmdb.py` to get the lmdb for the training images.

The model requires us to subtract the image mean from each image, so we have to compute the mean. caffe/tools/compute_image_mean.cpp implements that.
This file is at `yeg_src/compute_image_mean.cpp`

Run `compute_image_mean path/to/created_lmdb data/ilsvrc12/imagenet_mean.binaryproto`

imagenet_mean.binaryproto is the mean image file we need.

### Training

use `models/trial_model_1/train.sh` to train with caffe

make sure the paths are all correct in  
`models/trial_model_1/train.sh`,  
`models/trial_model_1/prototxt/solver.prototxt`, and  
`models/trial_model_1/prototxt/train_val_trial.prototxt`
