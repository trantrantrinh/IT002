import pygame, sys, random
from game import Game
from config import screen_width, screen_height, offset, blue

class Main:
    def __init__(self):
        """
        Khởi tạo các thành phần chính của trò chơi và đặt sự kiện bắn laser và tạo tàu bí ẩn.
        """
        pygame.init()
        self.play = pygame.transform.scale(pygame.image.load("Graphics/play.jpg"), (2000, 2000))
        self.font = pygame.font.Font("Graphics/monogram.ttf", 40)
        self.score_text_surface = self.font.render("SCORE", False, blue)
        self.highscore_text_surface = self.font.render("HIGH-SCORE", False, blue)
        self.screen = pygame.display.set_mode((screen_width + offset, screen_height + 2 * offset))
        pygame.display.set_caption("Python Space Invaders")
        self.clock = pygame.time.Clock()
        self.game = Game(screen_width, screen_height, offset)
        
        self.shoot_laser= pygame.USEREVENT
        pygame.time.set_timer(self.shoot_laser, 300)
        
        self.mysteryship = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mysteryship, random.randint(4000, 8000))

        self.mysteryship_laser = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mysteryship_laser, 3000)
        
    def run(self):
        """
        Bắt sự kiện, cập nhật trạng thái và vẽ các phần tử trên màn hình.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.shoot_laser and self.game.run:
                    self.game.alien_shoot_laser()

                if event.type == self.mysteryship_laser and self.game.run:
                    self.game.mystery_ship_shoot_laser()
                    pygame.time.set_timer(self.mysteryship_laser, 3000) 
            
            # Kiểm tra nếu tàu bí ẩn chưa xuất hiện thì tạo mới tàu bí ẩn
            if not self.game.aliens_group.sprites():
                if not self.game.mystery_ship_group.sprites():
                    self.game.create_mystery_ship()
                    pygame.time.set_timer(self.mysteryship, random.randint(2000, 5000))
            
            if self.game.run:
                self.game.spaceship_group.update()
                self.game.move_aliens()
                self.game.alien_lasers_group.update()
                self.game.mystery_ship_group.update()
                self.game.mystery_ship_shoot_laser()
                self.game.check_for_collisions()
                self.game.mystery_ship_lasers_group.update()
            self.screen.blit(self.play, (-100, -100))
            pygame.draw.rect(self.screen, blue, (10, 10, 780, 780), 2)
            pygame.draw.line(self.screen, blue, (25, 700), (775, 700), 3)
            x = 50
            for life in range(self.game.lives):
                self.screen.blit(self.game.spaceship_group.sprite.image, (x, 720))
                x += 50
            self.screen.blit(self.score_text_surface, (30, 15, 50, 50))
            formatted_score = str(self.game.score).zfill(5)
            score_surface = self.font.render(formatted_score, False, blue)
            self.screen.blit(score_surface, (30, 40, 50, 50))
            self.screen.blit(self.highscore_text_surface, (610, 710, 50, 50))
            formatted_highscore = str(self.game.highscore).zfill(5)
            highscore_surface = self.font.render(formatted_highscore, False, blue)
            self.screen.blit(highscore_surface, (680, 740, 50, 50))
            self.game.spaceship_group.draw(self.screen)
            self.game.spaceship_group.sprite.lasers_group.draw(self.screen)
            for obstacle in self.game.obstacles:
                obstacle.blocks_group.draw(self.screen)
            self.game.aliens_group.draw(self.screen)
            self.game.alien_lasers_group.draw(self.screen)
            self.game.mystery_ship_group.draw(self.screen)
            self.game.mystery_ship_lasers_group.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)
            
