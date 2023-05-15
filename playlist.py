import pygame
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

def read_video_from_text(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        title =  file.readline()
        link =  file.readline()
        video = Video(title,link)
        videos.append(video)

    return videos

def read_playlist_from_text():
    with open("data.txt","r") as file:
        playlist_name = file.readline()
        playlist_description = file.readline()
        playlist_rating = file.readline()
        playlist_videos  = read_video_from_text(file)
    playlist = Playlist(playlist_name,playlist_description,playlist_rating,playlist_videos)
    return playlist 
	 


class TextButton:
	def __init__(self,text ,position):
		self.text = text
		self.position = position
	def is_mouse_on_text(self):
		mouse_x, mouse_y =pygame.mouse.get_pos() #get position of mouse  
		if (self.position[0]<mouse_x<self.position[0]+self.text_box[2]) and (self.position[1]<mouse_y<self.position[1]+self.text_box[3]):

			return True
		else :
			return False

	def draw(self):
		font = pygame.font.SysFont('sans',20)
		text_render = font.render(self.text,True,(0,0,0))
		self.text_box = text_render.get_rect() #get position of text
		screen.blit(text_render,self.position)
		if self.is_mouse_on_text() == True:
			pygame.draw.line(screen,(0,0,255),(self.position[0],self.position[1]+self.text_box[3]),(self.position[0]+self.text_box[2],self.position[1]+self.text_box[3]))
			text_render = font.render(self.text,True,(0,0,255))
		else:
			text_render = font.render(self.text,True,(0,0,0))

		screen.blit(text_render,self.position)


# run pygame 


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Playlist')
running = True
WHITE = (255,255,255)
clock = pygame.time.Clock()


#load data
playlist = read_playlist_from_text()

playlist_name_btn = TextButton(playlist.name.rstrip(),(50,50))
video_btn_list = []
margin = 50
for i in range(len(playlist.videos)):
	video_btn = TextButton(str(i+1)+": "+playlist.videos[i].title.rstrip(),(250,50+margin*i))
	video_btn_list.append(video_btn)


while running:		
	clock.tick(60)
	screen.fill(WHITE)

	playlist_name_btn.draw()
	for i in range(len(video_btn_list)):
		video_btn_list[i].draw()


	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if playlist_name_btn.is_mouse_on_text() == True:
					print("chooselaylist")
				for i in range(len(video_btn_list)):
					if video_btn_list[i].is_mouse_on_text() == True:
						playlist.videos[i].open()
				
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()