import pygame, random
from config import screen_width, screen_height, offset

class Alien(pygame.sprite.Sprite):
    """
    Một lớp để đại diện cho người ngoài hành tinh trong trò chơi.

    Thuộc tính:
    type : str
        Loại người ngoài hành tinh.
    image : pygame.Surface
        Hình ảnh của người ngoài hành tinh.
    rect : pygame.Rect
        Vùng hình chữ nhật của người ngoài hành tinh.

    Phương thức:
    update(direction)
        Di chuyển người ngoài hành tinh theo hướng đã cho.
    """

    def __init__(self, type, x, y):
        """
        Khởi tạo tất cả các thuộc tính cần thiết cho đối tượng người ngoài hành tinh.

        Tham số:
        type : str
            Loại người ngoài hành tinh.
        x : int
            Tọa độ x ban đầu của người ngoài hành tinh.
        y : int
            Tọa độ y ban đầu của người ngoài hành tinh.
        """
        super().__init__()
        self.type = type
        path = f"Graphics/alien_{type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        """
        Di chuyển người ngoài hành tinh theo hướng đã cho.

        Tham số:
        direction : int
            Hướng di chuyển của người ngoài hành tinh (giá trị âm để di chuyển sang trái và giá trị dương để di chuyển sang phải).
        """
        self.rect.x += direction

class MysteryShip(pygame.sprite.Sprite):
    """
    Một lớp để đại diện cho tàu bí ẩn trong trò chơi.

    Thuộc tính:
    image : pygame.Surface
        Hình ảnh của tàu bí ẩn.
    rect : pygame.Rect
        Vùng hình chữ nhật của tàu bí ẩn.
    speed : int
        Tốc độ di chuyển của tàu bí ẩn.

    Phương thức:
    update()
        Cập nhật vị trí của tàu bí ẩn.
    """
    def __init__(self, screen_width, offset):
        """ Khởi tạo thuộc tính"""
        super().__init__()
        original_image = pygame.image.load("Graphics/mystery.png")
        scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 2, original_image.get_height() * 2))

        x = random.choice([offset / 2, screen_width + offset - scaled_image.get_width()])
        if x == offset / 2:
            self.speed = 3
        else:
            self.speed = -3

        self.image = scaled_image
        self.rect = self.image.get_rect(topleft=(x, 90))

    def update(self):
        """
        Cập nhật vị trí của tàu bí ẩn. Nếu tàu bí ẩn đi ra khỏi màn hình, nó sẽ bị xóa.
        """
        self.rect.x += self.speed
        if self.rect.right > screen_width + offset/2:
            self.kill()
        elif self.rect.left < offset/2:
            self.kill()
