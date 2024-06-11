import pygame, random
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from alien import Alien
from laser import Laser
from alien import MysteryShip
from config import screen_width, screen_height, offset

class Game:
    def __init__(self, screen_width, screen_height, offset):
        """
        Khởi tạo trò chơi với kích thước màn hình và độ lệch đã cho.
        
        Tham số
        ----------
        screen_width : int
            Chiều rộng của màn hình trò chơi.
        screen_height : int
            Chiều cao của màn hình trò chơi.
        offset : int
            Giá trị độ lệch để định vị các phần tử trên màn hình.
        """
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(screen_width, screen_height, offset))
        self.obstacles = self.create_obstacles()
        self.aliens_group = pygame.sprite.Group()
        self.create_aliens()
        self.aliens_direction = 1
        self.alien_lasers_group = pygame.sprite.Group()
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.mystery_ship_lasers_group = pygame.sprite.Group()
        self.lives = 3
        self.mystery_ship_hit_count = 0
        self.run = True
        self.score = 0
        self.highscore = 0
        self.mystery_ship_laser_timer = 0
        self.explosion_sound = pygame.mixer.Sound("Sounds/explosion.ogg")
        self.check_and_load_highscore()
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def create_obstacles(self):
        """
        Tạo và trả về danh sách chướng ngại vật.

        Trả về
        -------
        list
            Danh sách các đối tượng Obstacle.
        """
        obstacle_width = len(grid[0]) * 3
        gap = (screen_width + offset - (3 * obstacle_width)) / 4
        obstacles = []
        for i in range(3):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, screen_height - 100)
            obstacles.append(obstacle)
        return obstacles

    def create_aliens(self):
        """
        Tạo các đối tượng alien và thêm vào nhóm aliens_group.
        """
        for row in range(5):
            for column in range(8):
                x = 75 + column * 85
                y = 110 + row * 55

                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1

                alien = Alien(alien_type, x + offset / 2, y)
                self.aliens_group.add(alien)

    def move_aliens(self):
        """
        Di chuyển các alien và thay đổi hướng nếu chạm vào cạnh màn hình.
        """
        self.aliens_group.update(self.aliens_direction)
        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= screen_width + offset / 2:
                self.aliens_direction = -1
                self.alien_move_down(1)
            elif alien.rect.left <= offset / 2:
                self.aliens_direction = 1
                self.alien_move_down(1)

    def alien_move_down(self, distance):
        """
        Di chuyển tất cả các alien xuống một khoảng cách nhất định.

        Tham số
        ----------
        distance : int
            Khoảng cách để di chuyển các alien xuống.
        """
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        """
        Cho một alien ngẫu nhiên bắn tia laser.
        """
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, screen_height)
            self.alien_lasers_group.add(laser_sprite)

    def create_mystery_ship(self):
        """
        Tạo và thêm tàu bí ẩn vào trò chơi.
        """
        self.mystery_ship_group.add(MysteryShip(screen_width, offset))

            
    def mystery_ship_shoot_laser(self):
        """
        Cho mysteryship bắn 20 tia laser.
        """
        if self.mystery_ship_laser_timer >= 40:  # số frame giữa mỗi lần bắn laser của MysteryShip
            if self.mystery_ship_group.sprites():
                mystery_ship = self.mystery_ship_group.sprites()[0]
                
                for _ in range(20): 
                    x = mystery_ship.rect.centerx + random.randint(-50, 50)  
                    y = mystery_ship.rect.bottom  
                    laser_sprite = Laser((x, y), random.choice([-7, -6, -5, -4]), screen_height)
                    self.mystery_ship_lasers_group.add(laser_sprite)
                    
            self.mystery_ship_laser_timer = 0
        else:
            self.mystery_ship_laser_timer += 1

    
    def game_over(self):
        """
        Kết thúc trò chơi và hiển thị màn hình kết thúc.
        """
        pygame.init()
        screen = pygame.display.set_mode((750, 700))
        pygame.display.set_caption("Game Over")
        background = pygame.image.load("Graphics/game_over.jpg")
        background = pygame.transform.scale(background, (750, 700))
        font = pygame.font.Font(None, 40)
        text = font.render(str(self.score), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (215, 325)

        highscore_font = pygame.font.Font(None, 40)
        highscore_text = highscore_font.render(str(self.highscore), True, (255, 255, 255))
        highscore_rect = highscore_text.get_rect()
        highscore_rect.center = (310, 373)

        running = True
        pygame.mixer.music.stop()
        game_over_sound = pygame.mixer.Sound("Sounds/game_over.mp3")
        game_over_sound.play()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.blit(background, (0, 0))
            screen.blit(text, text_rect)
            screen.blit(highscore_text, highscore_rect)
            pygame.display.flip()

        pygame.quit()
        exit()

    def game_win(self):
        """
        Kết thúc trò chơi và hiển thị màn hình chiến thắng.
        """
        pygame.init()
        screen = pygame.display.set_mode((750, 700))
        pygame.display.set_caption("Game Win")
        background = pygame.image.load("Graphics/game_win.jpg") 
        background = pygame.transform.scale(background, (750, 700))
        pygame.mixer.music.stop()
        game_win_sound = pygame.mixer.Sound("Sounds/game_win.mp3")
        game_win_sound.play()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            screen.blit(background, (0, 0))
            pygame.display.flip()

        pygame.quit()
        exit()

    def check_for_collisions(self):
        """
        Kiểm tra và xử lý va chạm giữa các thành phần trong trò chơi.
        """
        if self.spaceship_group.sprite.lasers_group:
            aliens_hit = []
            for laser_sprite in self.spaceship_group.sprite.lasers_group:
                aliens_hit += pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True)
                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, False):
                    self.explosion_sound.play()
                    laser_sprite.kill()
                    self.mystery_ship_hit_count += 1
                    if self.mystery_ship_hit_count == 3:
                        self.score += 1000
                        self.check_and_load_highscore()
                        self.mystery_ship_group.empty()
                        self.game_win()
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
            if aliens_hit:
                self.explosion_sound.play()
                for alien in aliens_hit:
                    self.score += 100
                    self.check_and_load_highscore()
        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    laser_sprite.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
        if self.mystery_ship_lasers_group:
            for laser_sprite in self.mystery_ship_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    laser_sprite.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
        if self.aliens_group:
            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()


    def check_and_load_highscore(self):
        """
        Kiểm tra và cập nhật điểm cao nhất nếu điểm hiện tại cao hơn.
        """
        try:
            with open("highscore.txt", "r") as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            self.highscore = 0

        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))
