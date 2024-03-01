# Language Translation

This paper introduces a Raspberry Pi-based language translation system using the Google Translate API. The system captures user speech, translates it into a chosen language, and converts the translated text into speech. The implementation showcases the practicality of real-time multilingual communication on the Raspberry Pi, emphasizing its versatility and efficiency for compact language processing applications.

Detailed youtube Video explanation of how this works: https://youtu.be/FadNcNHQBHY?feature=shared

IEEE format Report of the project is attached as Report.pdf for complete overview of project. https://github.com/Barathj121/Language_Translation/blob/main/report.pdf



Before starting the project kindly install all the libraries given below

-->API setting:

pip install playsound==1.2.2 

pip install SpeechRecognition==3.8.1

pip install googletrans==4.0.0-rc1

pip install gTTS==2.2.3

pip install Pillow==8.4.0

pip install Adafruit-GPIO==1.1.2

pip install Adafruit-SSD1306==1.6.2

pip install Adafruit-Blinka==7.0.1




--> For setting up the display :
Python ST7735
Python library to control an ST7735 TFT LCD display. Allows simple drawing on the display without installing a kernel module.

Designed specifically to work with a ST7735 based 128x160 pixel TFT SPI display.

For all platforms (Raspberry Pi and Beaglebone Black) make sure you have the following dependencies:

sudo apt-get update

sudo apt-get install build-essential python-dev python-smbus python-pip python-pil python-numpy

For a Raspberry Pi make sure you have the RPi.GPIO and Adafruit GPIO libraries by executing:

sudo pip install RPi.GPIO

sudo pip install Adafruit_GPIO

For a BeagleBone Black make sure you have the Adafruit_BBIO library by executing:

sudo pip install Adafruit_BBIO

Install the library by downloading with the download link on the right, unzipping the archive, navigating inside the library's directory and executing:

sudo python setup.py install

Follow this github for more doubts regarding display : https://github.com/degzero/Python_ST7735/tree/master

--> Pin configuration to connect LCD display to Raspberry pi: 

![image](https://github.com/Barathj121/Language_Translation/assets/110909380/317cf5eb-ed8c-4cc0-8dbd-cb9d81b476a0)          ![image](https://github.com/Barathj121/Language_Translation/assets/110909380/e14aaeba-eba9-4597-ae82-b7a47bcd416c)

After Display has been set up connect the microphone to micro usb and speaker AUX cable 

Run S.py file and make sure other files are there in same folder.




