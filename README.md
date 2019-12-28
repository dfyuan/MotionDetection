# MotionDetection(In need of a new RPI3 B+)

**Help needed!** I am currently in need of a new RPI because the board that I currently have is now broken. I am in the middle of working on a UI to help the user configure the system. Help getting a new board would be much appreciated! You can donate to the paypal link that I have included below, send me a board, or any other way you might be able to help me achieve this goal. 

>
**Description:**  This system is called MotionDetection and it monitors motion from a USB webcam and Raspberry Pi 3 using the OpenCV API. Once motion is detected by the system, it takes a picture of what set the motion detection software off and E-mails that picture to you. It also affords the ability to remotely view that webcam from an android app from anywhere in the world at anytime. So after you’re notified via E-mail, then you have the option of checking the camera’s live feed if you’d like. This system is highly configurable and stable! Donate [here](https://paypal.me/motiondetection) if you'd like. You can contact me via E-mail if you have any questions at amboxer21@gmail.com.

A video demo can be found [HERE](https://www.youtube.com/watch?v=ZDyZsqIcBnk).

An image of my RPI3 can be found [HERE](https://drive.google.com/open?id=11fAc2o3DcJfO78mSmx6JLptXjQdwnBMb).

**DISCLAIMER:** Building the system can be very difficult and extremely complex. Some have tried but so far all have failed. I am willing to provide an image of my RPI3 on an SD card or you can DD the image from the link above. E-mail Anthony Guevara at amboxer21@gmail.com with any questions and I will be more than glad to help out.

### [Build Options]

#### **CMAKE BUILD OPTIONS FOR OpenCV:** 

```python
sudo cmake -DCAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DINSTALL_PYTHON_EXAMPLES=ON -DWITH_V4L=ON -DWITH_OPENGL=ON -DWITH_QT=OFF -DOPENCV_EXTRA_MODULES_PATH=/usr/src/opencv_contrib/modules -DBUILD_EXAMPLES=ON -DARCH=ARMV7 .. && sudo make -j3
```

#### **CMAKE BUILD OPTIONS for OpenCV on my Gentoo box**
```python
sudo cmake -DCAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local/opencv-3.4.3 -DINSTALL_PYTHON_EXAMPLES=ON -DWITH_V4L=ON -DWITH_OPENGL=ON -DWITH_OPENCL=OFF -DWITH_VTK=OFF -DWITH_QT=OFF -DOPENCV_EXTRA_MODULES_PATH=/usr/src/opencv_contrib/modules -DBUILD_EXAMPLES=ON -DARCH=ARMV7 .. && sudo make -j3
```

#### **FFMpeg configure options**

```python
sudo ./configure --enable-libv4l2 --enable-opengl --enable-libmp3lame
```

> **NOTE** ^^ The above build depends on OpenCV being built with the build3.4(NOT MASTER) branch of the opencv_contrib repo before OpenCV is built!! Download links can be found further down.

### [System Component Versions]

#### **SYSTEM OS VERSION**

```python
pi@raspberrypi:~/Documents/Python/MotionDetection $ readarray -t a < <(lsb_release -irs); echo "${a[@]}"
```

>Raspbian 8.0

#### **GCC VERSION**

```python
pi@raspberrypi:~/Documents/Python/MotionDetection $ dpkg -s gcc | grep ^Version
```

>Version: 4:4.9.2-2

#### **CMAKE VERSION**

```python
pi@raspberrypi:~/Documents/Python/MotionDetection $ cmake --version
```

>cmake version 3.5.1

#### **OpenCV System VERSION**

```python
aguevara@anthony ~ $ opencv_version 
```

>2.4.13.6

#### **OpenCV Python VERSION**

```javascript
pi@raspberrypi:~ $ python -c 'import cv2; print(str(cv2.__version__))'
```
>3.1.0

#### **FFMPEG VERSION**

```python
pi@raspberrypi:~/Documents/Python/MotionDetection $ ffmpeg -version
```

```python
ffmpeg version 3.4.5 Copyright (c) 2000-2018 the FFmpeg developers
built with gcc 4.9.2 (Raspbian 4.9.2-10+deb8u1)
configuration: --enable-libmp3lame --enable-libv4l2 --enable-opengl
libavutil      55. 78.100 / 55. 78.100
libavcodec     57.107.100 / 57.107.100
libavformat    57. 83.100 / 57. 83.100
libavdevice    57. 10.100 / 57. 10.100
libavfilter     6.107.100 /  6.107.100
libswscale      4.  8.100 /  4.  8.100
libswresample   2.  9.100 /  2.  9.100
```

#### ** BUILT WITH:**

>ffmpeg-3.4.5

>cmake version 3.5.1

>opencv-2.4.13.6

>opencv-3.1.0

>opencv_contrib-3.4

### [Download Links]

[FFMPEG 3.4.5](https://www.ffmpeg.org/releases/ffmpeg-3.4.5.tar.gz)

[CMake 3.5.1](https://github.com/Kitware/CMake/releases/download/v3.5.1/cmake-3.5.1.tar.gz)

[OpenCV 2.4.13.6](https://github.com/opencv/opencv/archive/2.4.13.6.zip)

[OpenCV 3.1.0](https://github.com/opencv/opencv/archive/3.1.0.zip)

[OpenCV open_contrib 3.4](https://github.com/opencv/opencv_contrib/tree/3.4)

### [DEPS]

**Debian:**

```python
sudo apt-get install build-essential pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev libv4l-dev libxvidcore-dev libx264-dev libgtk2.0-dev libatlas-base-dev gfortran python2.7-dev python3-dev 
```

**RHEL:**

```python
...
```

### [DEMO]

Here is an older(but still relevant) [video](https://www.youtube.com/watch?v=ZDyZsqIcBnk) demonstrating the program. Which can also be found at the top of this page.

### [SCREEN SHOTS]

> **MotionDetection System**

![alt text](https://github.com/amboxer21/MotionDetection/blob/master/src/screenshots/Screenshot_20181119-171140_scaled-250x500.png)
![alt text](https://github.com/amboxer21/MotionDetection/blob/master/src/screenshots/Screenshot_20181119-171159_scaled-250x500.png)
![alt text](https://github.com/amboxer21/MotionDetection/blob/master/src/screenshots/Screenshot_20181119-171209_scaled-250x500.png)
