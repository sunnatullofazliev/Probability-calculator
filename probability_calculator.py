import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError("At least one ball is needed")
        self.contents = [color for color, count in kwargs.items() for i in range(count)]

    def draw(self, n):
        drawn = []
        if n > len(self.contents):
            for i in range(len(self.contents)):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn.append(ball)
        else: 
            for i in range(n):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn.append(ball)
        return drawn

def experiment(*, hat, expected_balls, num_balls_drawn, num_experiments):   
    m = 0
    for _ in range(num_experiments): 
        hat_copy = copy.deepcopy(hat)
        expected_balls_list = [color for color, count in expected_balls.items() for i in range(count)]
        drawn = hat_copy.draw(num_balls_drawn) 
        if all(drawn.count(color) >= expected_balls_list.count(color) for color in set(expected_balls_list)):
            m += 1                                         
    return m / num_experiments   