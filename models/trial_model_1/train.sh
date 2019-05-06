#!/bin/bash
caffe train --solver=/home/aimladmin/liyao_workspace/dlcity/models/trial_model_1/prototxt/solver.prototxt \
--weights /home/aimladmin/liyao_workspace/dlcity/models/VGG_ILSVRC_19_layers.caffemodel \
2>&1 | tee /home/aimladmin/liyao_workspace/dlcity/models/trial_model_1/logs/trial_model_1.log