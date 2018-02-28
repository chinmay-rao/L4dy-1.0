from os import system
from difflib import get_close_matches
import pandas

def play_song(STRING):
    csv_path = 'songs.csv'
    db = pandas.read_csv(csv_path)
    song_dict = dict(zip(list(db.iloc[:,0]), list(db.iloc[:,1])))
    match_list = get_close_matches(STRING, song_dict.keys())
    
    song = str(match_list[0])
    song_path = song_dict[song]   
    print(song_path)
    #command = 'omxplayer -o local ' + song_path
    #system(command)
    
play_song("still breathing by green day")
