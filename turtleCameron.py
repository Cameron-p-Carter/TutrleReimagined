import turtle
import time
import random



class InvalidInputException(Exception):
    def __init__(self, message, input_type):
        super().__init__(message)
        self.input_type = input_type

class Racer(turtle.Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color(color)
        self.shape('turtle')
        self.left(90)
        self.penup()
        self.setpos(position)
        self.pendown()

class TurtleRace:
    def __init__(self, width, height, colors):
        self.width = width
        self.height = height
        self.colors = colors

    def get_number_of_racers(self):
        while True:
            try:
                racers = input('Enter the number of racers (2 - 10): ')
                if not racers.isdigit():
                    raise InvalidInputException('Input must be a number, Try Again!', 'non-numeric')

                racers = int(racers)

                if not (2 <= racers <= 10):
                    raise InvalidInputException('Number must be in between 2-10. Try Again!', 'out-of-range')

                return racers
            except InvalidInputException as e:
                print(e)
                continue

    def create_racers(self, num_racers):
        spacing_x = self.width // (num_racers + 1)
        return [Racer(color, (-self.width // 2 + (i + 1) * spacing_x, -self.height // 2 + 20)) for i, color in enumerate(self.colors[:num_racers])]

    def race(self, racers):
        while True:
            for racer in racers:
                distance = random.randrange(1, 20)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= self.height // 2 - 10:
                    return racer.color()[0]

    def init_turtle(self):
        screen = turtle.Screen()
        screen.setup(self.width, self.height)
        screen.title('Turtle Racing!')

    def run_race(self):
        num_racers = self.get_number_of_racers()
        self.init_turtle()

        racers = self.create_racers(num_racers)
        winner = self.race(racers)

        print("The winner is the turtle with color:", winner)
        time.sleep(5)

if __name__ == "__main__":
    WIDTH, HEIGHT = 700, 600
    COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

    race_game = TurtleRace(WIDTH, HEIGHT, COLORS)
    race_game.run_race()