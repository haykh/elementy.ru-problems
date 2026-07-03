class invPendulum:
    def __init__(self, node, bob):
        self.node = node
        self.bob = bob
        self.node_init = node.copy()
        self.bob_init = bob.copy()
    def show(self, t):
        stroke(0, 0, 255)
        strokeWeight(1)
        theta = atan(amplitude * sin(-t) / plen)
        nx = self.node.x
        ny = self.node.y
        bx = self.bob.x
        by = self.bob.y
        line(nx, ny, nx + (bx - nx) * 1.25, ny + (by - ny) * 1.25)
        
        stroke(255, 0, 0)
        strokeWeight(1)
        theta = atan(amplitude * sin(-t) / plen)
        nx = self.node.x
        ny = self.node.y
        bx = self.node.x + plen * cos(angle + 0.01 * t)
        by = self.node.y - plen * sin(angle + 0.01 * t)
        line(nx, ny, nx + (bx - nx) * 1.5, ny + (by - ny) * 1.5)
        
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
        theta = atan(amplitude * sin(-t) / plen)
        self.node.y = self.node_init.y + amplitude * sin(t)
        self.bob.x = self.node.x + plen * cos(angle + 0.01 * t - 0.5 * theta)
        self.bob.y = self.node.y - plen * sin(angle + 0.01 * t - 0.5 * theta)
        stroke(0)
        strokeWeight(1)
        line(self.node.x, self.node_init.y - amplitude, self.node.x, self.node_init.y + amplitude)
    def jerkBob(self, t):
        thetamax = atan(1.0 * amplitude / plen)
        thmin = (-PI/2 + angle - 0.01 * t - 0.5 * thetamax)
        thmax = (-PI/2 + angle - 0.01 * t + 0.5 * thetamax)
        theta = atan(amplitude * sin(-t) / plen)
        self.bob.x = self.node_init.x + plen * cos(angle + 0.01 * t - 0.5 * theta)
        self.bob.y = self.node_init.y - plen * sin(angle + 0.01 * t - 0.5 * theta)
        stroke(0)
        strokeWeight(1)
        noFill()
        arc(self.node_init.x, self.node_init.y, 2*plen, 2*plen, thmin, thmax);

angle = PI / 4.0
amplitude = 60
plen = 150
dt = 0.1

def setup():
    global pendulum1, pendulum2, time
    size(800, 450)
    f = createFont("Georgia", 8, True) 
    textFont(f, 24)
    textAlign(CENTER)
    xc = width/4 - plen/2
    yc = 2*height/3
    xc1 = xc + plen * cos(angle)
    yc1 = yc - plen * sin(angle)
    pendulum1 = invPendulum(PVector(xc, yc), 
                            PVector(xc1, yc1))
    xc = 3*width/4 - plen/2
    yc = 2*height/3
    xc1 = xc + plen * cos(angle)
    yc1 = yc - plen * sin(angle)
    pendulum2 = invPendulum(PVector(xc, yc), 
                            PVector(xc1, yc1))
    time = 0

def draw():
    global pendulum1, pendulum2, time
    background(217)
    text(u"лабораторная система", width/4, height/8)
    pendulum1.show(time)
    pendulum1.jerkNode(time)
    text(u"неинерциальная система", 3*width/4, height/8)
    pendulum2.show(time)
    pendulum2.jerkBob(time)
    text(u"(без гравитации)", width/2, height-height/8)
    time += dt
    if (time > 16 * PI):
        noLoop();
    saveFrame("anim-######.png");
