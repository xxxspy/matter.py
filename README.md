# matter.py
Python wraper for matter.js

# install

- install flexx v0.4

```
pip install https://github.com/flexxui/flexx/archive/master.zip

```

- install matter.py

```
pip install https://github.com/xxxspy/matter.py/archive/master.zip
```

# example

Run the code below , and you will see webbrowser opened a NamedTemporaryFile: 

```python
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

if __name__ == '__main__':
    matter.show([make_boxes, drop])
```

You will see:

<img src="example.gif" />