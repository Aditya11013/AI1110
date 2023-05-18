import os
import numpy as np
import vlc

# Define the path to your video playlist folder
playlist_folder = "/home/aditya/playlist"

# Get the list of video files from the playlist folder
playlist = os.listdir(playlist_folder)

# Create a VLC media player instance
instance = vlc.Instance("--no-video")

# List to keep track of played songs
played_songs = []

# Loop indefinitely
while True:
    # Check if all songs have been played
    if len(played_songs) == len(playlist):
        played_songs = []  # Reset the played songs list
        print("Loop completed. Starting from the beginning.")

    # Choose a random song from the playlist that has not been played
    random_song = np.random.choice(playlist)
    while random_song in played_songs:
        random_song = np.random.choice(playlist)

    # Create the full path to the selected song file
    song_path = os.path.join(playlist_folder, random_song)

    # Extract the song name from the file name
    song_name = os.path.splitext(random_song)[0]

    # Create a media player
    player = instance.media_player_new()

    # Load the selected song
    media = instance.media_new(song_path)

    # Set the media to play only the audio
    media.add_options(":no-video")

    # Set the media to loop
    media.get_mrl()
    player.set_media(media)

    # Play the audio
    player.play()
    # Display the song name
    print("Now playing:", song_name)

    # Add the song to the played songs list
    played_songs.append(random_song)

    # Wait for user input or until the audio finishes playing
    while True:
        # Check for user input
        user_input = input("Enter 's' to skip or 'q' to quit: ")

        if user_input.lower() == 's':
            # Stop the current song
            player.stop()
            break
        elif user_input.lower() == 'q':
            # Quit the program
            player.stop()
            exit()

        # Check if the audio has finished playing
        if player.get_state() == vlc.State.Ended:
            break
