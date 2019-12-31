import arcade
import math 

WIDTH = 800
HEIGHT = 800

class Player(arcade.Sprite):

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

        self.center_x = 400
        self.center_y = 400

    
    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)


-----------------------------------------------------------------------

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.player = Player("rokit_ship.png", 0.5)
        
   ----------------------------------------------------------------------     


    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()

    def update(self, delta_time):
        
        self.player.update()


---------------------------------------------------------------------
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Forward/back
        if key == arcade.key.UP:
            self.player.speed = 5
        elif key == arcade.key.DOWN:
            self.player.speed = -5

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.player.change_angle = 5
        elif key == arcade.key.RIGHT:
            self.player.change_angle = -5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_angle = 0





----------------------------------------------------

def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()