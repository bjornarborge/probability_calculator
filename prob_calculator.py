import copy
import random
# Consider using the modules imported above.

# 1. Create a Hat class in prob_calculator.py. 
# The class should take a variable number of arguments that specify the color of a ball that should be added to the hat. 
class Hat:
    # The arguments passed into the hat object upon creation should be converted to a contents instance variable.
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    # The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat.
    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]

# 2. Create an experiment function in prob_calculator.py that accepts the following arguments:
# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
# The experiment function should return a probability.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments