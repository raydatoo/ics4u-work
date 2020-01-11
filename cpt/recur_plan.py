'''
import json
import math

from typing import List

def check_name(lista, name):
    if name not in lista:
        return name
    elif name in lista:
        return check_name(lista, name + "x")

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
    # base case
    if len(numbers) == 1:
        return numbers

    midpoint = len(numbers)//2

    # two recursive steps
    # mergesort left
    left_side = merge_sort(numbers[:midpoint])
    # mergesort right
    right_side = merge_sort(numbers[midpoint:])
    # merge the two together
    sorted_list = []

    # loop through both lists with two markers
    left_marker = 0
    right_marker = 0
    while left_marker < len(left_side) and right_marker < len(right_side):
        # if right value less than left value, add right value to sorted, increase right marker
        if left_side[left_marker] < right_side[right_marker]:
            sorted_list.append(left_side[left_marker])
            left_marker += 1
        # if left value less than right value, add left value to sorted, increase left marker
        else:
            sorted_list.append(right_side[right_marker])
            right_marker += 1
    
    # create a while loop to gather the rest of the values from either list
    while right_marker < len(right_side):
        sorted_list.append(right_side[right_marker])
        right_marker += 1
    
    while left_marker < len(left_side):
        sorted_list.append(left_side[left_marker])
        left_marker += 1
    
    # return the sorted list
    return sorted_list

def save_score(name = None, score = None):
    with open("scores.json", "r") as f:
        score_dictionary = json.load(f)
    
    name_list = []
    for key in score_dictionary.keys():
        name_list.append(key)
    
    if name != None:
        name = check_name(name_list, name)
        score_dictionary[name] = score

    with open("scores.json", "w") as f:
        json.dump(score_dictionary, f)

    score_list = []
    for value in score_dictionary.values():
        score_list.append(value)
    score_list = merge_sort(score_list)

    
    return[len(score_list)-(binary_search(score_list, score)), name, score]

def find_highscore():
    with open("scores.json", "r") as f:
        dictionary = json.load(f)
    high_value = 0
    high_key = None
    for key,value in dictionary.items():
        if value > high_value:
            high_value = value
            high_key = key
    return high_value, high_key


print(save_score("john", 6))


'''

import arcade
import math
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Bullets Enemy Aims Example"



class MyGame(arcade.Window):
    """ Main application class """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)


        arcade.set_background_color(arcade.color.BLACK)



        self.enemy_list = None

        self.player_list = None
        self.player = None

    def setup(self):
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Add player ship
        self.player = arcade.Sprite("rokit_ship.png", 0.5)
        self.player_list.append(self.player)

        # Add top-left enemy ship
        enemy = arcade.Sprite("turret.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

       
    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.enemy_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

     

        # Loop through each enemy that we have
        for enemy in self.enemy_list:
   
            
    
             

            enemy.angle = math.degrees(math.atan2(self.player.center_y - enemy.center_y, self.player.center_x - enemy.center_x))-90

            
            

       
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = y


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()