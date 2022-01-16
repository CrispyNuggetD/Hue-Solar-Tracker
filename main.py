import urllib.request, json
import time

from datetime import datetime
from uploaddata import *

print('\n\n\n' + "Project Booted..." + '\n\n')
print("Hue Solar Tracker." + '\n')
#print (u"\U0001F12F")


print("A project by Christopher Nah." + '\n' + "Find me on https://github.com/CrispyNugget" + '\n')
print('''
This file is part of Hue Solar Tracker.

Hue Solar Tracker is free software: you can redistribute it and/or modify it under the terms of the Affero GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Hue Solar Tracker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Affero GNU General Public License for more details.

You should have received a copy of the Affero GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>.
''' + '\n\n\n')


seconds = 10
start_time = time.time()

display_now = datetime.now()
now_time = display_now.strftime("%H:%M:%S")
print("The time now is: " + now_time)


current_second = display_now.strftime("%S")
print("Current second: " + current_second)


shift_time = seconds - (int(current_second) % seconds)
print("Time to shift: " + str(shift_time))

shifted_seconds = int(current_second) + shift_time

current_hour_minute = display_now.strftime("%H:%M")
shifted_time = current_hour_minute + ":" + str(shifted_seconds)
print("Shifted time: " + str(shifted_time))



print("Data collection will start in " + str(shift_time) + " seconds, and will run every " + str(seconds) + " seconds starting from: " + str(shifted_time))


#initialise variables
initiallux = None


while True:
	programme_time = time.time() 
	elapsed_time = programme_time %seconds

	if elapsed_time == 0:
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")

		huejson = urllib.request.urlopen("http://192.168.1.148/api/fuCiYONTB9Xmc2fmVkUOJFZovVgzn29iO9aT7ZoQ/sensors/56")
		text = json.load(huejson)

		lux = text['state']['lightlevel']
		print("Live Update: The current outdoor Lux is: " + str(lux) + ", at " + str(current_time))
		
		if lux != initiallux:
			print("Live Update: Lux change detected. Uploading data...")
			sentence = str("Live Update: The current outdoor Lux is: " + str(lux) + ", at " + str(current_time))
			uploadlux(sentence)

			initiallux = lux


