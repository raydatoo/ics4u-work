import arcade
import math 

WIDTH = 1920
HEIGHT = 1080

class Turret(arcade.Sprite):

    def __init__(self, image, center_x, center_y, angle):
        # Call the parent init
        super().__init__(image)

        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.scale = 0.5
    




        
    



class Player(arcade.Sprite):

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

        self.center_x = 400
        self.center_y = 400

        self.hearts = 3

    
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

        self.turret_list = arcade.SpriteList()

        self.turret1 = Turret("turret.png",  700, 1000, 270)
        self.turret2 = Turret("turret.png",  200, 800, 270)
        self.turret3 = Turret("turret.png",  500, 600, 270)
        self.turret4 = Turret("turret.png",  1800, 100, 270)
        self.turret5 = Turret("turret.png",  450, 100, 270)
        self.turret6 = Turret("turret.png",  200, 100, 270)
        self.turret7 = Turret("turret.png",  600, 40, 270)
        self.turret8 = Turret("turret.png",  800, 350, 270)

        self.turret_list.append(self.turret1)
        self.turret_list.append(self.turret2)
        self.turret_list.append(self.turret3)
        self.turret_list.append(self.turret4)
        self.turret_list.append(self.turret5)
        self.turret_list.append(self.turret6)
        self.turret_list.append(self.turret7)
        self.turret_list.append(self.turret8)




        self.laser_texture = arcade.make_soft_square_texture(30, arcade.color.ORANGE, outer_alpha=255)
        self.lasers = arcade.SpriteList()

        self.frame_count = 0

        
        







    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()
        self.turret_list.draw()
        self.lasers.draw()

    def update(self, delta_time):
        
        self.frame_count += 1
        self.player.update()
        self.turret1.update()
        self.lasers.update()

        if self.player.center_x < self.player.width/2:
            self.player.center_x = self.player.width/2
        if self.player.center_x > WIDTH - self.player.width/2:
            self.player.center_x = WIDTH - self.player.width/2
        if self.player.center_y < self.player.width/2:
            self.player.center_y = self.player.width/2
        if self.player.center_y > HEIGHT - self.player.width/2:
            self.player.center_y = HEIGHT - self.player.width/2

        if self.frame_count %60 == 0:
            for turret in self.turret_list:
                laser = arcade.Sprite()
                laser.center_x = turret.center_x
                laser.center_y = turret.center_y
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
            self.player.speed = 20
        elif key == arcade.key.DOWN:
            self.player.speed = -20

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