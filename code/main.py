import pygame, sys
from settings import *
from level import Level



class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('AOOP Final Project')
		self.clock = pygame.time.Clock()

		self.level = Level()
		# Load pixel font
		self.font = pygame.font.Font('../pixel-operator/PixelOperator8.ttf', 30)
		# sound 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def show_start_screen(self):
		self.screen.fill((0, 0, 0))

		title_text = self.font.render('AOOP Final Project', True, (255, 255, 255))
		title_text = pygame.transform.scale(title_text, (title_text.get_width() * 2, title_text.get_height() * 2))
		title_rect = title_text.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery - 100))
		self.screen.blit(title_text, title_rect)

		member1_text = self.font.render('110612084 James Hsu', True, (255, 255, 255))
		member1_rect = member1_text.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery))
		self.screen.blit(member1_text, member1_rect)

		member2_text = self.font.render('110612025 Dunkun Wei', True, (255, 255, 255))
		member2_rect = member2_text.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery + 50))
		self.screen.blit(member2_text, member2_rect)

		prompt_text = self.font.render('Press any button to play', True, (255, 255, 255))
		prompt_rect = prompt_text.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery + 150))
		self.screen.blit(prompt_text, prompt_rect)

		pygame.display.flip()

		waiting = True
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
					waiting = False	
	
	def run(self):
		self.show_start_screen()  # Show start screen before the game loop
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()

			# Check if player is dead and display "You Died" message
			if self.level.player.is_dead:
				font = pygame.font.Font('../pixel-operator/PixelOperator8.ttf', 60)
				text = font.render('You Died', True, (255, 0, 0))
				text_rect = text.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery - 50))
				self.screen.blit(text, text_rect)
				pygame.display.flip()
				pygame.time.wait(2000)
				pygame.quit()
				sys.exit()

			pygame.display.update()
			#Control the frame rate
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()