""">>>
This script will create a simple alarm clock that is configurable, and plays a sound at a specified time.
I was having trouble with generating a nice sounding tone, so I ended up with white noise which is a bit... jumpscare-like.
"""

import datetime
import math
import time
import pyaudio
import random

class AlarmClock:
    """>>>
    This class will store a time and a sound file to be played.
    """
    def __init__(self, time : datetime.datetime):
        """>>>
        Ignore seconds in time
        """
        self.time = time.replace(second=0, microsecond=0)
        #>>> print the time
        print("Alarm set for {}:{}".format(self.time.hour, self.time.minute))

    def set_alarm(self, target_time: datetime.time):
        """>>>
        This method will set the alarm clock to the time specified, overwriting whatever it was before. Ignore seconds in time.
        """
        self.time = target_time.replace(second=0, microsecond=0)
        # print the time
        print("Alarm set for {}:{}".format(self.time.hour, self.time.minute))

    def play_alarm(self):
        """>>>
        play white noise for 1 second using pyaudio. The white noise is also generated in this method by generating random values between 0 and 255 (integer values, converted to bytes-like).
        """
        # define the output audio stream
        p = pyaudio.PyAudio()
        # define the output stream
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
        # generate the white noise
        white_noise = [random.randint(0,255) for i in range(44100)]
        # play the white noise
        stream.write(bytes(white_noise))
        # close the stream
        stream.close()
        # close the PyAudio session
        p.terminate()
        


        
    
    def wait_for_time(self):
        """>>>
        This method will wait until the time specified is reached. After that it will play the sound file. Prints information regarding this method being called. Prints time remaining every 1 second. Each print should end with a \r
        """
        # get the current time
        current_time = datetime.datetime.now()
        # calculate the time remaining
        time_remaining = (self.time - current_time).total_seconds()
        # print the time remaining
        print("\rTime remaining: {}".format(time_remaining), end="")
        # wait for the time remaining to be less than 0
        while time_remaining > 0:
            # print the time remaining
            print("\rTime remaining: {}".format(time_remaining), end="")
            # wait 1 second
            time.sleep(1)
            # get the current time
            current_time = datetime.datetime.now()
            # calculate the time remaining
            time_remaining = (self.time - current_time).total_seconds()
        # play the sound file
        self.play_alarm()
        

#>>> if main script is run, run the following
if __name__ == "__main__":
    #>>> save current time in current_time
    current_time = datetime.datetime.now()
    #>>> save current time plus 1 minutes into target_time
    target_time = current_time + datetime.timedelta(minutes=1)
    #>>> create alarm clock object
    alarm_clock = AlarmClock(current_time)
    #>>> set the alarm clock to the target time
    alarm_clock.set_alarm(target_time)
    #>>> wait for target time
    alarm_clock.wait_for_time()
    



