import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [i for i, j in kwargs.items() for _ in range(j)]

    def draw(self, number):
        ballsDrawed = []

        if int(number) > len(self.contents):
            number = len(self.contents)

        for _ in range(number):
            ballsDrawed.append(self.contents.pop(random.randrange(len(self.contents))))

        return ballsDrawed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        balls_drawed = copy_hat.draw(num_balls_drawn)
        if all(balls_drawed.count(color) >= count for color, count in expected_balls.items()):
            success += 1
    
    return success / num_experiments

hat = Hat(black=6, red=4, green=3)
print(hat.draw(1))
print(hat.contents)

probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)