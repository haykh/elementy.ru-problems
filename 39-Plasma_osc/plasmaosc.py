#!/usr/bin/env python

from manimlib.imports import *
import numpy as np

GLOBAL_XMAX = 7
GLOBAL_YMAX = 4
GLOBAL_MODES = 4
GLOBAL_T = 20

class PlasmaTh(Scene):
    CONFIG = {
        "radius": 0.15,
        "e_col": RED_C, "p_col": BLUE_C,
        "linew": 1, "opac": 0.2,
        "xmax": GLOBAL_XMAX, "ymax": GLOBAL_YMAX,
        "dt": 0.1
    }
    class Particle():
        def __init__(self, x0, y0, obj):
            self.obj = obj
            self.x = x0
            self.y = y0
            self.obj.move_to([self.x, self.y, 0])

            def update(myobj):
                self.x += 0.05 * np.random.uniform(-1, 1)
                self.y += 0.05 * np.random.uniform(-1, 1)
                myobj.move_to([self.x, self.y, 0])
            self.obj.add_updater(update)

    def construct(self):
        self.fps = self.camera.frame_rate
        self.duration = 2 * GLOBAL_T / (self.fps * self.dt)

        TIMER_ = TextMobject("TIMER").move_to([-1000, -1000, 0])
        self.add(TIMER_)

        N = 300
        # N = 50
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(0, 0.2)) for i in range(N)]
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(-0.2, 0)) for i in range(N)]
        N = 100
        # N = 20
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(0, 0.4)) for i in range(N)]
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(-0.4, 0)) for i in range(N)]
        N = 20
        # N = 5
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), +1) for i in range(N)]
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), -1) for i in range(N)]

        self.play(Write(TIMER_), run_time=self.duration)

    def makeParticle(self, x, y, ch):
        col = (self.e_col if (ch > 0) else self.p_col)
        sign = ("+" if (ch > 0) else "-")
        op = np.abs(ch)
        circ = Circle(radius=self.radius,
                      color=col, stroke_width=self.linew,
                      fill_opacity=self.opac*op, stroke_opacity=op)
        sign = TexMobject(sign, color=col, fill_opacity=op).scale((self.radius / 0.3))
        obj = VGroup(circ, sign)
        prtl = self.Particle(x, y, obj)
        self.add(prtl.obj)
        return prtl

class PlasmaOsc(Scene):
    CONFIG = {
        "radius": 0.15,
        "e_col": RED_C, "p_col": BLUE_C, "efield_col": TEAL_B, "efield_opac": 0.3,
        "linew": 1, "opac": 0.2,
        "xmax": GLOBAL_XMAX / GLOBAL_MODES, "ymax": GLOBAL_YMAX,
        "dt": 0.1
    }
    class Particle():
        def __init__(self, x0, y0, m, obj, dt, ch):
            self.ch = np.sign(ch)
            self.obj = obj
            self.x = x0
            self.y = y0
            xc = 2 * (GLOBAL_XMAX / GLOBAL_MODES) * m
            self.xc = xc
            self.obj.move_to([self.x + self.xc, self.y, 0])
            self.msign = np.sign(np.mod(m, 2) - 0.5)

            self.t = 0.0
            omega = 2 * np.pi / GLOBAL_T
            ampl = GLOBAL_XMAX / GLOBAL_MODES
            t0 = -np.arcsin(self.x / (ampl * self.ch)) / omega

            def update(myobj):
                self.t += dt
                self.x = -self.msign * self.ch * ampl * np.sin((self.t - t0) * omega)
                self.y += 0.05 * np.random.uniform(-1, 1)
                myobj.move_to([self.x + self.xc, self.y, 0])
            self.obj.add_updater(update)

    class Efield():
        def __init__(self, y, dx_max, obj, dt):
            self.y = y
            self.dx_max = dx_max
            self.obj = obj
            self.t = 0.0
            omega = 2 * np.pi / GLOBAL_T

            def update(myobj):
                self.t += dt
                x1 = 0.5 * self.dx_max * np.sin(self.t * omega)
                x2 = -0.5 * self.dx_max * np.sin(self.t * omega)
                myobj.put_start_and_end_on(np.array([x1, y, 0]), np.array([x2, y, 0]))
            self.obj.add_updater(update)

    def construct(self):
        self.fps = self.camera.frame_rate
        self.duration = 2 * GLOBAL_T / (self.fps * self.dt)

        TIMER_ = TextMobject("TIMER").move_to([-1000, -1000, 0])
        self.add(TIMER_)

        N = 300
        # N = 50
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(0, 0.2)) for i in range(N)]
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(-0.2, 0)) for i in range(N)]
        N = 100
        # N = 20
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(0, 0.4)) for i in range(N)]
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), np.random.uniform(-0.4, 0)) for i in range(N)]
        N = 20
        # N = 5
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), +1) for i in range(N)]
        [self.makeParticle(np.random.uniform(-self.xmax, self.xmax), np.random.uniform(-self.ymax, self.ymax), -1) for i in range(N)]

        [self.makeEfield(yi, 1.2) for yi in np.linspace(-self.ymax+0.5, self.ymax-0.5, 10)]

        e_text = TexMobject(r"\bm{E}", color=self.efield_col, stroke_opacity=self.efield_opac).scale(0.8).move_to([0, 0.8, 0])
        self.add(e_text)

        self.play(Write(TIMER_), run_time=self.duration)

    def makeParticle(self, x, y, ch):
        col = (self.e_col if (ch > 0) else self.p_col)
        sign = ("+" if (ch > 0) else "-")
        op = np.abs(ch)
        circ = Circle(radius=self.radius,
                      color=col, stroke_width=self.linew,
                      fill_opacity=self.opac*op, stroke_opacity=op)
        sign = TexMobject(sign, color=col, fill_opacity=op).scale((self.radius / 0.3))
        obj = VGroup(circ, sign)
        m = np.random.randint(-2, 3)
        prtl = self.Particle(x, y, m, obj, self.dt, ch)
        self.add(prtl.obj)
        return prtl

    def makeEfield(self, y, dx_max):
        arr = Arrow([0,0,0], [0,0,0],
                    color=self.efield_col,
                    stroke_opacity=self.efield_opac,
                    tip_length=0.3)
        tip = arr.get_tips()
        tip.set_fill(opacity = self.efield_opac)
        efield = self.Efield(y, dx_max, arr, self.dt)
        self.add(efield.obj)
        return efield

class PlasmaInt(Scene):
    CONFIG = {
        "radius": 0.15,
        "e_col": RED_C, "p_col": BLUE_C, "efield_col": TEAL_B, "efield_opac": 0.6,
        "linew": 1, "opac": 0.2,
        "xmax": GLOBAL_XMAX+0.1, "ymax": GLOBAL_YMAX,
        "dt": 0.1, "period": GLOBAL_T
    }
    class Region():
        def __init__(self, x0, dsx, col1, col2, obj, dt, period):
            self.period = period
            self.dt = dt
            self.col1 = col1
            self.col2 = col2
            self.obj = obj
            self.x0 = x0
            self.dsx = dsx
            self.w = 0
            self.obj.move_to([self.x0, 0, 0])
            self.obj.stretch_to_fit_height(2.5*GLOBAL_YMAX)
            self.obj.set_color(self.col1)
            self.t = 0
            def update(myobj):
                self.t += self.dt
                self.phase = self.t * 2 * np.pi / self.period
                self.w = np.sin(self.phase)
                myobj.stretch_to_fit_width(self.dsx * np.abs(self.w))
                myobj.set_opacity(1.0 - np.abs(self.w))
                if (np.cos(self.phase) > 0):
                    myobj.set_color(self.col1)
                else:
                    myobj.set_color(self.col2)
            self.obj.add_updater(update)
    class Efield():
        def __init__(self, x, y, dx_max, sign, obj, dt, period):
            self.dt = dt
            self.period = period
            self.x = x
            self.y = y
            self.dx_max = dx_max
            self.obj = obj
            self.t = period
            omega = 2 * np.pi / self.period

            def update(myobj):
                self.t += self.dt
                x1 = 0.5 * self.dx_max * np.sin(self.t * omega + sign * np.pi/2.0)
                x2 = -0.5 * self.dx_max * np.sin(self.t * omega + sign * np.pi/2.0)
                myobj.put_start_and_end_on(np.array([self.x + x1, y, 0]), np.array([self.x + x2, y, 0]))
            self.obj.add_updater(update)
    class dxArrow():
        def __init__(self, y, left, right, obj):
            self.y = y
            self.obj = obj
            def update(myobj):
                x1 = left.get_right()[0]
                x2 = right.get_left()[0]
                if (np.abs(x1 - x2) < 0.01):
                    x1 = x2 + 0.01
                myobj.put_start_and_end_on(np.array([x1, self.y, 0]), np.array([x2, self.y, 0]))
            self.obj.add_updater(update)

    def construct(self):
        self.fps = self.camera.frame_rate
        self.duration = 2 * GLOBAL_T / (self.fps * self.dt)
        TIMER_ = TextMobject("TIMER").move_to([-1000, -1000, 0])
        self.add(TIMER_)
        
        r1, r2, r3 = self.makeRegion()
        self.makeEfield(self.xmax/3.0, -2, 1.2, -1)
        self.makeEfield(-self.xmax/3.0, -2, 1.2, +1)
        a1 = self.makeArrow(+2, r1.obj, r2.obj)
        t1 = TexMobject(r'\Delta x').next_to(a1, UP).scale(0.8)
        a2 = self.makeArrow(+2, r3.obj, r1.obj)
        t2 = TexMobject(r'\Delta x').next_to(a2, UP).scale(0.8)
        self.add(t1, t2)
        
        self.play(Write(TIMER_), run_time=self.duration)
        
    def makeRegion(self):
        rec_ = Rectangle(fill_opacity=1, stroke_width=0)
        region1 = self.Region(0, self.xmax*2.0/3.0, 
                self.e_col, self.p_col, rec_, self.dt, self.period)
        self.add(region1.obj)
        
        rec_ = Rectangle(fill_opacity=1, stroke_width=0)
        region2 = self.Region(self.xmax*2.0/3.0, self.xmax*2.0/3.0, 
                self.p_col, self.e_col, rec_, self.dt, self.period)
        self.add(region2.obj)
        
        rec_ = Rectangle(fill_opacity=1, stroke_width=0)
        region3 = self.Region(-self.xmax*2.0/3.0, self.xmax*2.0/3.0, 
                self.p_col, self.e_col, rec_, self.dt, self.period)
        self.add(region3.obj)

        return (region1, region2, region3)

    def makeEfield(self, x, y, dx_max, sign):
        arr = Arrow([0,0,0], [0,0,0],
                    color=self.efield_col,
                    stroke_opacity=self.efield_opac,
                    tip_length=0.3)
        tip = arr.get_tips()
        tip.set_fill(opacity = self.efield_opac)
        efield = self.Efield(x, y, dx_max, sign, arr, self.dt, self.period)
        text = TexMobject(r'\bm{E}', color=self.efield_col).next_to(efield.obj, DOWN)
        self.add(efield.obj, text)

    def makeArrow(self, y, lft, rgt):
        arr = DoubleArrow([1, 0, 0], [0, 0, 0], 
                color=WHITE, tip_length=0.1, stroke_width=2)
        doublearr = self.dxArrow(y, lft, rgt, arr)
        self.add(doublearr.obj)
        return doublearr.obj

