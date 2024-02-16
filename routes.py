import random
from flask import Blueprint

combat = Blueprint('combat', __name__) 

@combat.route('/roll', methods = ['GET'])
def roll_combat():
    i = random.randint(1, 20)
    if i == 1:
        return 'critical miss!'
    if i == 20:
        return 'critical hit!'
    return 'you swing for ' + str(i) + ' damage!'

@combat.route('/roll.advantage', methods = ['GET'])
def roll_advantage():
    first = random.randint(1,20)
    second = random.randint(1,20)
    if first > second:
        return 'you rolled' + str(first) + 'points!'
    if second > first:
        return 'you rolled' + str(second) + 'points!'

@combat.route('/roll.disadvantage', methods = ['GET'])
def roll_disadvantage ():
    first = random.randint(1,20)
    second = random.randint(1,20)
    if first < second:
        return 'you rolled' + str(first) + 'points!'
    if second < first: 
        return 'you rolled' + str(second)  + 'points!'