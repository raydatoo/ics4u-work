import arcade
import math 

WIDTH = 800
HEIGHT = 800

class Turret(arcade.Sprite):

    def __init__(self, image, scale, center_x, center_y):
        # Call the parent init
        super().__init__(image, scale)

        self.center_x = center_x
        self.center_y = center_y



        
    



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






class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.player = Player("rokit_ship.png", 0.5)
        
        self.turret1 = Turret("turret.png", 0.5, 700, 800)

        self.laser_texture = arcade.make_soft_square_texture(30, arcade.color.ORANGE, outer_alpha=255)
        self.lasers = arcade.SpriteList()

        self.frame_count = 0

        
        







    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()
        self.turret1.draw()
        self.lasers.draw()

    def update(self, delta_time):
        
        self.frame_count += 1
        self.player.update()
        self.turret1.update()
        self.lasers.update()

        if self.player.center_x < 0:
            self.player.center_x = 0
        if self.player.center_x > WIDTH:
            self.player.center_x = WIDTH
        if self.player.center_y < 0:
            self.player.center_y = 0
        if self.player.center_y > HEIGHT:
            self.player.center_y = HEIGHT

        if self.frame_count %60 == 0:
            laser = arcade.Sprite()
            laser.center_x = self.turret1.center_x
            laser.center_y = self.turret1.center_y
            laser.change_y = -3
            laser.texture = self.laser_texture
            laser.width = 5

            self.lasers.append(laser)

        if self.player.collides_with_list(self.lasers):
            print("oof")






    
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







def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()