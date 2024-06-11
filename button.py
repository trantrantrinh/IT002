class Button():
    """
    Một lớp để đại diện cho một nút trong trò chơi.

    Thuộc tính:
    image : pygame.Surface
        Hình ảnh của nút.
    x_pos : int
        Tọa độ x của nút.
    y_pos : int
        Tọa độ y của nút.
    font : pygame.font.Font
        Phông chữ được sử dụng để hiển thị văn bản trên nút.
    base_color : tuple
        Màu sắc cơ bản của văn bản khi nút không được hover.
    hovering_color : tuple
        Màu sắc của văn bản khi nút được hover.
    text_input : str
        Văn bản hiển thị trên nút.
    text : pygame.Surface
        Hình ảnh văn bản được render.
    rect : pygame.Rect
        Vùng hình chữ nhật của nút.
    text_rect : pygame.Rect
        Vùng hình chữ nhật của văn bản.

    Phương thức:
    update(screen)
        Cập nhật và vẽ nút lên màn hình.
    checkForInput(position)
        Kiểm tra xem vị trí con trỏ chuột có nằm trong vùng của nút hay không.
    changeColor(position)
        Thay đổi màu sắc của văn bản khi con trỏ chuột di chuyển vào/ra khỏi nút.
    """

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        """
        Khởi tạo tất cả các thuộc tính cần thiết cho đối tượng nút.

        Tham số:
        image : pygame.Surface
            Hình ảnh của nút.
        pos : tuple
            Tọa độ (x, y) của nút.
        text_input : str
            Văn bản hiển thị trên nút.
        font : pygame.font.Font
            Phông chữ được sử dụng để hiển thị văn bản trên nút.
        base_color : tuple
            Màu sắc cơ bản của văn bản khi nút không được hover.
        hovering_color : tuple
            Màu sắc của văn bản khi nút được hover.
        """
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """
        Cập nhật và vẽ nút lên màn hình.

        Tham số:
        screen : pygame.Surface
            Màn hình trò chơi để vẽ nút.
        """
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        """
        Kiểm tra xem vị trí con trỏ chuột có nằm trong vùng của nút hay không.

        Tham số:
        position : tuple
            Vị trí (x, y) của con trỏ chuột.

        Trả về:
        bool
            True nếu con trỏ chuột nằm trong vùng của nút, ngược lại False.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
