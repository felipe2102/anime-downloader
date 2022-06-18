
import os
# define commands variables
wget = 'wget -O '

def downloadEpisodes(ini_episode, fn_episode):
    for downloaded_episodes in range(ini_episode,fn_episode):
        print(downloaded_episodes)
    else:
        print("All episodes downloaded successfully")

def openEpisodesLinkFile():
    file = open('links.txt', 'w')
    print("A file named 'links.txt' has been created, put your links there and press enter.")
    input()

if __name__ == '__main__':
    print("What's the initial episode number?")
    initial_episode = input()
    print("\nWhat's the final episode number?")
    final_episode = input()

    initial_episode = int(initial_episode)
    final_episode = int(final_episode) + 1
    
    openEpisodesLinkFile()

    downloadEpisodes(initial_episode, final_episode)
