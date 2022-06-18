# used libraries
import os

# define commands variables
wget = 'wget -O '

# A function that haves a for loop wich downloads the episode 
def downloadEpisodes(ini_episode, fn_episode):
    for downloaded_episodes in range(ini_episode,fn_episode):
        print(downloaded_episodes)
    else:
        print("All episodes downloaded successfully")

# A function that creates a text file
def openEpisodesLinkFile():
    file = open('links.txt', 'w')
    print("A file named 'links.txt' has been created, put your links there and press enter.")
    input()

if __name__ == '__main__':
    # Asks for the episode numbers 
    print("What's the initial episode number?")
    initial_episode = input()
    print("\nWhat's the final episode number?")
    final_episode = input()

    # Convert these variables to int and fix them
    initial_episode = int(initial_episode)
    final_episode = int(final_episode) + 1

    # Call other functions
    openEpisodesLinkFile()

    downloadEpisodes(initial_episode, final_episode)
