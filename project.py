import webbrowser 
class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link
        self.seen = False

    def open(self):
        webbrowser.open(self.link)
        self.seen = True


class Playlist:
    def __init__(self,name,description,rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos


def read_info_video():
    title = input("enter title video : ") + "\n"
    link = input("enter link video : ") + "\n"
    video  = Video(title,link)
    return video


def print_info_video(video):
    print("video title : ",video.title , end = "")
    print("video link : ",video.link , end = "")


def read_info_videos():
    videos = []
    total = int(input("enter amount video : "))
    for i in range(total):
        print("enter info video ",i+1)
        vid = read_info_video()
        videos.append(vid)
    return videos


def print_info_videos(videos):
    for i in range(len(videos)):
        print("info video ",i+1)
        print_info_video(videos[i])


def write_to_file(videos,file):
    file.write(str(len(videos)) + "\n")
    for i in range(len(videos)):
        file.write(videos[i].title)
        file.write(videos[i].link)

        
def read_video_from_text(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        title =  file.readline()
        link =  file.readline()
        video = Video(title,link)
        videos.append(video)

    return videos


def read_playlist():
    playlist_name = input("enter playlist name : ") + "\n"
    playlist_description = input("enter playlist description : ") + "\n"
    playlsit_rating = input("enter playlist rating (1-5) : ") + "\n"
    playlist_videos = read_info_videos()
    playlist = Playlist(playlist_name,playlist_description,playlsit_rating,playlist_videos)
    return playlist
    

def write_playlist_txt(playlist):
    with open("data.txt","w") as file:
        file.write(playlist.name  )
        file.write(playlist.description  )
        file.write(playlist.rating )
        write_to_file(playlist.videos,file)
    print("successfully write playlist to txt!")


def read_playlist_from_text():
    with open("data.txt","r") as file:
        playlist_name = file.readline()
        playlist_description = file.readline()
        playlist_rating = file.readline()
        playlist_videos  = read_video_from_text(file)
    playlist = Playlist(playlist_name,playlist_description,playlist_rating,playlist_videos)
    return playlist 


def print_playlist(playlist):
    print("playlist name : ", playlist.name , end = "") 
    print("playlist description : ", playlist.description , end = "") 
    print("playlist rating : ", playlist.rating , end = "") 
    print_info_videos(playlist.videos)

def show_menu():
    print("-----MAIN MENU-----")
    print("+ option 1:create playlist")
    print("+ option 2: show playlist")
    print("+ option 3: play a video")
    print("+ option 4: add a video")
    print("+ option 5: update playlist")
    print("+ option 6: remove video")
    print("+ option 7: save and exit")
    print("-------------------")


def select_in_range(prompt, min ,max):
    choice = input(prompt)
    print("-----------------")
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice

def play_video(playlist):
    print_info_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range("select a video (1, " + str(total) + "):",1,total)
    print("open video : " + playlist.videos[choice-1].title + "-" + playlist.videos[choice-1].link,end = "")
    playlist.videos[choice-1].open()


def add_video(playlist):
    print("enter new video information")
    new_video_title = input("enter new video title :") + "\n"
    new_video_link  = input("enter new video link : ") + "\n"
    new_video = Video(new_video_title,new_video_link)
    playlist.videos.append(new_video)

    return playlist

def update_playlist(playlist):
    #update name,description,rating
    print("update playlsit ?")
    print("1 : name")
    print("2 : description")
    print("3 : rating")
    
    choice = select_in_range("enter what you want to update(1-3 : ",1,3)
    if choice == 1:
        new_playlist_name = input("enter new name for playlist : ") + "\n"
        playlist.name = new_playlist_name
        print("updated successfully !")
        return playlist
    if choice == 2:
        new_playlist_description = input("enter new description for playlist : ") + "\n"
        playlist.description = new_playlist_description
        print("updated successfully !")
        return playlist
    if choice == 3:
        new_playlist_rating = str(select_in_range("enter new rating for playlist (1-5): ",1,5)) + "\n"
        playlist.rating = new_playlist_rating
        print("updated successfully !")
        return playlist  


def remove_video(playlist):
    print_info_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range("enter video want to remove (1," + str(total) + "):",1,total)
    del playlist.videos[choice - 1] 
    return playlist

def main(): 
    try:
        playlist = read_playlist_from_text()
        print("loaded data successfully")
    except:
        print("welcome first user")

 
    while True:
        show_menu()
        choice  = select_in_range("select an option (1-7) :",1,7)
        if choice == 1:
            playlist = read_playlist()
            input("\npress enter to continue.\n")
        elif choice == 2:
            print_playlist(playlist)
            input("\npress enter to continue.\n")
        elif choice == 3:
            play_video(playlist)
            input("\npress enter to continue.\n") 
        elif choice == 4:
            playlist = add_video(playlist)
            input("\npress enter to continue.\n") 
        elif choice == 5:
            playlist = update_playlist(playlist)
            input("\npress enter to continue.\n")
        elif choice == 6:
            playlist = remove_video(playlist)
            input("\npress enter to continue.\n")
        elif choice == 7:
            write_playlist_txt(playlist)
            input("\npress enter to continue.\n") 
            break
        else:
            print("Wrong Input, exist.")
            break

main()


