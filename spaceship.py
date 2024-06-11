import pygame
from laser import Laser
from config import screen_width, screen_height, offset, speed, laser_delay 

class Spaceship(pygame.sprite.Sprite):
    """
    Lớp đại diện cho tàu vũ trụ của người chơi trong trò chơi Space Invaders.

    Thuộc tính
    ----------
    image : pygame.Surface
        Hình ảnh của tàu vũ trụ.
    rect : pygame.Rect
        Hình chữ nhật giới hạn tàu vũ trụ.
    lasers_group : pygame.sprite.Group
        Nhóm các tia laser được bắn từ tàu vũ trụ.
    laser_ready : bool
        Biến xác định xem tàu vũ trụ đã sẵn sàng bắn tia laser mới hay không.
    laser_time : int
        Thời gian lần cuối cùng mà tàu vũ trụ đã bắn tia laser.
    laser_sound : pygame.mixer.Sound
        Âm thanh được phát khi tàu vũ trụ bắn tia laser.

    Phương thức
    -------
    __init__(self, screen_width, screen_height, offset)
        Khởi tạo tàu vũ trụ và các thuộc tính liên quan.
    get_user_input(self)
        Xử lý các sự kiện đầu vào từ người chơi.
    update(self)
        Cập nhật trạng thái của tàu vũ trụ.
    limit_movement(self)
        Giới hạn phạm vi di chuyển của tàu vũ trụ để không vượt ra khỏi màn hình.
    recharge_laser(self)
        Thực hiện việc nạp lại tia laser sau mỗi lần bắn.
    reset(self)
        Đặt lại tàu vũ trụ về vị trí ban đầu và xóa tất cả các tia laser.
    """
    
    def __init__(self, screen_width, screen_height, offset):
        """
        Khởi tạo tàu vũ trụ.

        Tham số
        ----------
        screen_width : int
            Chiều rộng của màn hình trò chơi.
        screen_height : int
            Chiều cao của màn hình trò chơi.
        offset : int
            Khoảng cách lề bên trái của màn hình.
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Graphics/spaceship.png").convert_alpha(), (45, 45))
        self.rect = self.image.get_rect(midbottom=((screen_width + offset) / 2, screen_height))
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")

    def get_user_input(self):
        """Xử lý các sự kiện đầu vào từ người chơi."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        
        if keys[pygame.K_UP]:
            self.rect.y -= speed

        if keys[pygame.K_DOWN]:
            self.rect.y += speed

        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, screen_height)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def update(self):
        """Cập nhật trạng thái của tàu vũ trụ."""
        self.get_user_input()
        self.limit_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def limit_movement(self):
        """Giới hạn phạm vi di chuyển của tàu vũ trụ để không vượt ra khỏi màn hình."""
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < offset:
            self.rect.left = offset
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top < 0:
            self.rect.top = 0

    def recharge_laser(self):
        """Thực hiện việc nạp lại tia laser sau mỗi lần bắn."""
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= laser_delay:
                self.laser_ready = True