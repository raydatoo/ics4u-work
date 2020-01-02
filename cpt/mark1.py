import arcade

WIDTH = 800
HEIGHT = 800


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.player = arcade.Sprite(center_x=100, center_y=200)
        self.player.texture = arcade.make_soft_square_texture(20, arcade.color.BLUE)
        self.player.width = 10

        self.turret1 = arcade.Sprite(center_x= 500, center_y=700)
        self.turret1.texture = arcade.make_soft_square_texture(50,arcade.color.ORANGE,outer_alpha=255)
        self.turret1.width = 80


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

        for laser in self.lasers:
            if laser.top < 0:
                laser.remove_from_sprite_lists()

        
        
        if self.player.collides_with_list(self.lasers):
            arcade.set_background_color(arcade.color.BLACK)

        print(len(self.lasers))


     
    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.LEFT:
            self.player.change_x = -10
        elif key == arcade.key.RIGHT:
            self.player.change_x = 10
        elif key == arcade.key.UP:
            self.player.change_y = 10
        elif key == arcade.key.DOWN:
            self.player.change_y = -10
        
        
        
        
            
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        



def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()



