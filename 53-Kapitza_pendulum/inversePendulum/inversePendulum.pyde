class invPendulum:
    def __init__(self, node, bob):
        self.node = node
        self.bob = bob
        self.node_init = node.copy()
        self.bob_init = bob.copy()
    def show(self):
        stroke(27)
        strokeWeight(2)
        line(self.node.x, self.node.y, self.bob.x, self.bob.y)
        strokeWeight(1)
        fill(255)
        ellipseMode(CENTER)
        circle(self.bob.x, self.bob.y, 20)
        fill(27)
        ellipseMode(CENTER)
        circle(self.node.x, self.node.y, 5)
    def jerkNode(self, t):
        self.node.y = self.node_init.y + amplitude * sin(t)
        self.bob.x = self.node.x + sqrt(plen**2 - (self.node.y - self.bob.y)**2)
        stroke(0)
        strokeWeight(1)
        line(self.node.x, self.node_init.y - amplitude, self.node.x, self.node_init.y + amplitude)
    def jerkBob(self, t):
        thetamax = atan(1.0 * amplitude / plen)
        theta = atan(amplitude * sin(-t) / plen)
        self.bob.x = self.node_init.x + plen * cos(theta)
        self.bob.y = self.node_init.y + plen * sin(theta)
        stroke(0)
        strokeWeight(1)
        noFill()
        arc(self.node_init.x, self.node_init.y, 2*plen, 2*plen, -thetamax, thetamax);

amplitude = 60
plen = 150
dt = 0.1

def setup():
    global pendulum1, pendulum2, time
    size(800, 300)
    f = createFont("Georgia", 8, True) 
    textFont(f, 24)
    textAlign(CENTER)
    pendulum1 = invPendulum(PVector(width/4 - plen/2, height/2), 
                            PVector(width/4 + plen/2, height/2))
    pendulum2 = invPendulum(PVector(3*width/4 - plen/2, height/2), 
                            PVector(3*width/4 + plen/2, height/2))
    time = 0

def draw():
    global pendulum1, pendulum2, time
    background(217)
    text(u"лабораторная система", width/4, height/8)
    pendulum1.show()
    pendulum1.jerkNode(time)
    text(u"неинерциальная система", 3*width/4, height/8)
    pendulum2.show()
    pendulum2.jerkBob(time)
    text(u"(без гравитации)", width/2, height-height/8)
    time += dt
    if (time > 2 * PI):
        noLoop();
    saveFrame("anim-######.png");
