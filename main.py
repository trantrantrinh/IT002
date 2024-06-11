import pygame
import sys
from button import Button
from game1 import Main

class MainGame:
    def __init__(self):
        """Khởi tạo lớp MainGame."""
        pygame.init()
        self.SCREEN = pygame.display.set_mode((750, 700))
        pygame.display.set_caption("Menu")
        self.BG_Menu = pygame.image.load("Graphics/Background.png").convert()

    def get_font(self, size):
        """Lấy một đối tượng font Pygame với kích thước đã cho.

        Args:
            size (int): Kích thước của font.

        Returns:
            pygame.font.Font: Đối tượng font Pygame.
        """
        return pygame.font.Font("Graphics/font.ttf", size // 4 * 3)

    def run(self):
        """Chạy vòng lặp menu chính."""
        running = True
        while running:
            self.SCREEN.blit(self.BG_Menu, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, (255, 255, 204))
            MENU_RECT = MENU_TEXT.get_rect(center=(375, 150))
            PLAY_BUTTON = Button(image=pygame.image.load("Graphics/Play Rect.jpg"), pos=(375, 400),
                                text_input="PLAY", font=self.get_font(80), base_color="#333333", hovering_color="#333333")
            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON]:
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        game_app = Main()
                        game_app.run()
                        running = False

            pygame.display.update()

        pygame.quit()
        sys.exit()

main = MainGame()
main.run()