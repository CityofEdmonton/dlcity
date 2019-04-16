#!/bin/bash
caffe train --solver=/home/liyao_jiang/dlcity/models/trial_model_1/prototxt/solver.prototxt \
--weights /home/liyao_jiang/dlcity/models/VGG_ILSVRC_19_layers.caffemodel \
2>&1 | tee /home/liyao_jiang/dlcity/models/trial_model_1/logs/trial_model_1.log