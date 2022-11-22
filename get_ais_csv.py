'''
Proof of concept to download files quickly from AIS from command line.
It only took about 30 seconds to get a 1GB sized file from AIS to our
DeepNote storage.
'''

import time
from datetime import timedelta
import subprocess
import datetime
import sys

data_source = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/"

print('Data source:', data_source)
print('Started download:', 
      datetime.datetime.now() - timedelta(hours=7), '\n')

start = time.time()

destination_path = "./data/"
filename = sys.argv[1]

s1 = time.time()
destination = destination_path + filename

print('Downloading "{}" to "{}"'.format(filename, destination))
subprocess.run(["curl", "-o", destination, data_source + filename])

print('  Unzipping...')
subprocess.run(["unzip", destination, "-d", destination_path])

print('  Deleting...')
subprocess.run(["rm", destination])

e1 = time.time()
print('  Elapsed:', str(timedelta(seconds=e1 - s1)))

end = time.time()

print("\nTotal time elapsed:", str(timedelta(seconds=end - start)))
print('Done downloading:', datetime.datetime.now() - timedelta(hours=7))

