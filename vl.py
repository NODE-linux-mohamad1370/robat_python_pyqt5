import vlc
player=vlc.MediaPlayer('rtsp://admin:1030@192.168.1.20:80/cam/realmonitor?channel=2&subtype=0')
player.play()
 
while(1):
 continue