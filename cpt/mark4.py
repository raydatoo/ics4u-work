import arcade
import math
import json

WIDTH = 1350
HEIGHT = 700

# global functions


def count_score(num_list):
    if len(num_list) == 0:
        return 0
    elif num_list[0].time_collected is not None:
        return num_list[0].time_collected*num_list[0].collection_bonus + count_score(num_list[1:])
    else:
        return 0 + count_score(num_list[1:])


def check_name(name):
    with open("scores.json", "r") as f:
        score_dictionary = json.load(f)

    name_list = []
    for key in score_dictionary.keys():
        name_list.append(key)

    if name not in name_list:
        return True
    else:
        return False


def binary_search(lista, target):
    start = 0
    end = len(lista) - 1
    while start <= end:
        mid = math.ceil((start + end) // 2)
        if lista[mid] == target:
            return mid
        elif lista[mid] > target:
            end = mid - 1
        elif lista[mid] < target:
            start = mid + 1
    return -1


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    midpoint = len(numbers)//2
    left_side = merge_sort(numbers[:midpoint])
    right_side = merge_sort(numbers[midpoint:])
    sorted_list = []
    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):

        if left_side[left_marker] < right_side[right_marker]:
            sorted_list.append(left_side[left_marker])
            left_marker += 1

        else:
            sorted_list.append(right_side[right_marker])
            right_marker += 1

    while right_marker < len(right_side):
        sorted_list.append(right_side[right_marker])
        right_marker += 1

    while left_marker < len(left_side):
        sorted_list.append(left_side[left_marker])
        left_marker += 1

    return sorted_list


def save_score(name=None, score=None):
    with open("scores.json", "r") as f:
        score_dictionary = json.load(f)

    name_list = []
    for key in score_dictionary.keys():
        name_list.append(key)

    score_dictionary[name] = score

    with open("scores.json", "w") as f:
        json.dump(score_dictionary, f)

    score_list = []
    for value in score_dictionary.values():
        score_list.append(value)
    score_list = merge_sort(score_list)

    return [len(score_list)-(binary_search(score_list, score)), name, score]


def find_highscore():
    with open("scores.json", "r") as f:
        dictionary = json.load(f)
    high_value = 0
    high_key = None
    for key, value in dictionary.items():
        if value > high_value:
            high_value = value
            high_key = key
    return [high_value, high_key]


# classes

class Player(arcade.Sprite):

    def __init__(self, image):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale=0.25)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0
        self.move_speed = 10
        self.turn_speed = 5
        self.center_x = 35
        self.center_y = 550
        self.angle = 270

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

        # keep player in screen
        if self.center_x < self.width/2:
            self.center_x = self.width/2
        if self.center_x > WIDTH - self.width/2:
            self.center_x = WIDTH - self.width/2
        if self.center_y < self.width/2:
            self.center_y = self.width/2
        if self.center_y > HEIGHT - 100 - self.width/2:
            self.center_y = HEIGHT - 100 - self.width/2


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
        super().__init__(image, scale=0.4)
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.activated = False


class SpinnyTurret(Turret):
    def __init__(self, image, center_x, center_y, angle):
        super().__init__(image, center_x, center_y, angle)
        self.turn_speed = 1


class SmartTurret(Turret):
    def __init__(self, image, center_x, center_y, angle):
        super().__init__(image, center_x, center_y, angle)
        self.angle = 90

    def update(self, target_x, target_y):
        # Convert angle in degrees to radians.
        self.angle = math.degrees(math.atan2(target_y - self.center_y, target_x - self.center_x))-90


class Laser(arcade.Sprite):

    def __init__(self, turret):

        super().__init__()
        self.center_x = turret.center_x
        self.center_y = turret.center_y
        self.angle = turret.angle
        self.change_x = math.cos(math.radians(self.angle + 90)) * 5
        self.change_y = math.sin(math.radians(self.angle + 90)) * 5
        self.texture = arcade.make_soft_square_texture(30, arcade.color.ORANGE, outer_alpha=255)
        self.width = 5


class Barrier(arcade.Sprite):
    def __init__(self, center_x, center_y, angle):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.texture = arcade.make_soft_square_texture(310, arcade.color.RED, outer_alpha=255)
        self.width = 10


class Heart(arcade.Sprite):

    def __init__(self, image, heart_num):

        super().__init__(image)
        self.scale = .75
        self.top = HEIGHT - 20
        self.left = heart_num*75 - 50


class Coin(arcade.Sprite):

    def __init__(self, image, center_x, center_y):
        super().__init__(image, scale=0.05)
        self.center_x = center_x
        self.center_y = center_y
        self.collection_bonus = 50
        self.time_collected = None


class Diamond(Coin):
    def __init__(self, image, center_x, center_y):
        super().__init__(image, center_x, center_y)
        self.scale = 0.25
        self.collection_bonus = 500
        self.time_collected = None


# game

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.BLACK)
        self.player = Player("rokit_ship.png")
        self.barrier_on = True
        self.frame_count = 0
        self.score = 0
        self.turret_list = arcade.SpriteList()
        self.lasers = arcade.SpriteList()
        self.long_lasers = arcade.SpriteList()
        self.heart_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.barrier_turrets = arcade.SpriteList()
        self.barriers = arcade.SpriteList()
        self.recur_list = []

        # set up turrets

        turret = Turret("turret.png",  800, 450, 90)
        self.turret_list.append(turret)
        turret = Turret("turret.png",  450, 100, 0)
        self.turret_list.append(turret)
        turret = Turret("turret.png",  1100, 125, 90)
        self.turret_list.append(turret)
        turret = Turret("turret.png",  1300, 250, 90)
        self.turret_list.append(turret)
        turret = Turret("turret.png",  900, 35, 0)
        self.turret_list.append(turret)
        turret = Turret("turret.png",  1200, 600, 180)
        self.turret_list.append(turret)
        turret = SpinnyTurret("turret.png",  1000, 600, 269)
        self.turret_list.append(turret)
        turret = SpinnyTurret("turret.png",  600, 600, 91)
        self.turret_list.append(turret)

        self.smart_turret = SmartTurret("turret.png",  25, 25, 300)

        barrier_turret = Turret("turret.png",  39, 300, 270)
        self.barrier_turrets.append(barrier_turret)
        barrier_turret = Turret("turret.png",  300, 39, 0)
        self.barrier_turrets.append(barrier_turret)

        # set up hearts

        heart = Heart("heart.jpg", 1)
        self.heart_list.append(heart)
        heart = Heart("heart.jpg", 2)
        self.heart_list.append(heart)
        heart = Heart("heart.jpg", 3)
        self.heart_list.append(heart)
        heart = Heart("heart.jpg", 4)
        self.heart_list.append(heart)
        heart = Heart("heart.jpg", 5)
        self.heart_list.append(heart)

        # set up coins

        coin = Coin("coin.png", 800, 550)
        self.coin_list.append(coin)
        self.recur_list.append(coin)

        coin = Coin("coin.png", 380, 50)
        self.coin_list.append(coin)
        self.recur_list.append(coin)

        coin = Coin("coin.png", 200, 400)
        self.coin_list.append(coin)
        self.recur_list.append(coin)

        coin = Coin("coin.png", 1250, 500)
        self.coin_list.append(coin)
        self.recur_list.append(coin)

        coin = Coin("coin.png", 200, 300)
        self.coin_list.append(coin)
        self.recur_list.append(coin)

        coin = Diamond("dimond.png", 100, 100)
        self.coin_list.append(coin)
        self.recur_list.append(coin)

        # set up barrier

        barrier = Barrier(300, 150, 0)
        self.barriers.append(barrier)
        barrier = Barrier(150, 300, 270)
        self.barriers.append(barrier)

        # activate initial turrets

        self.turret_list[0].activated = True
        self.turret_list[1].activated = True
        self.turret_list[2].activated = True
        self.turret_list[3].activated = True
        self.turret_list[4].activated = True
        self.turret_list[5].activated = True
        self.turret_list[6].activated = True
        self.turret_list[7].activated = True

    # class functions

    def countdown(self):
        if self.frame_count < 90:
            return str(math.ceil((90-self.frame_count)/30))
        else:
            return "go"

    # the draw

    def on_draw(self):
        arcade.start_render()  # keep as first line

        self.barriers.draw()
        self.lasers.draw()
        self.barrier_turrets.draw()
        self.turret_list.draw()
        self.smart_turret.draw()
        self.player.draw()
        self.heart_list.draw()
        self.coin_list.draw()

        arcade.draw_text(f"Score: {self.score}", 1100, 650, arcade.color.WHITE, 30)

        if self.frame_count < 120:
            arcade.draw_text(self.countdown(), 1, 1, arcade.color.WHITE, 500)

    # the update

    def update(self, delta_time):

        self.frame_count += 1

        self.player.update()
        self.turret_list.update()
        self.lasers.update()
        self.coin_list.update()
        self.smart_turret.update(self.player.center_x, self.player.center_y)

        # spinny turret

        if self.frame_count % 3 == 0:
            for turret in self.turret_list[6:8]:
                turret.angle -= turret.turn_speed
                if turret.angle == 270 or turret.angle == 90:
                    turret.turn_speed = -turret.turn_speed

        # shoot lasers

        if self.frame_count % 120 == 0:
            for turret in self.turret_list:
                if turret.activated is True:
                    laser = Laser(turret)
                    self.lasers.append(laser)

        if self.frame_count % 40 == 0:
            if self.smart_turret.activated is True:
                laser = Laser(self.smart_turret)
                self.lasers.append(laser)

        # check if laser hit

        for laser in self.lasers:
            hit = arcade.check_for_collision(laser, self.player)
            if hit is True:
                laser.remove_from_sprite_lists()

                self.player.center_x = 35
                self.player.center_y = 550
                self.player.angle = 270
                self.heart_list[-1].remove_from_sprite_lists()
                print(len(self.heart_list))

        if self.player.collides_with_list(self.turret_list) or self.player.collides_with_list(self.barrier_turrets) or self.player.collides_with_list(self.barriers):
            self.player.center_x = 35
            self.player.center_y = 550
            self.player.angle = 270
            self.heart_list[-1].remove_from_sprite_lists()
            print(len(self.heart_list))

        # kill laser when it leaves screen to save memory

        for laser in self.lasers:
            if laser.top < 0:
                laser.remove_from_sprite_lists()
            elif laser.bottom > HEIGHT:
                laser.remove_from_sprite_lists()
            if laser.right < 0:
                laser.remove_from_sprite_lists()
            elif laser.left > WIDTH:
                laser.remove_from_sprite_lists()

        # collect coins

        for coin in self.coin_list:
            hit = arcade.check_for_collision(coin, self.player)
            if hit is True:
                coin.remove_from_sprite_lists()
                coin.time_collected = 300-self.frame_count//60

        self.score = count_score(self.recur_list)

        if self.score > 9999999:
            self.score = 9999999

        # off barrier

        if len(self.coin_list) == 1:
            for barrier in self.barriers:
                barrier.remove_from_sprite_lists()
            self.smart_turret.activated = True

        # finish game

        if self.player.center_x > 1300 and self.player.center_y < 50:
            finish_view = FinishView()
            self.score += 100*(300-self.frame_count//60)
            finish_view.score = self.score
            finish_view.win = True
            self.window.show_view(finish_view)

        # die

        if len(self.heart_list) == 0:
            finish_view = FinishView()
            finish_view.score = self.score
            finish_view.win = False
            self.window.show_view(finish_view)

    # key functions

    def on_key_press(self, key, modifiers):

        # moving
        if key == arcade.key.UP and self.frame_count > 120:
            self.player.speed = self.player.move_speed
        elif key == arcade.key.DOWN and self.frame_count > 120:
            self.player.speed = -self.player.move_speed

        # turning
        elif key == arcade.key.LEFT:
            self.player.change_angle = self.player.turn_speed
        elif key == arcade.key.RIGHT:
            self.player.change_angle = -self.player.turn_speed

        # cheat codes in case you suck

        elif key == arcade.key.KEY_0:
            self.window.show_view(FinishView())
            FinishView.win = True
            FinishView.score = 5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_angle = 0


class FinishView(arcade.View):

    def on_draw(self):
        arcade.start_render()

        # print win/lose screen
        if self.win is False:
            arcade.set_background_color(arcade.color.RED)
            arcade.draw_text("You Lose", 500, 500, arcade.color.BLACK, 100)
        elif self.win is True:
            arcade.set_background_color(arcade.color.GREEN)
            arcade.draw_text("You Win", 500, 500, arcade.color.BLACK, 100)

        # buttons

        arcade.draw_text(f"your score was: {self.score}", 500, 450, arcade.color.BLACK, 50)
        arcade.draw_rectangle_filled(WIDTH//2, 300, 300, 100, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(WIDTH//2, 100, 300, 100, arcade.color.ORANGE)
        arcade.draw_text("Click here to try  \n again", WIDTH//2 - 100, 300, arcade.color.BLACK, 25)
        arcade.draw_text("Click here to submit  \n score", WIDTH//2 - 100, 75, arcade.color.BLACK, 25)

    # click buttons

    def on_mouse_press(self, _x, _y, _button, _modifiers):

        if 300 < _x < 900 and 250 < _y < 400:
            game_view = GameView()
            self.window.show_view(game_view)

        elif 300 < _x < 900 and 50 < _y < 200:
            score_view = ScoreView()
            score_view.score = self.score
            self.window.show_view(score_view)


class ScoreView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.name = " "
        self.submit = False
        self.name_taken = False
        self.show_time = 0

    def on_draw(self):
        arcade.start_render()

        # typing name
        if self.submit is False:
            arcade.draw_text(self.name, 100, 100, arcade.color.WHITE, 50)

        # highscore
        else:
            arcade.draw_text(f"{find_highscore()[1]} : {find_highscore()[0]}", 300, 30, arcade.color.WHITE, 50)

        # name taken
        if self.name_taken is True:
            arcade.draw_text("no", 500, 500, arcade.color.WHITE, 50)

    # flash message if name taken

    def update(self, delta_time):

        if self.name_taken is True:
            self.show_time += 1

        if self.show_time > 60:
            self.name_taken = False
            self.show_time = 0

    # type name

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE and len(self.name) > 1 and self.submit is False:
            self.name = self.name[:-1]
        elif key != arcade.key.BACKSPACE and key != arcade.key.ENTER and len(self.name) < 8 and self.submit is False:
            self.name += chr(key)

    # enter and check name/score
    def on_key_release(self, key, modifiers):
        if key == arcade.key.ENTER:

            if check_name(self.name) is True:
                self.submit = True
                save_score(self.name, self.score)

            else:
                self.name_taken = True


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.show_view(GameView())
    arcade.run()


if __name__ == "__main__":
    main()
