import os

os.system('pip install tqdm')
os.system('pip3 install tqdm')
os.system('python 1_Download_files.py')
os.system('python 2_Switch_module_activation_and_assign_gpus.py --pose F:0 --object F:0 --hand F:0 --gaze T:0') ##Acvitate:T/F, gpu_id:0/1
os.system('python 3_Replace_perception_folder_path_in_Makefile.py')
os.system('make build && make run')
