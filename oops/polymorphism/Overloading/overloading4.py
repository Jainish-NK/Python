class Bird:

    def fly(self):
        print("bird is flying....")

class Airplane:

    def fly(self):
        print("airplane is flying...")


def lets_fly(thing):
    thing.fly()

lets_fly(Airplane())
lets_fly(Bird())

class Circle:

    def draw(self):
        print("Drawing a Circle")

class Rectangle:

    def draw(self):
        print("Drawing a rectangle")

def render_shap(shap):
    shap.draw()

render_shap(Circle())
render_shap(Rectangle())


