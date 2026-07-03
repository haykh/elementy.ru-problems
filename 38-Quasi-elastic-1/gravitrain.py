#!/usr/bin/env python

from manimlib.imports import *
import numpy as np

PRODUCTION_QUALITY_FRAME_DURATION = 15

class Train(Scene):
    CONFIG = {
        "fps" : PRODUCTION_QUALITY_FRAME_DURATION
    }
    def construct(self):
        self.earth_rad = 3
        self.earth_cent = np.array([2, 0, 0])
        self.add_static_objects()
        self.add_dynamic_objects()

    def add_static_objects(self):
        theta1 = 70 * np.pi / 180.0
        theta2 = 190 * np.pi / 180.0
        theta1_ = 80 * np.pi / 180.0
        theta2_ = theta2 - (theta1_ - theta1)
        theta1__ = theta1 + (theta1_ - theta1) * 0.48
        theta2__ = theta2 + (theta2_ - theta2) * 0.48
        earth = Circle(radius=self.earth_rad, color=GOLD_E).move_to(self.earth_cent)
        tunnel = [Line(self.earth_cent + self.earth_rad * np.array([np.cos(theta1), np.sin(theta1), 0]),
                       self.earth_cent + self.earth_rad * np.array([np.cos(theta2), np.sin(theta2), 0]),
                       color=GOLD_A, stroke_opacity=0.5),
                  Line(self.earth_cent + self.earth_rad * np.array([np.cos(theta1_), np.sin(theta1_), 0]),
                       self.earth_cent + self.earth_rad * np.array([np.cos(theta2_), np.sin(theta2_), 0]),
                       color=GOLD_A, stroke_opacity=0.5)]
        self.p_start = self.earth_cent + self.earth_rad * np.array([np.cos(theta1__), np.sin(theta1__), 0])
        self.p_end = self.earth_cent + self.earth_rad * np.array([np.cos(theta2__), np.sin(theta2__), 0])
        self.add(earth)
        self.add(tunnel[0], tunnel[1])

    def add_dynamic_objects(self):
        self.time = 0
        def train_pos(time):
            return self.p_start + 0.5 * (1 - np.cos(2 * time)) * (self.p_end - self.p_start)
        def target_rad(time):
            return np.linalg.norm(train_pos(time) - self.earth_cent)
        def rv_pos(time):
            rad_theta = -10 * np.pi / 180.0
            return self.earth_cent + target_rad(time) * np.array([np.cos(rad_theta), np.sin(rad_theta), 0])
        def ff_len(time):
            return (target_rad(time) / self.earth_rad) * 0.6

        train = Circle(radius=0.18, color=None, fill_color=RED, fill_opacity=1)
        train.add_updater(lambda t: t.move_to(train_pos(self.time)))

        influence = Circle(radius=self.earth_rad, color=BLUE, fill_color=BLUE, fill_opacity=0.1).move_to(self.earth_cent)
        influence.add_updater(lambda inf: inf.set_width(2 * target_rad(self.time)))

        radius_vect = Arrow(self.earth_cent, self.earth_cent, stroke_width=2, tip_length=0.2, color=BLUE)
        radius_vect.add_updater(lambda rv: rv.put_start_and_end_on(self.earth_cent, rv_pos(self.time)))

        radius_text = TexMobject(r"r", height=0.2, color=BLUE)
        radius_text.add_updater(lambda rvt: rvt.next_to(radius_vect, 0.5 * DOWN))

        force = Arrow(self.earth_cent, self.earth_cent)
        force.add_updater(lambda ff: ff.put_start_and_end_on(train_pos(self.time),
                                                             train_pos(self.time) +
                                                                (self.earth_cent - train_pos(self.time)) * ff_len(self.time)))
        force_text = TexMobject(r"F")
        force_text.add_updater(lambda ft: ft.next_to(force, 0.5 * DOWN))

        TIMER_ = TextMobject("TIMER").move_to([-1000, -1000, 0])
        self.add(TIMER_)
        self.add(influence, radius_vect, radius_text)
        self.add(force, force_text)
        self.add(train)

        force_tex = TexMobject(
            "F = \\frac{G\\left(\\frac{4\\pi}{3} r^3\\rho\\right) m}{r^2}",
        ).shift([-4, 0, 0])
        descr1 = TextMobject("Гравитационная сила").shift([-4, 2, 0])
        descr2 = TextMobject("внутренней части")\
                    .next_to(descr1, DOWN)\
                    .align_to(descr1, LEFT)\
                    .set_color(BLUE)
        # self.play(Write(descr1), Write(descr2), Write(force_tex), run_time=1)
        self.add(descr1, descr2, force_tex)
        self.play(Write(TIMER_), run_time=2*np.pi)

class TrainsLEO(Scene):
    CONFIG = {
        "fps" : PRODUCTION_QUALITY_FRAME_DURATION
    }
    def construct(self):
        self.earth_rad = 3
        self.earth_cent = np.array([0, 0, 0])
        self.p_start = []
        self.p_end = []
        self.add_static_objects(90, 150, 10)
        self.add_static_objects(90, 190, 7)
        self.add_static_objects(90, 230, 6)
        self.add_static_objects(90, 270, 5)
        self.add_dynamic_objects()

    def add_static_objects(self, theta1, theta2, dth):
        theta1 = theta1 * np.pi / 180.0
        theta2 = theta2 * np.pi / 180.0
        theta1_ = theta1 + dth * np.pi / 180.0
        theta2_ = theta2 - (theta1_ - theta1)
        theta1__ = theta1 + (theta1_ - theta1) * 0.48
        theta2__ = theta2 + (theta2_ - theta2) * 0.48
        earth = Circle(radius=self.earth_rad, color=GOLD_E).move_to(self.earth_cent)
        tunnel = [Line(self.earth_cent + self.earth_rad * np.array([np.cos(theta1), np.sin(theta1), 0]),
                       self.earth_cent + self.earth_rad * np.array([np.cos(theta2), np.sin(theta2), 0]),
                       color=GOLD_A, stroke_opacity=0.5),
                  Line(self.earth_cent + self.earth_rad * np.array([np.cos(theta1_), np.sin(theta1_), 0]),
                       self.earth_cent + self.earth_rad * np.array([np.cos(theta2_), np.sin(theta2_), 0]),
                       color=GOLD_A, stroke_opacity=0.5)]
        self.p_start.append(self.earth_cent + self.earth_rad * np.array([np.cos(theta1__), np.sin(theta1__), 0]))
        self.p_end.append(self.earth_cent + self.earth_rad * np.array([np.cos(theta2__), np.sin(theta2__), 0]))
        self.add(earth)
        self.add(tunnel[0], tunnel[1])

    def add_dynamic_objects(self):
        self.time = 0
        def train_pos(ii, time):
            return self.p_start[ii] + 0.5 * (1 - np.cos(2 * time)) * (self.p_end[ii] - self.p_start[ii])
        def leosat_pos(time):
            return self.earth_cent + 1.1 * self.earth_rad * np.array([np.cos(2 * time + np.pi/2), np.sin(2 * time + np.pi/2), 0])

        TIMER_ = TextMobject("TIMER").move_to([-1000, -1000, 0])
        self.add(TIMER_)

        leosat = Circle(radius=0.18, color=None, fill_color=BLUE, fill_opacity=1)
        leosat.add_updater(lambda leo: leo.move_to(leosat_pos(self.time)))

        train0 = Circle(radius=0.18, color=None, fill_color=RED, fill_opacity=1)
        train0.add_updater(lambda t: t.move_to(train_pos(0, self.time)))
        train1 = Circle(radius=0.18, color=None, fill_color=RED, fill_opacity=1)
        train1.add_updater(lambda t: t.move_to(train_pos(1, self.time)))
        train2 = Circle(radius=0.18, color=None, fill_color=RED, fill_opacity=1)
        train2.add_updater(lambda t: t.move_to(train_pos(2, self.time)))
        train3 = Circle(radius=0.18, color=None, fill_color=RED, fill_opacity=1)
        train3.add_updater(lambda t: t.move_to(train_pos(3, self.time)))

        self.add(train0, train1, train2, train3, leosat)

        self.play(Write(TIMER_), run_time=2*np.pi)

class TrainProjection(Scene):
    def construct(self):
        self.earth_rad = 3.7
        self.earth_cent = np.array([0, 0, 0])
        self.add_static_objects()

    def add_static_objects(self):
        theta1 = 70 * np.pi / 180.0
        theta2 = 190 * np.pi / 180.0
        theta1_ = 80 * np.pi / 180.0
        theta2_ = theta2 - (theta1_ - theta1)
        theta1__ = theta1 + (theta1_ - theta1) * 0.48
        theta2__ = theta2 + (theta2_ - theta2) * 0.48
        earth = Circle(radius=self.earth_rad, color=GOLD_E).move_to(self.earth_cent)
        tunnel = [Line(self.earth_cent + self.earth_rad * np.array([np.cos(theta1), np.sin(theta1), 0]),
                       self.earth_cent + self.earth_rad * np.array([np.cos(theta2), np.sin(theta2), 0]),
                       color=GOLD_A, stroke_opacity=0.5),
                  Line(self.earth_cent + self.earth_rad * np.array([np.cos(theta1_), np.sin(theta1_), 0]),
                       self.earth_cent + self.earth_rad * np.array([np.cos(theta2_), np.sin(theta2_), 0]),
                       color=GOLD_A, stroke_opacity=0.5)]
        self.p_start = self.earth_cent + self.earth_rad * np.array([np.cos(theta1__), np.sin(theta1__), 0])
        self.p_end = self.earth_cent + self.earth_rad * np.array([np.cos(theta2__), np.sin(theta2__), 0])
        tt = 1.2

        def train_pos(time):
            return self.p_start + 0.5 * (1 - np.cos(2 * time)) * (self.p_end - self.p_start)
        def target_rad(time):
            return np.linalg.norm(train_pos(time) - self.earth_cent)
        def rv_pos(time):
            rad_theta = -30 * np.pi / 180.0
            return self.earth_cent + target_rad(time) * np.array([np.cos(rad_theta), np.sin(rad_theta), 0])
        def ff_len(time):
            return (target_rad(time) / self.earth_rad) * 0.8

        train = Circle(radius=0.3, color=None, fill_color=RED, fill_opacity=1).move_to(train_pos(tt))
        force = Arrow(train_pos(tt), train_pos(tt) + (self.earth_cent - train_pos(tt)) * ff_len(tt))
        force_text = TexMobject(r"F").next_to(force, 0.5 * DOWN)

        influence = Circle(radius=target_rad(tt), color=BLUE, fill_color=BLUE, fill_opacity=0.1).move_to(self.earth_cent)
        influence = DashedVMobject(influence, num_dashes=50)
        radius_vect = Arrow(self.earth_cent, rv_pos(tt), stroke_width=2, tip_length=0.2, color=BLUE)
        radius_text = TexMobject(r"r", height=0.2, color=BLUE).next_to(radius_vect, 0.5 * DOWN)

        dx = Arrow(train_pos(np.pi/4), train_pos(tt), color=RED_A, tip_length=0.2)
        dx = DashedVMobject(dx, num_dashes=20, positive_space_ratio=0.3)
        dx_text = TexMobject(r"x", heigh=0.2, color=RED_A).move_to(dx.get_center() + 0.4 * (UP + LEFT))

        dh = Line(self.earth_cent, train_pos(np.pi/4), color=RED_A)
        dh = DashedVMobject(dh, num_dashes=20, positive_space_ratio=0.3)
        dh_text = TexMobject(r"h", height=0.3, color=RED_A).move_to(dh.get_center() + 0.2 * (UP + RIGHT))

        self.add(earth)
        self.add(tunnel[0], tunnel[1])
        self.add(influence, radius_vect, radius_text)
        self.add(dx, dx_text)
        self.add(dh, dh_text)
        self.add(force, force_text)
        self.add(train)

class GaussTh(Scene):
    CONFIG = {
        "radius" : 3
    }
    def construct(self):
        self.p0 = self.radius * np.array([-0.3, 0.5, 0])
        self.c0 = np.array([2.0, 0, 0])
        circle = Circle(radius=self.radius, colo=RED).move_to(self.c0)
        point = Dot().move_to(self.c0 + self.p0)

        def get_d1d2(A, P, C):
            ac = np.dot(C, C)
            pa = np.dot(P, A)
            pc = np.dot(P, C)
            a = np.linalg.norm(A)
            c = np.linalg.norm(C)
            p = np.linalg.norm(P)
            d1 = (2*ac - 2*pa - np.sqrt((-2*ac + 2*pa)**2 - 4*a**2*(c**2 + p**2 - 2*pc - self.radius**2)))/(2.*a**2)
            d2 = (2*ac - 2*pa + np.sqrt((-2*ac + 2*pa)**2 - 4*a**2*(c**2 + p**2 - 2*pc - self.radius**2)))/(2.*a**2)
            return d1, d2

        self.a = np.array([-0.8, 1, 0])
        d1, d2 = get_d1d2(self.a, self.p0, np.array([0,0,0]))
        v1 = self.c0 + self.p0 + self.a * d1
        v2 = self.c0 + self.p0 + self.a * d2
        line1 = Line(v1, v2, color=BLUE)
        theta1 = np.arccos(np.dot(v1 - self.c0, UP) / np.linalg.norm(v1 - self.c0))
        theta2 = np.arccos(np.dot(v2 - self.c0, UP) / np.linalg.norm(v2 - self.c0))

        self.a = np.array([-1.2, 1, 0])
        d1, d2 = get_d1d2(self.a, self.p0, np.array([0,0,0]))
        v1 = self.c0 + self.p0 + self.a * d1
        v2 = self.c0 + self.p0 + self.a * d2
        line2 = Line(v1, v2, color=BLUE)
        dth1 = np.arccos(np.dot(v1 - self.c0, UP) / np.linalg.norm(v1 - self.c0)) - theta1
        dth2 = np.arccos(np.dot(v2 - self.c0, UP) / np.linalg.norm(v2 - self.c0)) - theta2

        self.a = np.array([-1, 1, 0])
        d1, d2 = get_d1d2(self.a, self.p0, np.array([0,0,0]))
        v1 = self.c0 + self.p0 + self.a * d1
        v2 = self.c0 + self.p0 + self.a * d2
        line01 = Line(self.c0 + self.p0, v1, color=BLUE)
        line01 = DashedVMobject(line01, num_dashes=30)
        line02 = Line(self.c0 + self.p0, v2, color=BLUE)
        line02 = DashedVMobject(line02, num_dashes=10)

        arc1 = Arc(radius=self.radius, arc_center=self.c0, start_angle=PI/2-theta1, angle=-dth1)
        arc2 = Arc(radius=self.radius, arc_center=self.c0, start_angle=PI/2 + theta2, angle=dth2)
        r1 = TexMobject(r'r_1', color=BLUE).move_to(line02.get_center() + 0.5 * (UP + RIGHT))
        r2 = TexMobject(r'r_2', color=BLUE).move_to(line01.get_center() + 0.5 * (RIGHT) + 0.2 * UP)

        m1 = TexMobject(r'm_1', color=WHITE).move_to(arc2.get_center() + 0.3 * (UP + LEFT))
        m2 = TexMobject(r'm_2', color=WHITE).move_to(arc1.get_center() + 0.3 * (RIGHT + DOWN))

        f1 = Arrow(self.c0 + self.p0,
                   self.c0 + self.p0 + 1.5 * (v1 - self.c0 - self.p0) / np.linalg.norm(v1 - self.c0 - self.p0))
        f2 = Arrow(self.c0 + self.p0,
                   self.c0 + self.p0 + 1.5 * (v2 - self.c0 - self.p0) / np.linalg.norm(v2 - self.c0 - self.p0))
        f1_t = TexMobject(r'F_2', color=WHITE).move_to(f1.get_center() + 0.4 * (DOWN + LEFT))
        f2_t = TexMobject(r'F_1', color=WHITE).move_to(f2.get_center() + 0.4 * (DOWN + LEFT))

        form1 = TexMobject(r"F_1 \propto \frac{m_1}{r_1^2}").move_to([-5.5, 2, 0])
        form10 = TexMobject(r"m_1\propto A_1\propto r_1^2")\
                    .next_to(form1, DOWN)\
                    .align_to(form1, LEFT)
        form2 = TexMobject(r"F_2 \propto \frac{m_2}{r_2^2}").move_to([-5.5, -1.5, 0])
        form20 = TexMobject(r"m_2\propto A_2\propto r_2^2")\
                    .next_to(form2, DOWN)\
                    .align_to(form2, LEFT)

        self.add(circle, line1, line2, line01, line02, point)
        self.add(f1, f2, f1_t, f2_t)
        self.add(r1, r2, m1, m2)
        self.add(form1, form10, form2, form20)
        self.add(arc1, arc2)
