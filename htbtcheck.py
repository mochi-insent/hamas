from asyncio import subprocess
import time
import subprocess
from hamadasConfigure import hamasconf

path = hamasconf.path

try:
    while True:
        time.sleep(0.5)
        u = time.time()
        f = open(path, 'r')
        t = float(f.read())
        if u - t > 60:
            subprocess.run(["python", "hamadasRefFileVer_tamesi.py"], check=True)
except KeyboardInterrupt:
    pass
