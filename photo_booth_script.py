#!/usr/bin/python

import RPi.GPIO as GPIO, time, os, subprocess 


# GPIO setup
GPIO.setmode(GPIO.BCM)
SWITCH = 24
GPIO.setup(SWITCH, GPIO.IN)
#RESET = 25
#GPIO.setup(RESET, GPIO.IN)
PRINT_LED = 22
POSE_LED = 18
BUTTON_LED = 23
GPIO.setup(POSE_LED, GPIO.OUT)
GPIO.setup(BUTTON_LED, GPIO.OUT)
GPIO.setup(PRINT_LED, GPIO.OUT)
GPIO.output(BUTTON_LED, True)
GPIO.output(PRINT_LED, False)

while True:
  if (GPIO.input(SWITCH)):
    snap = 0
    GPIO.output(BUTTON_LED, False)
    while snap < 4:
      print("Pose!")
      subprocess.call("feh -F --cycle-once --slideshow-delay 1 /home/pi/AwesomePhotobooth/PB_archive/" + str(snap), shell=True)
      #print("SNAP")
      gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/AwesomePhotobooth/TempPhotoBooth/photobooth%H%M%S.jpg", stderr=subprocess.STDOUT, shell=True)
      #print(gpout)
      if "ERROR" not in gpout: 
        snap += 1
      GPIO.output(POSE_LED, False)
      time.sleep(0.1)
    print("And a little magic...")
    GPIO.output(PRINT_LED, True)
    #subprocess.call("feh -F -x --cycle-once --slideshow-delay 12 /home/pi/AwesomePhotobooth/PB_archive/1.png", shell=True)
    #time.sleep(0.5)
    #GPIO.output(PRINT_LED, False)

    subprocess.call("sudo /home/pi/AwesomePhotobooth/scripts/assemble_and_save", shell=True)

    subprocess.call("feh -F --cycle-once --slideshow-delay 8 /home/pi/AwesomePhotobooth/TempMontage/temp_montage2.jpg*", shell=True)
    subprocess.call("feh -F -s --cycle-once --slideshow-delay 3 /home/pi/AwesomePhotobooth/ImageStock/ThankYou.png", shell=True)
    
    #GPIO.output(PRINT_LED, False)
    #time.sleep(0.2)
    #subprocess.call("rm /home/pi/AwesomePhotobooth/PB_archive/*.jpg", shell=True)
    # TODO: implement a reboot button
    # Wait to ensure that print queue doesn't pile up
    # TODO: check status of printer instead of using this arbitrary wait time
    #time.sleep(10)


    print("Press to start!")
    GPIO.output(PRINT_LED, False)
    GPIO.output(BUTTON_LED, True)
