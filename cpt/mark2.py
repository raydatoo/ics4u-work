import arcade
import math 

WIDTH = 1920
HEIGHT = 1080


#turret class

class Turret(arcade.Sprite):
    '''Turret class
    Attributes:
        image (image file): the name of the food
        center_x (int): x pos of turret
        center_y (int): y pos of turret
        angle (int): angle of turret
        '''

    def __init__(self, image, center_x, center_y, angle):
        """Create a Turret object.
        Args:
            image: file path of image
            center_x: x pos of turret
            center_y: y pos of turret
            angle: angle of turret
        """
        # Call the parent init
        super().__init__(image)

        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.scale = 0.5
    


        
#player class

class Player(arcade.Sprite):

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

        self.move_speed = 10
        self.turn_speed = 5

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



#game class


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.player = Player("rokit_ship.png", 0.5)

        self.turret_list = arcade.SpriteList()

        self.turret1 = Turret("turret.png",  700, 1000, 270)
        self.turret2 = Turret("turret.png",  200, 800, 0)
        self.turret3 = Turret("turret.png",  500, 600, 270)
        self.turret4 = Turret("turret.png",  1800, 100, 90)
        self.turret5 = Turret("turret.png",  1600, 500, 180)
        self.turret6 = Turret("turret.png",  200, 100, 90)
        self.turret7 = Turret("turret.png",  1300, 800, 270)
        self.turret8 = Turret("turret.png",  800, 350, 0)

        self.turret_list.append(self.turret1)
        self.turret_list.append(self.turret2)
        self.turret_list.append(self.turret3)
        self.turret_list.append(self.turret4)
        self.turret_list.append(self.turret5)
        self.turret_list.append(self.turret6)
        self.turret_list.append(self.turret7)
        self.turret_list.append(self.turret8)




        
        self.lasers = arcade.SpriteList()

        self.frame_count = 0

    #function that makes the lasors

    def lasor(self, turret):
        laser = arcade.Sprite()
        laser.center_x = turret.center_x
        laser.center_y = turret.center_y
        laser.tangle = turret.angle
        laser.angle = turret.angle 
        laser.texture = arcade.make_soft_square_texture(30, arcade.color.ORANGE, outer_alpha=255)
        laser.width = 5
        if laser.tangle == 0:
            laser.change_y = 3
        elif laser.tangle == 90:
            laser.change_x = -3
        elif laser.tangle == 180:
            laser.change_y = -3
        elif laser.tangle == 270:
            laser.change_x = 3
        
        self.lasers.append(laser)

        
        


    #the draw

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()
        self.turret_list.draw()
        self.lasers.draw()
        
    #the update 

    def update(self, delta_time):
        
        self.frame_count += 1
        self.player.update()
        self.turret1.update()
        self.lasers.update()

        #keep player in screen

        if self.player.center_x < self.player.width/2:
            self.player.center_x = self.player.width/2
        if self.player.center_x > WIDTH - self.player.width/2:
            self.player.center_x = WIDTH - self.player.width/2
        if self.player.center_y < self.player.width/2:
            self.player.center_y = self.player.width/2
        if self.player.center_y > HEIGHT - self.player.width/2:
            self.player.center_y = HEIGHT - self.player.width/2

        #shoot laser every this many frames

        if self.frame_count %120 == 0:
            for turret in self.turret_list:
                self.lasor(turret)
                

        #kill laser when it leaves screen to save memory

        for laser in self.lasers:
            if laser.top < 0:
                laser.remove_from_sprite_lists()
            elif laser.bottom > HEIGHT:
                laser.remove_from_sprite_lists()
            if laser.right < 0:
                laser.remove_from_sprite_lists()
            elif laser.left > WIDTH:
                laser.remove_from_sprite_lists()


        # check if hit laser

        for laser in self.lasers:
            hit = arcade.check_for_collision(laser, self.player)
            if hit == True:
                laser.remove_from_sprite_lists()
                print("oof")


        

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        #moving
        if key == arcade.key.UP:
            self.player.speed = self.player.move_speed
        elif key == arcade.key.DOWN:
            self.player.speed = -self.player.move_speed

        #turning
        elif key == arcade.key.LEFT:
            self.player.change_angle = self.player.turn_speed
        elif key == arcade.key.RIGHT:
            self.player.change_angle = -self.player.turn_speed

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