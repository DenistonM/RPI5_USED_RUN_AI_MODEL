Running a TensorFlow Lite Model on Raspberry Pi

This repository provides step-by-step instructions for setting up and running a .tflite model on a Raspberry Pi.

Step 1: Connect to Raspberry Pi via SSH over Wi-Fi

Before running any commands, we need to connect to the Raspberry Pi (RPi) via SSH.

I am using the **Advanced IP Scanner** application to find the Raspberry Pi's IP address. Both my Raspberry Pi and laptop are connected to the same Wi-Fi network.

After finding the Raspberry Pi's IP address using Advanced IP Scanner, I open **PuTTY** and enter the IP address to establish an SSH connection.

Once the connection is established, I can execute commands remotely to install the required dependencies and configure the Raspberry Pi to run the `.tflite` model.

1. Update the Pi
bash

sudo apt update && sudo apt full-upgrade -y
sudo reboot

2. Install system packages
bash

sudo apt install -y python3-pip python3-venv python3-dev git \
  libgl1 libglib2.0-0 libjpeg-dev libopenblas-dev \
  python3-picamera2 rpicam-apps

3. Create the project folder and virtual environment
bash

mkdir ~/photo-ai && cd ~/photo-ai
python3 -m venv venv --system-site-packages
source venv/bin/activate

4. Install Python packages
bash

pip install --upgrade pip
pip install ultralytics opencv-python-headless pillow numpy
pip install ai-edge-litert pillow numpy

5. Check the installation and the Pi
bash

python -c "import torch, cv2, ultralytics; print('torch', torch.__version__); print('opencv', cv2.__version__); print('ultralytics', ultralytics.__version__)"
uname -m
df -h /
rpicam-hello --list-cameras


Step 2: Access Raspberry Pi Files Remotely Using WinSCP

After installing the required dependencies, I use WinSCP to access the Raspberry Pi's files and folders remotely via SSH.

WinSCP allows me to browse the Raspberry Pi's file system, transfer files between my laptop and the Raspberry Pi, and edit files directly on the Raspberry Pi when required.


Step 3: Create a Python Script and Transfer the Image Folder

I use Bash commands in the Raspberry Pi's SSH terminal to create a Python script. Then, I use WinSCP to transfer the image folder from my laptop to the Raspberry Pi.

bash

nano predict.py


