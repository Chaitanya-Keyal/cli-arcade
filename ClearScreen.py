import os
from time import sleep
def cls():
   # for mac and linux (here, os.name is 'posix')
   if os.name == 'posix':
      os.system('clear')
   else:
      # for windows platfrom
      os.system('cls')
#sleep(3) # Wait time in seconds
cls()
