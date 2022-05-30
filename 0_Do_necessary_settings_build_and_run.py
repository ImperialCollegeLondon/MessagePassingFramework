import os
import sys

my_python_path = sys.executable

# If nvidia-docker is not installed, raise an error.
if os.system("which nvidia-docker") == 256:
    raise Exception("nvidia-docker is not installed. Please install it first.")

os.system(my_python_path + ' -m pip install tqdm')
os.system(my_python_path + ' 1_Download_files.py')
os.system(my_python_path + ' 2_Switch_module_activation_and_assign_gpus.py --pose F:0 --object T:0 --hand F:0 --gaze F:0') ##Activate:T/F, gpu_id:0/1
os.system(my_python_path + ' 3_Switch_subscriber_activation.py --pose F --object T --hand F --integration F --MPF F') ##Activate:T/F
os.system(
    'make build '
    '&& MPF_REALSENSE_ON=TRUE '   # Switch this to 'FALSE' to turn off realsense
    'make run MPF_REPO_PATH="{}"'.format(os.getcwd()))
