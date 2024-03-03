"""
File:
Name: Cara
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Go killing the suck piggies!

    Bad Piggies are bugs, Angry Birds are method attributes.
    Just like lives are full of bugs then view yourself as
    full-functional Angry Birds to kill piggies.
    """
    window = GWindow(width=800, height=500, title='AngryBird Classic')
    # sky
    sky = GRect(801, 500, x=-1, y=-1)
    sky.filled = True
    sky.fill_color = "lavender"
    sky.color = "lavender"
    window.add(sky)
    # cloud1
    cloud = GOval(900, 800, x=-100, y=250)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)
    cloud = GOval(700, 700, x=500, y=200)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)
    cloud = GOval(500, 500, x=-300, y=300)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)
    # cloud2
    cloud = GOval(900, 800, x=-80, y=270)
    cloud.filled = True
    cloud.fill_color = 'lightcyan'
    cloud.color = 'lightcyan'
    window.add(cloud)
    cloud = GOval(700, 700, x=520, y=210)
    cloud.filled = True
    cloud.fill_color = 'lightcyan'
    cloud.color = 'lightcyan'
    window.add(cloud)
    cloud = GOval(500, 500, x=-300, y=325)
    cloud.filled = True
    cloud.fill_color = 'lightcyan'
    cloud.color = 'lightcyan'
    window.add(cloud)
    # balloon
    rope = GLine(450, 70, 450, 88)
    rope.color = 'saddlebrown'
    window.add(rope)
    rope = GLine(451, 70, 451, 88)
    rope.color = 'saddlebrown'
    window.add(rope)
    rope = GLine(450, 88, 433, 98)
    rope.color = 'saddlebrown'
    window.add(rope)
    rope = GLine(451, 88, 434, 98)
    rope.color = 'saddlebrown'
    window.add(rope)
    rope = GLine(450, 88, 467, 98)
    rope.color = 'saddlebrown'
    window.add(rope)
    rope = GLine(451, 88, 468, 98)
    rope.color = 'saddlebrown'
    window.add(rope)
    tie = GPolygon()
    tie.add_vertex((450, 70))
    tie.add_vertex((445, 78))
    tie.add_vertex((455, 78))
    tie.filled = True
    tie.fill_color = 'red'
    tie.color = "black"
    window.add(tie)
    balloon = GOval(40, 43, x=430, y=30)
    balloon.filled = True
    balloon.fill_color = 'red'
    balloon.color = 'black'
    window.add(balloon)
    luster = GOval(7, 7, x=452, y=35)
    luster.filled = True
    luster.fill_color = 'salmon'
    luster.color = 'salmon'
    window.add(luster)
    luster = GOval(8, 8, x=456, y=45)
    luster.filled = True
    luster.fill_color = 'salmon'
    luster.color = 'salmon'
    window.add(luster)
    luster = GOval(8, 8, x=456, y=49)
    luster.filled = True
    luster.fill_color = 'salmon'
    luster.color = 'salmon'
    window.add(luster)
    luster = GOval(8, 8, x=456, y=51)
    luster.filled = True
    luster.fill_color = 'salmon'
    luster.color = 'salmon'
    window.add(luster)
    luster = GOval(8, 8, x=455, y=53)
    luster.filled = True
    luster.fill_color = 'salmon'
    luster.color = 'salmon'
    window.add(luster)
    luster = GOval(8, 8, x=454, y=55)
    luster.filled = True
    luster.fill_color = 'salmon'
    luster.color = 'salmon'
    window.add(luster)
    banner = GRect(34, 160, x=433, y=98)
    banner.filled = True
    banner.fill_color = 'whitesmoke'
    banner.color = "grey"
    window.add(banner)
    text = GLabel("S", x=445, y=128)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("S", x=446, y=128)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("t", x=447, y=145)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("t", x=448, y=145)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("a", x=446, y=161)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("a", x=447, y=161)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("n", x=446, y=178)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("n", x=447, y=178)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("C", x=445, y=199)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("C", x=446, y=199)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("o", x=446, y=214)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("o", x=447, y=214)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("d", x=446, y=233)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("d", x=447, y=233)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("e", x=447, y=249)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    text = GLabel("e", x=448, y=249)
    text.color = "navy"
    text.font = '-14'
    window.add(text)
    # ground
    floor = GRect(801, 70, x=-1, y=430)
    floor.filled = True
    floor.fill_color = 'midnightblue'
    floor.color = "midnightblue"
    window.add(floor)
    # lawn
    lawn = GRect(801, 6, x=-1, y=424)
    lawn.filled = True
    lawn.fill_color = 'limegreen'
    lawn.color = "limegreen"
    window.add(lawn)
    # platform
    platform = GRect(250, 45, x=200, y=379)
    platform.filled = True
    platform.fill_color = 'saddlebrown'
    platform.color = "saddlebrown"
    window.add(platform)
    # slopes of the main platform
    platform_left_slope = GPolygon()
    platform_left_slope.add_vertex((200, 379))
    platform_left_slope.add_vertex((200, 424))
    platform_left_slope.add_vertex((155, 424))
    platform_left_slope.filled = True
    platform_left_slope.fill_color = 'saddlebrown'
    platform_left_slope.color = "saddlebrown"
    window.add(platform_left_slope)
    platform_right_slope = GPolygon()
    platform_right_slope.add_vertex((450, 379))
    platform_right_slope.add_vertex((450, 424))
    platform_right_slope.add_vertex((495, 424))
    platform_right_slope.filled = True
    platform_right_slope.fill_color = 'saddlebrown'
    platform_right_slope.color = "saddlebrown"
    window.add(platform_right_slope)
    # second platform
    platform_slope = GPolygon()
    platform_slope.add_vertex((635, 424))
    platform_slope.add_vertex((835, 424))
    platform_slope.add_vertex((735, 324))
    platform_slope.filled = True
    platform_slope.fill_color = 'saddlebrown'
    platform_slope.color = "saddlebrown"
    window.add(platform_slope)
    # tnt1
    in1 = GRect(8, 30, x=339, y=338)
    in1.filled = True
    in1.fill_color = 'peru'
    in1.color = "sienna"
    window.add(in1)
    in2 = GRect(8, 30, x=347, y=338)
    in2.filled = True
    in2.fill_color = 'peru'
    in2.color = "sienna"
    window.add(in2)
    in3 = GRect(8, 30, x=355, y=338)
    in3.filled = True
    in3.fill_color = 'peru'
    in3.color = "sienna"
    window.add(in3)
    in4 = GRect(8, 30, x=362, y=338)
    in4.filled = True
    in4.fill_color = 'peru'
    in4.color = "sienna"
    window.add(in4)
    lid1 = GRect(50, 10, x=330, y=330)
    lid1.filled = True
    lid1.fill_color = 'sandybrown'
    lid1.color = "sienna"
    window.add(lid1)
    lid2 = GRect(50, 10, x=330, y=368)
    lid2.filled = True
    lid2.fill_color = 'sandybrown'
    lid2.color = "sienna"
    window.add(lid2)
    wall1 = GRect(10, 28, x=330, y=340)
    wall1.filled = True
    wall1.fill_color = 'sandybrown'
    wall1.color = "sienna"
    window.add(wall1)
    wall2 = GRect(10, 28, x=370, y=340)
    wall2.filled = True
    wall2.fill_color = 'sandybrown'
    wall2.color = "sienna"
    window.add(wall2)
    label = GRect(24, 15, x=343, y=346)
    label.filled = True
    label.fill_color = 'gainsboro'
    label.color = "gainsboro"
    window.add(label)
    text = GLabel("TNT", x=344, y=362)
    text.color = "red"
    window.add(text)
    # angry bird
    tail1 = GOval(3, 3, x=131, y=136)
    tail1.filled = True
    tail1.fill_color = 'black'
    tail1.color = 'black'
    window.add(tail1)
    tail2 = GOval(10, 4, x=127, y=140)
    tail2.filled = True
    tail2.fill_color = 'black'
    tail2.color = 'black'
    window.add(tail2)
    tail3 = GOval(3, 3, x=132, y=145)
    tail3.filled = True
    tail3.fill_color = 'black'
    tail3.color = 'black'
    window.add(tail3)
    bird_body = GOval(41, 40, x=135, y=120)
    bird_body.filled = True
    bird_body.fill_color = 'firebrick'
    bird_body.color = 'saddlebrown'
    window.add(bird_body)
    bird_bangs = GOval(7, 7, x=148, y=110)
    bird_bangs.filled = True
    bird_bangs.fill_color = 'firebrick'
    bird_bangs.color = 'firebrick'
    window.add(bird_bangs)
    bird_bangs = GOval(8, 8, x=151, y=112)
    bird_bangs.filled = True
    bird_bangs.fill_color = 'firebrick'
    bird_bangs.color = 'firebrick'
    window.add(bird_bangs)
    bird_bangs = GOval(8, 8, x=152, y=113)
    bird_bangs.filled = True
    bird_bangs.fill_color = 'firebrick'
    bird_bangs.color = 'firebrick'
    window.add(bird_bangs)
    bird_bangs = GOval(7, 7, x=137, y=115)
    bird_bangs.filled = True
    bird_bangs.fill_color = 'firebrick'
    bird_bangs.color = 'firebrick'
    window.add(bird_bangs)
    bird_bangs = GOval(8, 8, x=140, y=115)
    bird_bangs.filled = True
    bird_bangs.fill_color = 'firebrick'
    bird_bangs.color = 'firebrick'
    window.add(bird_bangs)
    bird_bangs = GOval(8, 8, x=143, y=116)
    bird_bangs.filled = True
    bird_bangs.fill_color = 'firebrick'
    bird_bangs.color = 'firebrick'
    window.add(bird_bangs)
    bird_bangs = GOval(7, 7, x=155, y=115)
    bird_bangs.filled = True
    bird_bangs.fill_color = 'firebrick'
    bird_bangs.color = 'firebrick'
    window.add(bird_bangs)
    bird_bangsline = GLine(147, 116, 153, 122)
    window.add(bird_bangsline)
    bird_belly = GOval(34, 15, x=138, y=144)
    bird_belly.filled = True
    bird_belly.fill_color = 'wheat'
    bird_belly.color = 'saddlebrown'
    window.add(bird_belly)
    bird_eye_r = GOval(11, 11, x=163, y=132)
    bird_eye_r.filled = True
    bird_eye_r.fill_color = 'snow'
    bird_eye_r.color = 'saddlebrown'
    window.add(bird_eye_r)
    bird_eye_rm = GOval(2, 2, x=167, y=137)
    bird_eye_rm.filled = True
    bird_eye_rm.fill_color = 'black'
    bird_eye_rm.color = 'black'
    window.add(bird_eye_rm)
    bird_eye_l = GOval(11, 11, x=155, y=132)
    bird_eye_l.filled = True
    bird_eye_l.fill_color = 'snow'
    bird_eye_l.color = 'saddlebrown'
    window.add(bird_eye_l)
    bird_eye_lm = GOval(2, 2, x=162, y=138)
    bird_eye_lm.filled = True
    bird_eye_lm.fill_color = 'black'
    bird_eye_lm.color = 'black'
    window.add(bird_eye_lm)
    eyebrow = GPolygon()
    eyebrow.add_vertex((152, 130))
    eyebrow.add_vertex((165, 134))
    eyebrow.add_vertex((173, 128))
    eyebrow.add_vertex((174, 131))
    eyebrow.add_vertex((165, 136))
    eyebrow.add_vertex((152, 134))
    eyebrow.filled = True
    eyebrow.fill_color = 'black'
    eyebrow.color = "black"
    window.add(eyebrow)
    upper_beak = GPolygon()
    upper_beak.add_vertex((167, 140))
    upper_beak.add_vertex((162, 147))
    upper_beak.add_vertex((180, 147))
    upper_beak.filled = True
    upper_beak.fill_color = 'gold'
    upper_beak.color = "darkred"
    window.add(upper_beak)
    lower_beak = GPolygon()
    lower_beak.add_vertex((163, 146))
    lower_beak.add_vertex((166, 151))
    lower_beak.add_vertex((177, 147))
    lower_beak.filled = True
    lower_beak.fill_color = 'gold'
    lower_beak.color = "darkred"
    window.add(lower_beak)
    route = GOval(9, 9, x=-2, y=110)
    route.filled = True
    route.fill_color = 'white'
    route.color = 'thistle'
    window.add(route)
    route = GOval(6, 6, x=17, y=113)
    route.filled = True
    route.fill_color = 'white'
    route.color = 'thistle'
    window.add(route)
    route = GOval(9, 9, x=36, y=115)
    route.filled = True
    route.fill_color = 'white'
    route.color = 'thistle'
    window.add(route)
    route = GOval(9, 9, x=57, y=119)
    route.filled = True
    route.fill_color = 'white'
    route.color = 'thistle'
    window.add(route)
    route = GOval(6, 6, x=78, y=126)
    route.filled = True
    route.fill_color = 'white'
    route.color = 'thistle'
    window.add(route)
    route = GOval(6, 6, x=98, y=130)
    route.filled = True
    route.fill_color = 'white'
    route.color = 'thistle'
    window.add(route)
    route = GOval(9, 9, x=116, y=135)
    route.filled = True
    route.fill_color = 'white'
    route.color = 'thistle'
    window.add(route)
    # pig2
    pig2_face = GOval(34, 30, x=335, y=300)
    pig2_face.filled = True
    pig2_face.fill_color = 'limegreen'
    pig2_face.color = 'black'
    window.add(pig2_face)
    pig2_ear_l = GOval(6, 6, x=347, y=295)
    pig2_ear_l.filled = True
    pig2_ear_l.fill_color = 'limegreen'
    pig2_ear_l.color = 'darkgreen'
    window.add(pig2_ear_l)
    pig2_ear_l_m = GOval(2, 3, x=349, y=298)
    pig2_ear_l_m.filled = True
    pig2_ear_l_m.fill_color = 'darkolivegreen'
    pig2_ear_l_m.color = 'darkolivegreen'
    window.add(pig2_ear_l_m)
    pig2_ear_r = GOval(6, 7, x=360, y=296)
    pig2_ear_r.filled = True
    pig2_ear_r.fill_color = 'limegreen'
    pig2_ear_r.color = 'darkgreen'
    window.add(pig2_ear_r)
    pig2_ear_r_m = GOval(2, 3, x=361, y=299)
    pig2_ear_r_m.filled = True
    pig2_ear_r_m.fill_color = 'darkolivegreen'
    pig2_ear_r_m.color = 'darkolivegreen'
    window.add(pig2_ear_r_m)
    pig2_eye_l = GOval(9, 10, x=335, y=308)
    pig2_eye_l.filled = True
    pig2_eye_l.fill_color = 'whitesmoke'
    pig2_eye_l.color = 'black'
    window.add(pig2_eye_l)
    pig2_eye_l_m = GOval(2, 2, x=338, y=310)
    pig2_eye_l_m.filled = True
    pig2_eye_l_m.fill_color = 'black'
    pig2_eye_l_m.color = 'black'
    window.add(pig2_eye_l_m)
    pig2_eye_r = GOval(9, 10, x=360, y=310)
    pig2_eye_r.filled = True
    pig2_eye_r.fill_color = 'whitesmoke'
    pig2_eye_r.color = 'black'
    window.add(pig2_eye_r)
    pig2_eye_r_m = GOval(2, 2, x=363, y=312)
    pig2_eye_r_m.filled = True
    pig2_eye_r_m.fill_color = 'black'
    pig2_eye_r_m.color = 'black'
    window.add(pig2_eye_r_m)
    pig2_nose = GOval(16, 13, x=343, y=312)
    pig2_nose.filled = True
    pig2_nose.fill_color = 'greenyellow'
    pig2_nose.color = 'darkolivegreen'
    window.add(pig2_nose)
    pig2_nostril1 = GOval(4, 6, x=346, y=315)
    pig2_nostril1.filled = True
    pig2_nostril1.fill_color = 'black'
    pig2_nostril1.color = 'darkolivegreen'
    window.add(pig2_nostril1)
    pig2_nostril2 = GOval(4, 6, x=352, y=316)
    pig2_nostril2.filled = True
    pig2_nostril2.fill_color = 'black'
    pig2_nostril2.color = 'darkolivegreen'
    window.add(pig2_nostril2)
    # pig3
    pig3_face = GOval(34, 30, x=400, y=348)  # x=335, y=300
    pig3_face.filled = True
    pig3_face.fill_color = 'limegreen'
    pig3_face.color = 'black'
    window.add(pig3_face)
    pig3_ear_l = GOval(6, 6, x=412, y=342)  # x=347, y=295
    pig3_ear_l.filled = True
    pig3_ear_l.fill_color = 'limegreen'
    pig3_ear_l.color = 'darkgreen'
    window.add(pig3_ear_l)
    pig3_ear_l_m = GOval(2, 3, x=414, y=345)  # x=349, y=298
    pig3_ear_l_m.filled = True
    pig3_ear_l_m.fill_color = 'darkolivegreen'
    pig3_ear_l_m.color = 'darkolivegreen'
    window.add(pig3_ear_l_m)
    pig3_ear_r = GOval(6, 7, x=425, y=344)  # x=360, y=296
    pig3_ear_r.filled = True
    pig3_ear_r.fill_color = 'limegreen'
    pig3_ear_r.color = 'darkgreen'
    window.add(pig3_ear_r)
    pig3_ear_r_m = GOval(2, 3, x=426, y=347)  # x=361, y=299
    pig3_ear_r_m.filled = True
    pig3_ear_r_m.fill_color = 'darkolivegreen'
    pig3_ear_r_m.color = 'darkolivegreen'
    window.add(pig3_ear_r_m)
    pig3_eye_l = GOval(9, 10, x=400, y=356)  # x=335, y=308
    pig3_eye_l.filled = True
    pig3_eye_l.fill_color = 'whitesmoke'
    pig3_eye_l.color = 'black'
    window.add(pig3_eye_l)
    pig3_eye_l_m = GOval(2, 2, x=403, y=358)  # x=338, y=310
    pig3_eye_l_m.filled = True
    pig3_eye_l_m.fill_color = 'black'
    pig3_eye_l_m.color = 'black'
    window.add(pig3_eye_l_m)
    pig3_eye_r = GOval(9, 10, x=425, y=358)  # x=360, y=310
    pig3_eye_r.filled = True
    pig3_eye_r.fill_color = 'whitesmoke'
    pig3_eye_r.color = 'black'
    window.add(pig3_eye_r)
    pig3_eye_r_m = GOval(2, 2, x=428, y=360)  # x=363, y=312
    pig3_eye_r_m.filled = True
    pig3_eye_r_m.fill_color = 'black'
    pig3_eye_r_m.color = 'black'
    window.add(pig3_eye_r_m)
    pig3_nose = GOval(16, 13, x=409, y=360)  # x=343, y=312
    pig3_nose.filled = True
    pig3_nose.fill_color = 'greenyellow'
    pig3_nose.color = 'darkolivegreen'
    window.add(pig3_nose)
    pig3_nostril1 = GOval(4, 6, x=412, y=363)  # x=346, y=315
    pig3_nostril1.filled = True
    pig3_nostril1.fill_color = 'black'
    pig3_nostril1.color = 'darkolivegreen'
    window.add(pig3_nostril1)
    pig3_nostril2 = GOval(4, 6, x=418, y=364)  # x=352, y=316
    pig3_nostril2.filled = True
    pig3_nostril2.fill_color = 'black'
    pig3_nostril2.color = 'darkolivegreen'
    window.add(pig3_nostril2)
    # pig1
    pig1_face = GOval(34, 30, x=246, y=113)
    pig1_face.filled = True
    pig1_face.fill_color = 'limegreen'
    pig1_face.color = 'black'
    window.add(pig1_face)
    pig1_ear_l = GOval(6, 6, x=246, y=112)
    pig1_ear_l.filled = True
    pig1_ear_l.fill_color = 'limegreen'
    pig1_ear_l.color = 'darkgreen'
    window.add(pig1_ear_l)
    pig1_ear_l_m = GOval(2, 3, x=248, y=115)
    pig1_ear_l_m.filled = True
    pig1_ear_l_m.fill_color = 'darkolivegreen'
    pig1_ear_l_m.color = 'darkolivegreen'
    window.add(pig1_ear_l_m)
    pig1_ear_r = GOval(6, 7, x=258, y=107)
    pig1_ear_r.filled = True
    pig1_ear_r.fill_color = 'limegreen'
    pig1_ear_r.color = 'darkgreen'
    window.add(pig1_ear_r)
    pig1_ear_r_m = GOval(2, 3, x=260, y=110)
    pig1_ear_r_m.filled = True
    pig1_ear_r_m.fill_color = 'darkolivegreen'
    pig1_ear_r_m.color = 'darkolivegreen'
    window.add(pig1_ear_r_m)
    pig1_eye_l = GOval(9, 10, x=247, y=127)
    pig1_eye_l.filled = True
    pig1_eye_l.fill_color = 'whitesmoke'
    pig1_eye_l.color = 'black'
    window.add(pig1_eye_l)
    pig1_eye_l_m = GOval(2, 2, x=250, y=132)
    pig1_eye_l_m.filled = True
    pig1_eye_l_m.fill_color = 'black'
    pig1_eye_l_m.color = 'black'
    window.add(pig1_eye_l_m)
    pig1_eye_r = GOval(9, 10, x=270, y=120)
    pig1_eye_r.filled = True
    pig1_eye_r.fill_color = 'whitesmoke'
    pig1_eye_r.color = 'black'
    window.add(pig1_eye_r)
    pig1_eye_r_m = GOval(2, 2, x=274, y=124)
    pig1_eye_r_m.filled = True
    pig1_eye_r_m.fill_color = 'black'
    pig1_eye_r_m.color = 'black'
    window.add(pig1_eye_r_m)
    pig1_nose = GOval(16, 13, x=256, y=125)
    pig1_nose.filled = True
    pig1_nose.fill_color = 'greenyellow'
    pig1_nose.color = 'darkolivegreen'
    window.add(pig1_nose)
    pig1_nostril1 = GOval(4, 6, x=259, y=129)
    pig1_nostril1.filled = True
    pig1_nostril1.fill_color = 'black'
    pig1_nostril1.color = 'darkolivegreen'
    window.add(pig1_nostril1)
    pig1_nostril2 = GOval(4, 6, x=265, y=129)
    pig1_nostril2.filled = True
    pig1_nostril2.fill_color = 'black'
    pig1_nostril2.color = 'darkolivegreen'
    window.add(pig1_nostril2)
    # pig4 (big)
    pig4_face = GOval(51, 45, x=545, y=245)
    pig4_face.filled = True   # (15, 15, x=603, y=273)
    pig4_face.fill_color = 'limegreen'
    pig4_face.color = 'black'
    window.add(pig4_face)
    pig4_ear_l = GOval(10, 10, x=560, y=236)
    pig4_ear_l.filled = True
    pig4_ear_l.fill_color = 'limegreen'
    pig4_ear_l.color = 'darkgreen'
    window.add(pig4_ear_l)
    pig4_ear_l_m = GOval(4, 6, x=563, y=240)
    pig4_ear_l_m.filled = True
    pig4_ear_l_m.fill_color = 'darkolivegreen'
    pig4_ear_l_m.color = 'darkolivegreen'
    window.add(pig4_ear_l_m)
    pig4_ear_r = GOval(10, 10, x=580, y=239)
    pig4_ear_r.filled = True
    pig4_ear_r.fill_color = 'limegreen'
    pig4_ear_r.color = 'darkgreen'
    window.add(pig4_ear_r)
    pig4_ear_r_m = GOval(4, 6, x=582, y=242)
    pig4_ear_r_m.filled = True
    pig4_ear_r_m.fill_color = 'darkolivegreen'
    pig4_ear_r_m.color = 'darkolivegreen'
    window.add(pig4_ear_r_m)
    pig4_eye_l = GOval(13, 15, x=545, y=260)
    pig4_eye_l.filled = True
    pig4_eye_l.fill_color = 'whitesmoke'
    pig4_eye_l.color = 'black'
    window.add(pig4_eye_l)
    pig4_eye_l_m = GOval(3, 3, x=550, y=270)
    pig4_eye_l_m.filled = True
    pig4_eye_l_m.fill_color = 'black'
    pig4_eye_l_m.color = 'black'
    window.add(pig4_eye_l_m)
    pig4_eye_r = GOval(13, 15, x=582, y=265)
    pig4_eye_r.filled = True
    pig4_eye_r.fill_color = 'whitesmoke'
    pig4_eye_r.color = 'black'
    window.add(pig4_eye_r)
    pig4_eye_r_m = GOval(3, 3, x=587, y=275)
    pig4_eye_r_m.filled = True
    pig4_eye_r_m.fill_color = 'black'
    pig4_eye_r_m.color = 'black'
    window.add(pig4_eye_r_m)
    pig4_nose = GOval(22, 19, x=560, y=265)
    pig4_nose.filled = True
    pig4_nose.fill_color = 'greenyellow'
    pig4_nose.color = 'darkolivegreen'
    window.add(pig4_nose)
    pig4_nostril1 = GOval(6, 8, x=564, y=271)
    pig4_nostril1.filled = True
    pig4_nostril1.fill_color = 'black'
    pig4_nostril1.color = 'darkolivegreen'
    window.add(pig4_nostril1)
    pig4_nostril2 = GOval(5, 7, x=572, y=272)
    pig4_nostril2.filled = True
    pig4_nostril2.fill_color = 'black'
    pig4_nostril2.color = 'darkolivegreen'
    window.add(pig4_nostril2)
    # pig5
    pig5_face = GOval(34, 30, x=550, y=334)
    pig5_face.filled = True
    pig5_face.fill_color = 'limegreen'
    pig5_face.color = 'black'
    window.add(pig5_face)
    pig5_ear_l = GOval(6, 6, x=550, y=334)
    pig5_ear_l.filled = True
    pig5_ear_l.fill_color = 'limegreen'
    pig5_ear_l.color = 'darkgreen'
    window.add(pig5_ear_l)
    pig5_ear_l_m = GOval(2, 3, x=552, y=336)
    pig5_ear_l_m.filled = True
    pig5_ear_l_m.fill_color = 'darkolivegreen'
    pig5_ear_l_m.color = 'darkolivegreen'
    window.add(pig5_ear_l_m)
    pig5_ear_r = GOval(6, 7, x=562, y=328)
    pig5_ear_r.filled = True
    pig5_ear_r.fill_color = 'limegreen'
    pig5_ear_r.color = 'darkgreen'
    window.add(pig5_ear_r)
    pig5_ear_r_m = GOval(2, 3, x=564, y=331)
    pig5_ear_r_m.filled = True
    pig5_ear_r_m.fill_color = 'darkolivegreen'
    pig5_ear_r_m.color = 'darkolivegreen'
    window.add(pig5_ear_r_m)
    pig5_eye_l = GOval(9, 10, x=551, y=348)
    pig5_eye_l.filled = True
    pig5_eye_l.fill_color = 'whitesmoke'
    pig5_eye_l.color = 'black'
    window.add(pig5_eye_l)
    pig5_eye_l_m = GOval(2, 2, x=554, y=350)
    pig5_eye_l_m.filled = True
    pig5_eye_l_m.fill_color = 'black'
    pig5_eye_l_m.color = 'black'
    window.add(pig5_eye_l_m)
    pig5_eye_r = GOval(9, 10, x=574, y=341)
    pig5_eye_r.filled = True
    pig5_eye_r.fill_color = 'whitesmoke'
    pig5_eye_r.color = 'black'
    window.add(pig5_eye_r)
    pig5_eye_r_m = GOval(2, 2, x=577, y=343)
    pig5_eye_r_m.filled = True
    pig5_eye_r_m.fill_color = 'black'
    pig5_eye_r_m.color = 'black'
    window.add(pig5_eye_r_m)
    pig5_nose = GOval(16, 13, x=560, y=346)
    pig5_nose.filled = True
    pig5_nose.fill_color = 'greenyellow'
    pig5_nose.color = 'darkolivegreen'
    window.add(pig5_nose)
    pig5_nostril1 = GOval(4, 6, x=563, y=350)
    pig5_nostril1.filled = True
    pig5_nostril1.fill_color = 'black'
    pig5_nostril1.color = 'darkolivegreen'
    window.add(pig5_nostril1)
    pig5_nostril2 = GOval(4, 6, x=569, y=350)
    pig5_nostril2.filled = True
    pig5_nostril2.fill_color = 'black'
    pig5_nostril2.color = 'darkolivegreen'
    window.add(pig5_nostril2)
    # wood (main place)
    wood1 = GRect(55, 28, x=201, y=348)
    wood1.filled = True
    wood1.fill_color = 'sandybrown'
    wood1.color = "sienna"
    window.add(wood1)
    wood2 = GRect(55, 28, x=258, y=348)
    wood2.filled = True
    wood2.fill_color = 'sandybrown'
    wood2.color = "sienna"
    window.add(wood2)
    wood3 = GRect(53, 28, x=231, y=319)
    wood3.filled = True
    wood3.fill_color = 'sandybrown'
    wood3.color = "sienna"
    window.add(wood3)
    wood4 = GRect(28, 28, x=201, y=260)
    wood4.filled = True
    wood4.fill_color = 'sandybrown'
    wood4.color = "sienna"
    window.add(wood4)
    wood5 = GRect(56, 28, x=230, y=260)
    wood5.filled = True
    wood5.fill_color = 'sandybrown'
    wood5.color = "sienna"
    window.add(wood5)
    wood6 = GRect(28, 29, x=288, y=260)
    wood6.filled = True
    wood6.fill_color = 'sandybrown'
    wood6.color = "sienna"
    window.add(wood6)
    wood7 = GRect(28, 28, x=201, y=231)
    wood7.filled = True
    wood7.fill_color = 'sandybrown'
    wood7.color = "sienna"
    window.add(wood7)
    wood8 = GRect(13, 56, x=234, y=203)
    wood8.filled = True
    wood8.fill_color = 'sandybrown'
    wood8.color = "sienna"
    window.add(wood8)
    wood9 = GRect(14, 56, x=269, y=203)
    wood9.filled = True
    wood9.fill_color = 'sandybrown'
    wood9.color = "sienna"
    window.add(wood9)
    wood10 = GRect(28, 28, x=288, y=231)
    wood10.filled = True
    wood10.fill_color = 'sandybrown'
    wood10.color = "sienna"
    window.add(wood10)
    wood11 = GRect(113, 14, x=202, y=187)
    wood11.filled = True
    wood11.fill_color = 'sandybrown'
    wood11.color = "sienna"
    window.add(wood11)
    wood12 = GRect(116, 14, x=200, y=143)
    wood12.filled = True
    wood12.fill_color = 'sandybrown'
    wood12.color = "sienna"
    window.add(wood12)
    # wood(second-place)
    wood13 = GRect(55, 28, x=510, y=394)
    wood13.filled = True
    wood13.fill_color = 'sandybrown'
    wood13.color = "sienna"
    window.add(wood13)
    wood14 = GRect(55, 28, x=568, y=394)
    wood14.filled = True
    wood14.fill_color = 'sandybrown'
    wood14.color = "sienna"
    window.add(wood14)
    wood15 = GRect(28, 28, x=512, y=306)
    wood15.filled = True
    wood15.fill_color = 'sandybrown'
    wood15.color = "sienna"
    window.add(wood15)
    wood16 = GRect(28, 28, x=593, y=306)
    wood16.filled = True
    wood16.fill_color = 'sandybrown'
    wood16.color = "sienna"
    window.add(wood16)
    wood17 = GRect(112, 15, x=510, y=290)
    wood17.filled = True
    wood17.fill_color = 'sandybrown'
    wood17.color = "sienna"
    window.add(wood17)
    # stone
    stone1 = GRect(28, 28, x=201, y=319)
    stone1.filled = True
    stone1.fill_color = 'grey'
    stone1.color = "dimgrey"
    window.add(stone1)
    stone2 = GRect(28, 28, x=285, y=319)
    stone2.filled = True
    stone2.fill_color = 'grey'
    stone2.color = "dimgrey"
    window.add(stone2)
    stone3 = GRect(28, 28, x=201, y=114)
    stone3.filled = True
    stone3.fill_color = 'grey'
    stone3.color = "dimgrey"
    window.add(stone3)
    stone4 = GRect(28, 28, x=286, y=114)
    stone4.filled = True
    stone4.fill_color = 'grey'
    stone4.color = "dimgrey"
    window.add(stone4)
    # stone(second place)
    stone5 = GRect(15, 15, x=510, y=273)
    stone5.filled = True
    stone5.fill_color = 'grey'
    stone5.color = "dimgrey"
    window.add(stone5)
    stone6 = GRect(15, 15, x=603, y=273)
    stone6.filled = True
    stone6.fill_color = 'grey'
    stone6.color = "dimgrey"
    window.add(stone6)
    # ice
    ice1 = GRect(28, 28, x=200, y=290)
    ice1.filled = True
    ice1.fill_color = 'lightskyblue'
    ice1.color = "steelblue"
    window.add(ice1)
    ice2 = GRect(27, 28, x=229, y=290)
    ice2.filled = True
    ice2.fill_color = 'lightskyblue'
    ice2.color = "steelblue"
    window.add(ice2)
    ice3 = GRect(28, 28, x=258, y=290)
    ice3.filled = True
    ice3.fill_color = 'lightskyblue'
    ice3.color = "steelblue"
    window.add(ice3)
    ice4 = GRect(27, 28, x=287, y=290)
    ice4.filled = True
    ice4.fill_color = 'lightskyblue'
    ice4.color = "steelblue"
    window.add(ice4)
    ice5 = GRect(27, 28, x=203, y=202)
    ice5.filled = True
    ice5.fill_color = 'lightskyblue'
    ice5.color = "steelblue"
    window.add(ice5)
    ice6 = GRect(15, 56, x=250, y=203)
    ice6.filled = True
    ice6.fill_color = 'lightskyblue'
    ice6.color = "steelblue"
    window.add(ice6)
    ice7 = GRect(28, 27, x=287, y=203)
    ice7.filled = True
    ice7.fill_color = 'lightskyblue'
    ice7.color = "steelblue"
    window.add(ice7)
    ice8 = GRect(28, 27, x=200, y=159)
    ice8.filled = True
    ice8.fill_color = 'lightskyblue'
    ice8.color = "steelblue"
    window.add(ice8)
    ice9 = GRect(28, 28, x=229, y=158)
    ice9.filled = True
    ice9.fill_color = 'lightskyblue'
    ice9.color = "steelblue"
    window.add(ice9)
    ice10 = GRect(27, 27, x=259, y=159)
    ice10.filled = True
    ice10.fill_color = 'lightskyblue'
    ice10.color = "steelblue"
    window.add(ice10)
    ice11 = GRect(28, 28, x=288, y=158)
    ice11.filled = True
    ice11.fill_color = 'lightskyblue'
    ice11.color = "steelblue"
    window.add(ice11)
    # ice(second-place)
    ice12 = GRect(28, 28, x=510, y=365)  # 下方木塊座標x=510, y=394  x=565, y=394
    ice12.filled = True
    ice12.fill_color = 'lightskyblue'
    ice12.color = "steelblue"
    window.add(ice12)
    ice13 = GRect(55, 28, x=539, y=365)
    ice13.filled = True
    ice13.fill_color = 'lightskyblue'
    ice13.color = "steelblue"
    window.add(ice13)
    ice14 = GRect(28, 28, x=595, y=365)
    ice14.filled = True
    ice14.fill_color = 'lightskyblue'
    ice14.color = "steelblue"
    window.add(ice14)
    ice15 = GRect(28, 28, x=509, y=336)
    ice15.filled = True
    ice15.fill_color = 'lightskyblue'
    ice15.color = "steelblue"
    window.add(ice15)
    ice16 = GRect(28, 28, x=595, y=335)
    ice16.filled = True
    ice16.fill_color = 'lightskyblue'
    ice16.color = "steelblue"
    window.add(ice16)
    # game UI
    button = GOval(50, 50, x=10, y=10)
    button.filled = True
    button.fill_color = 'oldlace'
    button.color = 'tan'
    window.add(button)
    button = GOval(40, 40, x=15, y=15)
    button.filled = True
    button.fill_color = 'khaki'
    button.color = 'tan'
    window.add(button)
    pause = GRect(9, 20, x=24, y=26)
    pause.filled = True
    pause.fill_color = 'whitesmoke'
    pause.color = "goldenrod"
    window.add(pause)
    pause = GRect(9, 20, x=37, y=26)
    pause.filled = True
    pause.fill_color = 'whitesmoke'
    pause.color = "goldenrod"
    window.add(pause)
    score = GLabel("HIGHSCORE: 587087", x=550, y=30)
    score.color = "black"
    score.font = '-20'
    window.add(score)
    score = GLabel("SCORE:          0", x=613, y=60)
    score.color = "black"
    score.font = '-20'
    window.add(score)
    # signature
    name = GLabel("I m a g e  C r e a t o r  &  C r e d i t :  C a r a", x=20, y=480)
    name.color = "lightsteelblue"
    name.font = '-10'
    window.add(name)


if __name__ == '__main__':
    main()
