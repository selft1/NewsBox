HEY HOW'S IT GOIN'?

First, just a note, I am a student in Computer Engineering with a focus in Software Engineering. I do very much enjoy software development
 but I am still a student and most of my experience is in C, Verilog, and PowerShell (PowerShell is a story for another time) so 
 let's try to keep any comments or criticisms constructive. This was also a quick side project for my own amusement so I'm sure there are
 plenty of flaws and inefficiencies in the code.

Anyway, on with the geeky stuff!

The idea is that this script will go to your favorite YouTube channel (I chose Inside Gaming) pick the 3 newest videos, check against
a log that is kept of videos from that channel that you've already watched to make sure it doesn't show you something twice, then download 
the videos that you haven’t seen, then turn on your tv and play them. Then finally log the videos as watched, delete the video files,
and turn off the tv. Again, this isn't perfect, and I'll list some bugs later (please don't hesitate to report them or send me your fix ideas)
in the Help.py file I've got global variables where you can add your YouTube API key and the channel id for your favorite channel. 

--The script is currently set to run at a given time. There are two timers, one to prep your videos to make sure they're downloaded
      ahead of time, and one to play the videos. I have mine set for the ungodly hours of 6am and 6:45am respectively. 
      This is set in the NewsBox.py file and the numbers should be fairly obvious. You can hard code these numbers in the lines. I may make this
      easier to change later. There's also an if statement that makes sure it doesn't wake you up on weekends, only weekdays

Some things you're going to need
  - a raspberry pi (preferably. I'm sure plenty of people will find uses for this without a pi)
  - a CEC enabled TV (this is how the raspberry pi will turn on your tv to show the videos and turn it off when it's done)
  - a YouTube API key. follow this: https://www.slickremix.com/docs/get-api-key-for-youtube/
  - the channel id of your favorite channel: https://commentpicker.com/youtube-channel-id.php
  - wherever you copy this repo to, also create a folder called VideoCache (github hates me and won't add that empty folder to the repo)

Some libraries you'll need
  - python-vlc https://wiki.videolan.org/PythonBinding
  - python-cec https://github.com/trainman419/python-cec
  - pytube https://github.com/trainman419/python-cec
  (please let me know if you have issues with these or find things are missing)
  
Some known bugs
  - I've had the script run and do everything exactly right but then leave a black VLC media player up. I didn't notice this until I
    checked the next day, because it turns off your tv when the video finishes playing. For some reason this causes the next video viewing
    session to not work right. This is probably my highest priority bug right now
  - Kind of a bug, king of a note, whenever a video starts I get 2 errors from pulseaudio. I've read up on it and its common and doesn't
    really mean anything since the audio still works fine so I'm choosing to ignore it and you should too
  - Sometimes when the video is cut off there is a high pitched sound left ringing until the tv is shut off. Probably related to the first
    bug I pointed out where VLC stays open
    
Things I hope to fix soon
  - Make sure VLC closes after video is done (check and log this)
  - allow for easier changes to channel, api key, and timers
  - create a backend GUI?
  - look into some overlays for optional weather and clock (this is because I use this in the morning and I'd like all that information
    in one place)
    
Feel free to email me any questions, suggestions, code improvements, or issues: tylerjayself@gmail.com
