from pytube import YouTube
from datetime import datetime
import urllib
import json
import os
import vlc
import time
import re
import cec

api_key = ''
channel_id = ''

def TV_On():
    cec.init()
    TV = cec.Device(0)
    SoundSystem = cec.Device(5)
    SoundSystem.power_on()
    time.sleep(3)
    TV.power_on()
    time.sleep(1)
    return

def TV_Off():
    SoundSystem = cec.Device(5)
    TV = cec.Device(0)
    TV.standby()
    SoundSystem.standby()
    return

def Play_News():
    print('SEND IT')
    TodaysLineup = open("TodaysLineup","r")
    VideoTitles = TodaysLineup.read().splitlines()
    VideoTitles.pop(0)
    vlc_instance = vlc.Instance(['--video-on-top'])
    player = vlc_instance.media_player_new()
    player.set_fullscreen(True)
    TV_On()
    for VideoTitle in VideoTitles:
        try:
            VideoTitle = re.sub(r'[\\/*?:"\'<>,|$]','',VideoTitle)
            Filename = 'VideoCache/{}.mp4'.format(VideoTitle)
            Video = vlc_instance.media_new(Filename)
            player.set_media(Video)
            player.play()
            time.sleep(1)
            duration = (player.get_length() / 1000)
            #if(duration > 20):
            #    duration = duration - 20
            time.sleep(duration)
            time.sleep(5)
            os.remove(Filename)
        except: 
            pass
    TV_Off()
    return    


def Prep_News():
    Clear_TodaysLineup()
    TodaysLineup = []
    Latest_IG_Links = Get_LatestEp(api_key,channel_id)
    Latest_IG_VidInfos = Get_VideoInfo(Latest_IG_Links)
    for Latest_IG_VidInfo in Latest_IG_VidInfos:
        if(Check_WatchedLog(Latest_IG_VidInfo) == 0):
            Download_Video(Latest_IG_VidInfo)
            #Log = open("./WatchedLog","a")
            #Log.write('\r\n')
            #Log.close()
            Log_VideoWatched(Latest_IG_VidInfo.title)    
            TodaysLineup.append(Latest_IG_VidInfo)
    Set_TodaysLineup(TodaysLineup)
    return

# -- GET THE 3 LATEST EPISODES FROM CHANNEL --
def Get_LatestEp(api_key,channel_id):
    print('\r\nLet\'s get the newest IG episodes')
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
    url = first_url
    video_links = []

    print('== You better watch this news if I\'m doing all this urllib work on it')
    inp = urllib.urlopen(url)
    resp = json.load(inp)
    count = 0;
    print('== Time to HACK')
    for i in resp['items']:
        if i['id']['kind'] == "youtube#video":
            video_links.append(base_video_url + i['id']['videoId'])
            print('==== Got one! %s' % video_links[count])
            count = count + 1
        if count > 2:
            break

    return(video_links)

# -- GET VIDEO INFO FROM LINKS --
def Get_VideoInfo(video_links):
    print('\r\nGet some sweet deets on them vids bro')
    YTObjs = []
    for video_link in video_links:
        print('==== loading %s ...' % video_link)
        YTObj = YouTube(video_link)
        print('==== Got \'em! | {}'.format(YTObj.title))
        YTObjs.append(YTObj)
    return(YTObjs)

# -- DOWNLOAD VIDEO -- 
def Download_Video(YTObj):
    print('\r\nCan\'t complain about buffering if it\'s downloaded')
    stream = YTObj.streams.first()
    File = stream.download('./VideoCache')
    print('== I\'m sure you\'ll find a way tho')
    return(File)

# -- LOG VIDEO AS WATCHED --
def Log_VideoWatched(title):
    print('\r\nNow to log this shit')
    datestamp = datetime.today().strftime('%m-%d-%Y')
    logline = '{} | {}'.format(datestamp,title)
    try:
        print('== Slipping into that file for ya')
        Log = open("./WatchedLog","a")
        Log.write('{}\r\n'.format(logline))
        Log.close()
    except:
        print('== Sorry bud, I couldn\'t get into the log file')

# -- CHECK AGAINST WATCHED LOG -- 
def Check_WatchedLog(YTObj):
    print('\r\nMaking sure you don\'t rewatch {}'.format(YTObj.title))
    print('== I\'d hate for you to see it again')
    watched = 0
    try:
        with open("WatchedLog") as Log:
            if YTObj.title in Log.read():
                print('== Wait a minute... You\'ve seen this before')
                watched = 1
                print('== Annihilating video')
            else:
                print('== mmm... fresh')
            Log.close()
    except:
        print('== Whoopsie Doodle. Couldn\'t hack that log')
    return(watched)

# -- INITIALIZE TODAY'S LINEUP --
def Clear_TodaysLineup():
    print('\r\nGiving this script a digital ass-wiping')
    try:
        open('./TodaysLineup','w').close()
        print('== Squeaky Clean')
    except:
        print('== ASSHOLE STILL DIRTY')
        os.remove("./TodaysLineup")
        print('== RECT(UM)FYING')
        open('./TodaysLineup','w+').close()
        print('== Hope to god that worked...')
    return

# -- ADD TO TODAY'S LINEUP --
def Set_TodaysLineup(files):
    print('\r\nQueuing up your well balanced news')
    try:
        TodaysLineup = open("./TodaysLineup",'w')
        for video in files:
            TodaysLineup.write('\r\n{}'.format(video.title))
        print('== Locked and loaded')
        TodaysLineup.close()
    except:
        print('== Python is awful at opening text files')
        TodaysLineup = open("./TodaysLineup",'w+')
        for video in files:
            TodaysLineup.write('\r\n{}'.format(video.title))
        print('== Don\'t do Python kids')
    return



