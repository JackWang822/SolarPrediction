# -*- coding: utf-8 -*-
__author__= 'WANG Kejie<wang_kejie@foxmail.com>'
__date__ = '10/12/2016'

"""
This file is used to generate the train, test and validation dataset
from the NREL_BMS_SKY_CAM dataset
"""

import numpy as np
import sys
import os
import time
HOUR_IN_A_DAY = 24

data_path = "pad_data_path.csv"

validation_day_num = 365
test_day_num = 366

if len(sys.argv) != 2:
	print "Error: please input the train and validation set prop, e.g. python generate.py 200011201205"
	exit(0)

data_dir = sys.argv[1] + "/"

#load the data
sky_cam_data = np.loadtxt(data_dir + "pad_data_path.csv", delimiter=',')

data_hour_length = len(sky_cam_data)
validation_length = validation_day_num * HOUR_IN_A_DAY
test_length = test_day_num * HOUR_IN_A_DAY
train_length = data_hour_length - validation_length - test_length

sky_cam_train_data = sky_cam_data[0:train_length]
sky_cam_validation_data = sky_cam_data[train_length:train_length+validation_length]
sky_cam_test_data = sky_cam_data[train_length+validation_length:]

if not os.path.exists('./train/'):
	os.mkdir('./train/')
if not os.path.exists('./validation/'):
	os.mkdir('./validation/')
if not os.path.exists('./test/'):
	os.mkdir('./test/')

#save the data
np.savetxt('./train/sky_cam_train_data.csv', sky_cam_train_data, fmt='%.4f', delimiter=',')
np.savetxt('./validation/sky_cam_validation_data.csv', sky_cam_validation_data, fmt='%.4f', delimiter=',')
np.savetxt('./test/sky_cam_test_data.csv', sky_cam_test_data, fmt='%.4f', delimiter=',')

#generate a README
with open('README', 'w') as fp:
	fp.write("SUMMARY\n")
	fp.write("="*80)
	fp.write("\n\n")

	fp.write("This is an auto generate file by the pre-process file\n")
	fp.write("author: WANG Kejie<wang_kejie@foxmail.com>\n")
	fp.write("Generating time:"+time.strftime('%Y-%m-%d %X', time.localtime())+"\n")
	fp.write("\n\n")

	fp.write("Dataset Info\n")
	fp.write("="*80 + "\n")
	fp.write("The excel file is the source dataset and use the preprocess python script to generate the train, validation and test data\n")
	fp.write("Train set data length: %d days / %d hours\n" %(train_length/HOUR_IN_A_DAY, train_length))
	fp.write("Validation set data length: %d days / %d hours\n" %(validation_length/HOUR_IN_A_DAY, validation_length))
	fp.write("Test set data length: %d days / %d hours\n" %(test_length/HOUR_IN_A_DAY, test_length))
