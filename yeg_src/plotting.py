import pandas as pd
from matplotlib import *
from matplotlib.pyplot import *

train_log = pd.read_csv(r"H:\workspace\dlcity\models\trial_model_1\logs\trial_model_1.log.train",delim_whitespace=True)
test_log = pd.read_csv(r"H:\workspace\dlcity\models\trial_model_1\logs\trial_model_1.log.test",delim_whitespace=True)
_, ax1 = subplots(figsize=(15, 10))
ax2 = ax1.twinx()
ax1.plot(train_log["#Iters"], train_log["TrainingLoss"], alpha=0.4)
ax1.plot(test_log["#Iters"], test_log["TestLoss"], 'g')
ax2.plot(test_log["#Iters"], test_log["TestAccuracy"], 'r')
ax1.set_xlabel('iteration')
ax1.set_ylabel('train loss')
ax2.set_ylabel('test accuracy')
savefig("./train_test_image.png") #save image as png