class PlayList: 
    def __init__(self,songs):
        self.songs = songs
       

    def add_song(self,songs):
        self.songs.append("song")
    def __len__(self):
        return len(self.songs)
    def __str__(self):
        return f"Playlist with {len(self.songs)} songs"


myPlaylist = PlayList(["song1","song2","song3"])



print(str(myPlaylist))