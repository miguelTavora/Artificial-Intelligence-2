import pygame

class GraphQueens():

	def __init__(self):
		
		self.__size = 70
		self.__display = pygame.display.set_mode((self.__size*8, self.__size*8))
		self.__clock = pygame.time.Clock()

		# when the world is big it turns the images on half the size 
		self.__queen_img = pygame.transform.scale(pygame.image.load("../lib/graph/queen.png"), (self.__size-5, self.__size-5))


	def graph(self, board):
		

		end = False

		while not end:
			#time.sleep(0.5)

			# detect when to stop the execution
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end = True


			self.__draw_board(board)


			pygame.display.update()
			self.__clock.tick(30)

		pygame.quit()


	def __draw_board(self, board):

		black = (0, 0, 0)
		white = (255, 255, 255)
		count = 0

		for line in range(len(board)):
			for column in range(len(board[line])):
				
				color = black if count%2 == 0 else white

				pygame.draw.rect(self.__display, color, [self.__size*line, self.__size*column, self.__size, self.__size])

				if board[column][line] == 1:
					size = (line * self.__size, column * self.__size)
					self.__display.blit(self.__queen_img, size) 

				count += 1

			count = 1 if line%2 == 0 else 0