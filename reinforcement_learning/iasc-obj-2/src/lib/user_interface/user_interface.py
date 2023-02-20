import pygame
from operators.direction import Direction
from operators.enviroment import Enviroment
import time

class UserInterface:

	def __init__(self, agent):


		self.__agent = agent
		self.__tick = 60
		print("\nPara mudar a velocidade clicar: F")

		# 70px width and height, when map is big is half
		print("size:", len(self.__agent.world[0]))
		self.__block_size = 70 if len(self.__agent.world[0]) < 14 else int(70/2)

		self.__size = (self.__block_size*len(self.__agent.world[0]), self.__block_size*len(self.__agent.world[1])) # width and height
		
		self.__display = pygame.display.set_mode((self.__size[0], self.__size[1]))

		self.__clock = pygame.time.Clock()

		# when the world is big it turns the images on half the size 
		self.__obstacle_img = pygame.transform.scale(pygame.image.load("../lib/user_interface/blockx.jpg"), (self.__block_size, self.__block_size))
		self.__target_img = pygame.transform.scale(pygame.image.load("../lib/user_interface/target4.png"), (self.__block_size, self.__block_size))
		self.__agent_img = pygame.transform.scale(pygame.image.load("../lib/user_interface/agent2.png"), (self.__block_size, self.__block_size))
		self.__empty_img = pygame.transform.scale(pygame.image.load("../lib/user_interface/down2.jpg"), (self.__block_size, self.__block_size))

	def loop(self):

		end = False

		while not end:
			#time.sleep(1)

			# detect when to stop the execution
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_f:
						self.__tick  = 60 if self.__tick == 10 else 10
						print("Mudou velocidade!!!")

			self.__agent.execute()
			
			self.__draw_blocks(self.__agent.world)


			self.__draw_policy(self.__agent.policy)

			pygame.display.update()

			self.__clock.tick(self.__tick)

		pygame.quit()

	def __draw_blocks(self, world):

		for line in range(len(world)):
			for column in range(len(world[line])):
				
				size = (column * self.__block_size, line * self.__block_size)

				self.__get_img(world[line][column], size)


	def __get_img(self, type, size):

		if type == Enviroment.OBSTACLE.value:
			self.__display.blit(self.__obstacle_img, size)


		elif type == Enviroment.TARGET.value:
			self.__display.blit(self.__empty_img, size)
			self.__display.blit(self.__target_img, size)

		elif type == Enviroment.EMPTY.value:
			self.__display.blit(self.__empty_img, size)

		else:
			self.__display.blit(self.__empty_img, size)
			self.__display.blit(self.__agent_img, size)


	def __draw_policy(self, policy):

		for state in policy.keys():
			
			pos = state[0]
			angle = state[1]
			value = policy[state]

			# center the pixel to draw the arrows, when the map is large must make half the size
			center_pix = 35 if len(self.__agent.world[0]) < 14 else int(35/2)

			pos_x = (pos[0]*self.__block_size) + center_pix
			pos_y = (pos[1]*self.__block_size) + center_pix

			color = None
			increased_color = min(int(abs(value * (1.8)))+85, 255)

			if value <= 0:
				color = (increased_color, 15, 15) # red color

			else:
				color = (15, increased_color, 15)# green color


			# center the pixel to draw the arrows, when the map is large must make half the size
			line_size = 30 if len(self.__agent.world[0]) < 14 else int(30/2)
			arrow_size = 10 if len(self.__agent.world[0]) < 14 else int(10/2)
			angle_45_increase = 5 if len(self.__agent.world[0]) < 14 else 0

			if angle == Direction.FRONT.value:
				pygame.draw.line(self.__display, color, (pos_x + 3, pos_y), (pos_x + line_size, pos_y), 3)
				pygame.draw.line(self.__display, color, (pos_x + line_size, pos_y), (pos_x + line_size - arrow_size, pos_y - arrow_size), 3)
				pygame.draw.line(self.__display, color, (pos_x + line_size, pos_y), (pos_x + line_size - arrow_size, pos_y + arrow_size), 3)

			elif angle == Direction.BACK.value:
				pygame.draw.line(self.__display, color, (pos_x - 3, pos_y), (pos_x-line_size, pos_y), 3)
				pygame.draw.line(self.__display, color, (pos_x-line_size, pos_y), (pos_x-line_size + arrow_size, pos_y + arrow_size), 3)
				pygame.draw.line(self.__display, color, (pos_x-line_size, pos_y), (pos_x-line_size + arrow_size, pos_y - arrow_size), 3)

			elif angle == Direction.TOP.value:
				pygame.draw.line(self.__display, color, (pos_x, pos_y - 3), (pos_x, pos_y - line_size), 3)
				pygame.draw.line(self.__display, color, (pos_x, pos_y - line_size), (pos_x + arrow_size, pos_y-line_size + arrow_size), 3)
				pygame.draw.line(self.__display, color, (pos_x, pos_y - line_size), (pos_x - arrow_size, pos_y-line_size + arrow_size), 3)

			elif angle == Direction.DOWN.value:
				pygame.draw.line(self.__display, color, (pos_x, pos_y + 3), (pos_x, pos_y + line_size), 3)
				pygame.draw.line(self.__display, color, (pos_x, pos_y + line_size), (pos_x + arrow_size, pos_y + line_size - arrow_size), 3)
				pygame.draw.line(self.__display, color, (pos_x, pos_y + line_size), (pos_x - arrow_size, pos_y + line_size - arrow_size), 3)

			elif angle == Direction.TOP_FRONT.value:
				pygame.draw.line(self.__display, color, (pos_x + 3, pos_y - 3), (pos_x + line_size , pos_y - line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x + line_size , pos_y - line_size ), 
					(pos_x + line_size - arrow_size - angle_45_increase, pos_y - line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x + line_size , pos_y - line_size ), 
					(pos_x + line_size , pos_y - line_size + arrow_size + angle_45_increase), 3)

			elif angle == Direction.TOP_BACK.value:
				pygame.draw.line(self.__display, color, (pos_x - 3, pos_y - 3), (pos_x - line_size , pos_y - line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x - line_size , pos_y - line_size ), 
					(pos_x - line_size + arrow_size + angle_45_increase, pos_y - line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x - line_size , pos_y - line_size ), 
					(pos_x - line_size , pos_y - line_size  + arrow_size + angle_45_increase), 3)

			elif angle == Direction.DOWN_FRONT.value:

				pygame.draw.line(self.__display, color, (pos_x + 3, pos_y + 3), (pos_x + line_size , pos_y + line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x + line_size , pos_y + line_size ), 
					(pos_x + line_size - arrow_size - angle_45_increase, pos_y + line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x + line_size , pos_y + line_size ), 
					(pos_x + line_size , pos_y + line_size - arrow_size - angle_45_increase), 3)

			else:

				pygame.draw.line(self.__display, color, (pos_x - 3, pos_y + 3), (pos_x - line_size , pos_y + line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x - line_size , pos_y + line_size ), 
					(pos_x - line_size + arrow_size + angle_45_increase, pos_y + line_size ), 3)

				pygame.draw.line(self.__display, color, (pos_x - line_size , pos_y + line_size ), 
					(pos_x - line_size , pos_y + line_size - arrow_size - angle_45_increase), 3)