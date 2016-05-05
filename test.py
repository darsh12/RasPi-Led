import RPi.GPIO as GPIO;
import random;
import time;

GPIO.setmode(GPIO.BOARD);

#Dictionary for GPIO pins
#Maped as 'Breadboard pins: GPIO pins'
led={17:11, 18:12, 27:13, 22:15};

#Get all values from the led dictionary
pin=led.values()


#Set specified GPIO pins as output
def output():
    GPIO.setup(pin,GPIO.OUT);
    print "Pin's active: %s" % (pin);

"""
  GPIO.setup(17,GPIO.OUT);
  GPIO.setup(18,GPIO.OUT);
  GPIO.setup(22,GPIO.OUT);
  GPIO.setup(27,GPIO.OUT);
"""

#Starts random leds
def randomLed():
  output();
#Switches on and off random led until user ends 
  while True:
    x=random.choice(pin);
    y=random.choice(pin);
    if(x!=y):
      GPIO.output(x,GPIO.HIGH);
      print"This is x: %s" % x;
      GPIO.output(y,GPIO.HIGH);
      print"This is y: %s" % y;
      time.sleep(0.15);
      GPIO.output(x,GPIO.LOW);
      GPIO.output(y,GPIO.LOW);
      pass; #End if
    pass; #End while

#Start all leds
def allLed():
  output();
#Instantiate the leds then enters the while loop for further processing
  GPIO.output(pin,GPIO.HIGH);
  print "All led: %s" %(pin);

#While loop until user stops the process
  while True:
    time.sleep(5);
    GPIO.output(pin,GPIO.HIGH);
    print "All led: %s" %(pin);
    pass;

def singleLed():
  output();
  
  all=False;
  while True:
#TODO implemet a While loop
	  for x in led:
	    test=led.get(x);
	    GPIO.output(test,GPIO.HIGH);
	    print ("Single led: %s" %(test));
	    time.sleep(1);
	    all = True;

	  if(all==True):
	    print ("Leds shutting down");
	    for i in led:
	      alpha=led.get(i);
	      GPIO.output(alpha,GPIO.LOW);
	      print ("Shutting led: %s" %(alpha));
	      time.sleep(1);
	  pass

def trafficLight():
	output();

	red=led.get(17);
	yellow=led.get(18);
	green=led.get(27);

	while True:
		GPIO.output(red,GPIO.HIGH);
		time.sleep(1.5);
		GPIO.output(red,GPIO.LOW);
		time.sleep(1.5);
		GPIO.output(yellow,GPIO.HIGH);
		time.sleep(1.5);
		GPIO.output(yellow,GPIO.LOW);
		time.sleep(1.5);
		GPIO.output(green,GPIO.HIGH);
		time.sleep(1.5);
		GPIO.output(green,GPIO.LOW);
		pass;#end if

#Stop all leds
def stopLed():
  output();
  print("Stopping leds");
  GPIO.output(pin,GPIO.LOW);

#On input start defined method
def selection(input):
  """
  switcher = {1:randomLed(), 2:allLed()};
  return (switcher.get(input, "Wrong selection"));
  """
  if (input == "1"):
    randomLed();
  elif(input == "2"):
    allLed();
  elif(input =="3"):
    singleLed();
  else:
    print"Wrong input";
    pass; #End if


def userInterface(): 
  try:
    #Print the functions available 
    list=["Enter '1' for random leds", "Enter '2' for all leds", "Enter '3' for single leds"];
    for list in list:
      print "%s" %(list);

    #Asks user for input and goes through loop until user inputs 'End' or the correct input
    while True:
      ans = raw_input("Input selection: ");
      if (ans == "End"):		#MOVE TO 'SELECTION'
        print "Exiting from system";
        stopLed();
        time.sleep(3);
        break;
      else:
        selection(ans);
        break;
        pass; #End if
      pass; #End while
    pass; #End try
  except KeyboardInterrupt, e:
    print "\nProcess stopped";
    print "Led's shutting down";
    time.sleep(1.5);
    stopLed();

    #TODO close specific GPIO

    #raise e;

#userInterface();
trafficLight();
#stopLed();

