import pygame
from config import screen_height

class Laser(pygame.sprite.Sprite):
    """
    Lớp đại diện cho tia laser trong trò chơi.

    Thuộc tính
    ----------
    image : pygame.Surface
        Hình ảnh của tia laser.
    rect : pygame.Rect
        Hình chữ nhật bao quanh tia laser.
    speed : int
        Tốc độ di chuyển của tia laser.

    Phương thức
    -------
    __init__(self, position, speed, screen_height)
        Khởi tạo một tia laser tại vị trí được chỉ định với tốc độ và chiều cao màn hình.
    update(self)
        Cập nhật vị trí của tia laser theo hướng di chuyển và kiểm tra xem nó đã vượt ra khỏi màn hình hay chưa.
    """
    
    def __init__(self, position, speed, screen_height):
        """
        Khởi tạo một tia laser.

        Tham số
        ----------
        position : tuple
            Tọa độ (x, y) ban đầu của tia laser.
        speed : int
            Tốc độ di chuyển của tia laser.
        screen_height : int
            Chiều cao của màn hình trò chơi.
        """
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill((0, 206, 209))
        self.rect = self.image.get_rect(center=position)
        self.speed = speed

    def update(self):
        """
        Cập nhật vị trí của tia laser.

        Nếu tia laser vượt ra khỏi màn hình, nó sẽ bị xóa khỏi nhóm sprite.
        """
        self.rect.y -= self.speed
        if self.rect.y > screen_height + 15 or self.rect.y < 0:
            self.kill()
