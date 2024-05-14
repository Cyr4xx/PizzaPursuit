# class Button
class Button():
    # __init__ is used to initialize a new Button class
    # image         -   Button
    # pos           -   position array that stores x and y
    # text_input    -   text the button will contain
    # font          -   which font the button will use
    # base_color    -   color the button will use
    def __init__(self, image, pos, text_input, font, base_color,
                 hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        # checks if image == None
        # if image is null then the button will use the text
        if self.image is None:
            self.image = self.text
        # scales the button based on the image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        # scales the button based on the text
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):  # Updates/puts the button on the screen
        # checks if image is null
        if self.image is not None:
            # renders the image on the button
            screen.blit(self.image, self.rect)
        # renders the text on the button
        screen.blit(self.text, self.text_rect)

    def checkForInput(self,
                      position):  # Checks if mouse clicked button.
        # checks if mouse is in the range of the rect bounds
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self,
                    position):  # Changes the buttons colour when the mouse is over it
        # changes text if the mouse is hovering over it
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True,
                                         self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True,
                                         self.base_color)
