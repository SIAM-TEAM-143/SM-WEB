import os
import platform
import time
import sys

# প্লাটফর্ম আর্কিটেকচার চেক
arch = platform.architecture()[0]

if arch == '64bit':
    os.system('git pull')
    os.system('clear')
    print('[•] YOUR DEVICE IS 64 BIT')
    time.sleep(2)

    try:
        from smweb import smweb
        smweb()
    except ImportError as e:
        print(f"[!] Import Error: {e}")
        print("[!] smweb.so ফাইলটি সঠিকভাবে compile হয়নি অথবা Python version mismatch.")
        sys.exit(1)

elif arch == '32bit':
    os.system('git pull')
    os.system('clear')
    print('[•] YOUR DEVICE IS 32 BIT')
    time.sleep(2)

    try:
        from smweb import smweb
        smweb()
    except ImportError as e:
        print(f"[!] Import Error: {e}")
        sys.exit(1)

else:
    print("[!] Unknown architecture!")

os.system('clear')
print('\x1b[1;97m Soon Your Device Supported Tools ')
