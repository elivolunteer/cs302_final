class Song:
    def __init__(self, title, time, track):
        self.title = title
        self.time = time
        self.track = track
#    title
#    time
#    track

#class Album:
#    songs = {}
#    name
#    time
#    nsongs
#class Artist:
#    albums = {}
#    name
#    time
#    nsongs

print("Please enter the file name: ")
fileName = input()

#open(fileName, "r")

with open(fileName) as f:
    content = f.readlines()

# split the lines by spaces, assign to proper variable
for line in content:
    line = line.replace("\n","")
    word = line.split(" ")
    #word = word.replace("_", " ")
    title = word[0].replace("_", " ")
    #title = title.replace("_", " ")
    time_str = word[1].replace(":", "")
    minutes = int(time_str[0])
    tens = int(time_str[1])
    ones = int(time_str[2])
    seconds = (minutes * 60) + (tens * 10) + (ones)
    artist_str = word[2].replace("_", " ")
    #artist_str = artist_str.replace("_", " ")
    album_str = word[3].replace("_", " ")
    #album_str = album_str.replace("_", " ")
    genre = word[4]
    track_int = int(word[5])

    #if artist is not already in the map, add
    #if album not already in the map, add
    #if song not already in the map, add
    toAdd = Song(title, seconds, track_int)
    print(toAdd.time)



f.close