import RPi.GPIO as GPIO;
import random;
import time;

GPIO.setmode(GPIO.BCM);

#List fot GPIO pins
led=[17,18,22,27];

#Set specified GPIO pins as output
def output():
  for x in led:
    GPIO.setup(x,GPIO.OUT);
    print "This is: %s" % (x);
    pass; #End for

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
    x=random.choice(led);
    y=random.choice(led);
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
#For loop to instantiate the leds then enters the while loop for further processing
  for y in led:
      GPIO.output(y,GPIO.HIGH);
      print "All led: %s" %(y);
      pass;

#While loop until user stops the process
  while True:
    time.sleep(60);
    for x in led:
      GPIO.output(x,GPIO.HIGH);
      print "All led: %s" %(x);
      pass;
    pass;


#Stop all leds
def stopLed():
  output();

  for x in led:
    GPIO.output(x,GPIO.LOW);
    pass; #End for

def selection(input):

#Keys to be defined in strings
  """
  switcher = {1:randomLed(), 2:allLed()};
  return (switcher.get(input, "Wrong selection"));
  """

  if (input == "1"):
    randomLed();
  elif(input == "2"):
    allLed();
  else:
    print"Wrong input";
    pass; #End if


def userInterface(): 
  try:
    #Print the functions available 
    list=["Enter '1' for random leds", "Enter '2' for all leds"];
    for list in list:
      print "%s" %(list);

    #Asks user for input and goes through loop until user inputs 'End' or the correct input
    while True:
      ans = raw_input("Input selection: ");
      if (ans == "End"):
        print "Exiting from system";
        stopLed();
        time.sleep(3);
        break;
      else:
        print(selection(ans));
        pass; #End if
      pass; #End while
    pass; #End try
  except KeyboardInterrupt, e:
    stopLed();
    print "Process stopped";
    raise e;

userInterface();
