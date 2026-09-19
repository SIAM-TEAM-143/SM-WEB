import os
import platform
import time
import smweb
os.system("pip install requests")
fuck = platform.architecture()[0]
if fuck == '64bit':
    os.system('git pull')
    os.system('clear')
    print('[•] YOUR DEVICE IS 64 BIT')
    time.sleep(2)
    from smweb import smweb
    smweb()
if fuck == '32bit':
    os.system('git pull')
    os.system('clear')
    print('[•] YOUR DEVICE IS 32 BIT')
    time.sleep(2)
    from smweb import smweb
    smweb() 
os.system('clear')
print('\x1b[1;97m Soon Your Device Supported Tools ')
 
