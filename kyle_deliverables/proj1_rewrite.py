#class Song:
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

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
for line in content:
    line = line.replace("\n","")
    word = line.split(" ")
    #word = word.replace("_", " ")
    title = word[0]
    title = title.replace("_", " ")
    time_str = word[1]
    artist_str = word[2]
    artist_str = artist_str.replace("_", " ")
    album_str = word[3]
    album_str = album_str.replace("_", " ")
    genre = word[4]
    track_str = word[5]
    print(word)



f.close