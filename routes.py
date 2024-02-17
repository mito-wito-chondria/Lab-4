import random
from flask import Blueprint

combat = Blueprint('combat', __name__) 

@combat.route('/roll', methods = ['GET'])
def roll_combat():
# the dice has 20 sides 
    i = random.randint(1, 20)
# if it randomly rolls a 1 its a critical miss
    if i == 1:
        return 'critical miss!'
# if it randomly rolls a 20 its a critical hit
    if i == 20:
        return 'critical hit!'
# if its any other number it just returns saying what number you rolled
    return 'you swing for ' + str(i) + ' damage!'

@combat.route('/roll.advantage', methods = ['GET'])
def roll_advantage():
# randomly generates out of the 20 sides for the first roll
    first = random.randint(1,20)
 # randomly generates out of the 20 sides for the second roll
    second = random.randint(1,20)
# if the first is greater return that one
    if first > second:
        return 'you rolled ' + str(first) + ' points!'
# if its not then it moves on and returns the second as greater
    if second > first:
        return 'you rolled ' + str(second) + ' points!'


@combat.route('/roll.disadvantage', methods = ['GET'])
def roll_disadvantage ():
# random roll first
    first = random.randint(1,20)
# second random roll 
    second = random.randint(1,20)
# if the first is less then return it with the value 
    if first < second:
        return 'you rolled ' + str(first) + ' points!'
# moves on to the next where the if the second is less it gets returned
    if second < first: 
        return 'you rolled ' + str(second)  + ' points!'