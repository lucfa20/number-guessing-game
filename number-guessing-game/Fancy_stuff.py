import time,os,sys

def typingPrint(text, interval=0):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(interval)

def typingInput(text, interval=0):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(interval)
  value = input()  
  return value  

def clearScreen():
  os.system("cls")

