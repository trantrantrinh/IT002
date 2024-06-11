import pygame
# tạo chướng ngại vật

class Block(pygame.sprite.Sprite):
	"""
    Đối tượng đại diện cho một khối chướng ngại vật trong trò chơi.
    """
	def __init__(self, x, y):
		"""
        Khởi tạo một Block mới.

        Tham số:
            x (int): Tọa độ x của khối.
            y (int): Tọa độ y của khối.
        """
		super().__init__()
		self.image = pygame.Surface((3,3))
		self.image.fill((100,149,237))
		self.rect = self.image.get_rect(topleft = (x,y))

grid = [
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]]

class Obstacle:
	"""
    Lớp đại diện cho chướng ngại vật trong trò chơi.
    """
	def __init__(self, x, y):
		"""
        Khởi tạo một chướng ngại vật mới.

        Tham số:
            x (int): Tọa độ x của chướng ngại vật.
            y (int): Tọa độ y của chướng ngại vật.
        """
		self.blocks_group = pygame.sprite.Group()
		for row in range(len(grid)):
			for column in range(len(grid[0])):
				if grid[row][column] == 1:
					pos_x = x + column * 3
					pos_y = y + row * 3
					block = Block(pos_x, pos_y)
					self.blocks_group.add(block)

