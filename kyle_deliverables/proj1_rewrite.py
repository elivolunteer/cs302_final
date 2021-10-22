# define classes
class Song:
    def __init__(self, title, time, track):
        self.title = title
        self.time = time
        self.track = track


class Album:
    def __init__(self, songs, name, time, nsongs):
        self.songs = {}
        self.name = name
        self.time = time
        self.nsongs = nsongs

class Artist:
    def __init__(self, albums, name, time, nsongs):
        self.albums = {}
        self.name = name
        self.time = time
        self.nsongs = nsongs

# get filename from user
print("Please enter the file name: ")
fileName = input()

#open(fileName, "r")

# open and read the file
with open(fileName) as f:
    content = f.readlines()

# initialize a dictionary of artists
artists = {}

# split the lines by spaces, assign to proper variable
for line in content:
    
    # split the line
    line = line.replace("\n","")
    word = line.split(" ")

    title = word[0].replace("_", " ")

    # change time to seconds as an int
    time_str = word[1].replace(":", "")
    minutes = int(time_str[0])
    tens = int(time_str[1])
    ones = int(time_str[2])
    seconds = (minutes * 60) + (tens * 10) + (ones)

    artist_str = word[2].replace("_", " ")

    album_str = word[3].replace("_", " ")

    genre = word[4]

    track_int = int(word[5])

    # song instance for adding to dictionaries later
    toAdd = Song(title, seconds, track_int)

    #if artist is not already in the map, add
    if not artists.get(artist_str):
        artist_tmp = Artist({}, artist_str, 0, 0)
        artists[artist_str] = artist_tmp

    #if album not already in the map, add
    if not artists[artist_str].albums.get(album_str):
        album_tmp = Album({}, album_str, 0, 0)
        artists[artist_str].albums[album_str] = album_tmp

    # #if song not already in the map, add
    if not artists[artist_str].albums[album_str].songs.get(track_int):
        artists[artist_str].albums[album_str].songs[track_int] = toAdd

        # tack on time and nsongs to upper level dictionaries
        artists[artist_str].albums[album_str].time += toAdd.time
        artists[artist_str].albums[album_str].nsongs += 1
        artists[artist_str].time += toAdd.time
        artists[artist_str].nsongs += 1
    
sorted(artists)

# nested for loops for printing data
for key in artists:

    # convert time back to mm:ss
    artTimeStr = ''
    artTimeStr += str(artists[key].time // 60) + ":"
    if artists[key].time % 60 < 10:
        artTimeStr += "0" + str(artists[key].time % 60)
    else:
        artTimeStr += str(artists[key].time % 60)

    # print artist piece
    print(artists[key].name + ":" + " " + str(artists[key].nsongs) + ", " + artTimeStr)
    sorted(artists[key].albums)

    for key1 in artists[key].albums:

        # convert time back to mm:ss
        albTimeStr = ''
        albTimeStr += str(artists[key].albums[key1].time // 60) + ":"
        if artists[key].albums[key1].time % 60 < 10:
            albTimeStr += "0" + str(artists[key].albums[key1].time % 60)
        else:
            albTimeStr += str(artists[key].albums[key1].time % 60)

        # print album piece
        print("    " + artists[key].albums[key1].name + ": " + albTimeStr)

        sorted(artists[key].albums[key1].songs)

        for key2 in artists[key].albums[key1].songs:

            # convert time back to mm:ss
            songTimeStr = ''
            songTimeStr += str(artists[key].albums[key1].songs[key2].time // 60) + ":"
            if artists[key].albums[key1].songs[key2].time % 60 < 10:
                songTimeStr += "0" + str(artists[key].albums[key1].songs[key2].time % 60)
            else:
                songTimeStr += str(artists[key].albums[key1].songs[key2].time % 60)

            # print songs piece
            print("        " + str(artists[key].albums[key1].songs[key2].track) + ". " + artists[key].albums[key1].songs[key2].title + ": " + songTimeStr)
            
# close the file
f.close