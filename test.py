import unittest
import matter


def make_boxes():
    Bodies = Matter.Bodies
    # create two boxes and a ground
    boxA = Bodies.rectangle(400, 200, 80, 80)
    boxB = Bodies.rectangle(450, 50, 80, 80)
    ground = Bodies.rectangle(400, 610, 810, 60, { 'isStatic': True })
    return boxA, boxB, ground

def drop():
    # module aliases
    Engine = Matter.Engine
    Render = Matter.Render
    World = Matter.World

    # create an engine
    engine = Engine.create()

    # create a renderer
    render = Render.create({
        'element': document.body,
        'engine': engine
    })



    # add all of the bodies to the world
    World.add(engine.world, make_boxes())

    # run the engine
    Engine.run(engine)

    # run the renderer
    Render.run(render)

class Test(unittest.TestCase):

    def test_show(self):
        matter.show([make_boxes, drop])

if __name__ == '__main__':
    unittest.main()