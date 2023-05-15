import webbrowser
class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link

    def open(self):
        webbrowser.open(self.link)


class Playlist:
    def __init__(self,name,description,rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos


def read_video():
    
    title  = input("enter video title : ") + "\n"
    link = input("enter video link : ") + "\n"
    video = Video(title, link)
    return video 

def read_videos():
    videos = []
    user_input = int(input("enter how many video : "))
    for i in range(user_input):
        print("enter infomation video ",i+1)
        vid = read_video()
        videos.append(vid)

    return videos

def print_video(video):
    print("video title : ",video.title , end="")
    print("video link : ",video.link , end="")

def print_videos(videos):
    
    for i in range(len(videos)):
        print("informations video ",i+1)
        print_video(videos[i])


def read_video_from_txt(file):
    title = file.readline() 
    link = file.readline()
    video = Video(title, link)
    return video

def read_videos_from_text(file):
    videos  = []
    
    total = file.readline()
    for i in range(int(total)):
        video = read_video_from_txt(file)
        videos.append(video)

    return videos

def write_video_txt(video,file):
    file.write(video.title)
    file.write(video.link)

def write_videos_text(videos,file):
    
        file.write(str(len(videos)) + "\n")
        for i in range(len(videos)):
            write_video_txt(videos[i],file)
    

def read_playlist():
    playlist_name = input("enter playlist name : ") + "\n"
    playlist_description = input("enter playlist description : ") + "\n"
    playlist_rating = input("enter playlist rating : ") + "\n"
    playlist_videos = read_videos()
    playlist =  Playlist(playlist_name, playlist_description, playlist_rating,playlist_videos)
    return playlist
    
def write_playlist_txt(playlist):
    with open("data.txt","w") as file:
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(playlist.rating)
        write_videos_text(playlist.videos,file)
    print("\nsuccessfully wrote")
    

def read_playlist_from_txt():
    
    with open("data.txt","r") as file:
        name = file.readline()
        description = file.readline()
        rating = file.readline()
        videos = read_videos_from_text(file)
    playlist = Playlist(name, description, rating, videos)   

    return playlist

def print_playlist(playlist):
    print("playlist name : ",playlist.name , end = "")
    print("playlist description : ",playlist.description , end = "")
    print("playlist rating : ",playlist.rating , end="")
    print_videos(playlist.videos)


def show_menu():
    print("\n----------------------")
    print("option 1: Craete playlist")
    print("option 2: Show playlist")
    print("option 3: Play a video")
    print("option 4: Add a video")
    print("option 5: Update playlist")
    print("option 6: Remove a video")
    print("option 7: Save and exit")

def select_in_range(prompt,min,max):
    choice = input(prompt)
    while not choice.isdigit() or max < int(choice) or int(choice) < min :
        choice = input(prompt)
    choice = int(choice) 
    return choice
    
def play_video(playlist):
    print_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range("select a video : ",1,total)
    print("open video have link : " + playlist.videos[choice - 1].link)
    # webbrowser.open(playlist.videos[choice - 1].link , new = 2)
    playlist.videos[choice - 1].open()


def add_video(playlist):
    title = input("enter title video : ") + "\n"
    link = input("enter link video : ") + "\n"
    video = Video(title,link)
    playlist = playlist.videos.append(video)
    return playlist


def update_playlist(playlist):
    print("1. Name : ")
    print("2. Description : ")
    print("3. Rating : ")
    
    choice = select_in_range("what do you want to update ? : ",1,3)
    if choice == 1:
        new_playlist_name = input("enter new name : ")+"\n"
        playlist.name = new_playlist_name
        print("updatee successfully")
        return playlist
    if choice == 2:
        new_playlist_descripition = input("enter new description : ")+"\n"
        playlist.description = new_playlist_descripition
        print("updatee successfully")
        return playlist
    if choice == 3:
        new_playlist_rating = str(select_in_range("enter new rating(1-5) : ",1,5)) + "\n"
        playlist.rating = new_playlist_rating
        print("updatee successfully")
        return playlist
    
    
def remove_video(playlist):
    print_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range("Do you want to remove video? :",1,total)
    del playlist.videos[choice -1]
    return playlist
def main():


    try:
        playlist = read_playlist_from_txt()
        print("loaded data successfully")
    except:
        print("welcome to playlist")

    while True:
        show_menu()
        choice = select_in_range("select an option(1-7): ",1,7)
        if choice == 1:
            playlist = read_playlist()
            input("press enter to continue")
        elif choice == 2:
            print("\n------------------- INFORMATION PLAYLIST --------------------")
            print_playlist(playlist)
            input("press enter to continue")
        elif choice == 3:
            play_video(playlist)
            input("press enter to continue")
        elif choice == 4:
            playlist = add_video(playlist)
            input("press enter to continue")
        elif choice == 5:
            playlist = update_playlist(playlist) 
            input("press enter to continue")
        elif choice == 6:
            playlist = remove_video(playlist)
            input("press enter to continue")
        elif choice == 7:
            write_playlist_txt(playlist)
            input("press enter to continue")
            break
        else:
            print("wrong input,exist")
            break
        


main()
