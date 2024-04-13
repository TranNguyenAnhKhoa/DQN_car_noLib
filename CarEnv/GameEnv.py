
import pygame
import math

GOALREWARD = 1
LIFE_REWARD = 0
PENALTY = -1

class Wall(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, win):
        pygame.draw.line(win, (255, 255, 255), (self.x1, self.y1), (self.x2, self.y2), 5)

def getWalls():
    walls = []

    wall1 = Wall(32, 160, 32, 460)
    wall2 = Wall(32, 460, 40, 512)
    wall3 = Wall(40, 512, 61, 547)
    wall4 = Wall(61, 547, 98, 578)
    wall5 = Wall(98, 578, 151, 598)
    wall6 = Wall(151, 598, 172, 600)
    wall7 = Wall(172, 600, 227, 599)  #
    wall8 = Wall(227, 599, 229, 557)
    wall9 = Wall(229, 557, 340, 557)
    wall10 = Wall(340, 557, 340, 599)
    wall11 = Wall(340, 599, 671, 599)
    wall12 = Wall(671, 599, 670, 568)  #
    wall13 = Wall(670, 568, 697, 565)
    wall14 = Wall(697, 565, 709, 557)
    wall15 = Wall(709, 557, 725, 556)
    wall16 = Wall(725, 556, 746, 567)
    wall17 = Wall(746, 567, 757, 571)
    wall18 = Wall(757, 571, 758, 598)
    wall19 = Wall(758, 598, 776, 594)
    wall20 = Wall(776, 594, 814, 590)
    wall21 = Wall(814, 590, 878, 559)
    wall22 = Wall(878, 559, 913, 524)
    wall23 = Wall(913, 524, 933, 483)
    wall24 = Wall(933, 483, 931, 434)
    wall25 = Wall(931, 434, 906, 385)
    wall27 = Wall(906, 385, 865, 351)
    wall28 = Wall(865, 351, 808, 328)
    wall29 = Wall(808, 328, 721, 325)
    wall30 = Wall(721, 325, 723, 363)
    wall31 = Wall(723, 363, 638, 362)
    wall32 = Wall(638, 362, 637, 339)
    wall33 = Wall(637, 339, 636, 323)
    wall34 = Wall(636, 323, 365, 324)  #
    wall35 = Wall(365, 324, 339, 311)
    wall36 = Wall(339, 311, 333, 288)
    wall37 = Wall(333, 288, 347, 266)
    wall38 = Wall(347, 266, 365, 257)
    wall39 = Wall(365, 257, 432, 257)
    wall40 = Wall(432, 257, 433, 227)
    wall41 = Wall(433, 227, 464, 225)
    wall42 = Wall(464, 225, 486, 211)  #
    wall43 = Wall(486, 211, 510, 222)  #
    wall44 = Wall(510, 222, 530, 234)
    wall45 = Wall(530, 234, 531, 257)
    wall46 = Wall(531, 257, 750, 255)
    wall47 = Wall(750, 255, 814, 239)
    wall48 = Wall(814, 239, 854, 209)
    wall49 = Wall(814, 239, 854, 209)
    wall50 = Wall(854, 209, 885, 160)
    wall51 = Wall(885, 160, 889, 111)
    wall52 = Wall(889, 111, 860, 57)
    wall53 = Wall(860, 57, 800, 27)
    wall54 = Wall(800, 27, 698, 24)
    wall55 = Wall(698, 24, 699, 67)
    wall56 = Wall(699, 67, 584, 66)
    wall57 = Wall(584, 66, 583, 21)
    wall58 = Wall(583, 21, 175, 20)
    wall59 = Wall(175, 20, 114, 36)  #
    wall60 = Wall(114, 36, 70, 63)
    wall61 = Wall(70, 63, 40, 109)
    wall62 = Wall(40, 109, 32, 160)
    wall63 = Wall(135, 154, 140, 475)
    wall64 = Wall(140, 475, 180, 494)
    wall65 = Wall(180, 494, 331, 496)
    wall66 = Wall(331, 496, 455, 496)
    wall67 = Wall(455, 496, 456, 537)
    wall68 = Wall(456, 537, 573, 539)
    wall69 = Wall(573, 539, 575, 496)
    wall70 = Wall(575, 496, 766, 494)
    wall71 = Wall(766, 494, 797, 470)
    wall72 = Wall(797, 470, 791, 442)
    wall73 = Wall(791, 442, 768, 428)
    wall74 = Wall(768, 428, 523, 427)
    wall75 = Wall(523, 427, 520, 399)
    wall76 = Wall(520, 399, 483, 382)
    wall77 = Wall(483, 382, 432, 395)
    wall78 = Wall(432, 395, 427, 423)
    wall79 = Wall(427, 423, 364, 427)
    wall80 = Wall(364, 427, 311, 418)
    wall81 = Wall(311, 418, 231, 339)
    wall82 = Wall(231, 339, 229, 249)
    wall83 = Wall(229, 249, 268, 192)
    wall84 = Wall(268, 192, 349, 148)
    wall85 = Wall(349, 148, 490, 155)  #
    wall86 = Wall(490, 155, 612, 152)
    wall87 = Wall(612, 152, 610, 194)
    wall88 = Wall(610, 194, 696, 198)
    wall89 = Wall(696, 198, 700, 151)
    wall90 = Wall(700, 151, 765, 151)
    wall91 = Wall(765, 151, 785, 126)
    wall92 = Wall(785, 126, 371, 127)
    wall93 = Wall(371, 127, 367, 83)
    wall94 = Wall(367, 83, 253, 85)
    wall95 = Wall(253, 85, 251, 126)  #
    wall96 = Wall(251, 126, 155, 128)
    wall97 = Wall(155, 128, 135, 154)
    wall98 = Wall(135, 154, 135, 154)

    walls.append(wall1)
    walls.append(wall2)
    walls.append(wall3)
    walls.append(wall4)
    walls.append(wall5)
    walls.append(wall6)
    walls.append(wall7)
    walls.append(wall8)
    walls.append(wall9)
    walls.append(wall10)
    walls.append(wall11)
    walls.append(wall12)
    walls.append(wall13)
    walls.append(wall14)
    walls.append(wall15)
    walls.append(wall16)
    walls.append(wall17)
    walls.append(wall18)
    walls.append(wall19)
    walls.append(wall20)
    walls.append(wall21)
    walls.append(wall22)
    walls.append(wall23)
    walls.append(wall24)
    walls.append(wall25)

    walls.append(wall27)
    walls.append(wall28)
    walls.append(wall29)
    walls.append(wall30)
    walls.append(wall31)
    walls.append(wall32)
    walls.append(wall33)
    walls.append(wall34)
    walls.append(wall35)
    walls.append(wall36)
    walls.append(wall37)
    walls.append(wall38)
    walls.append(wall39)
    walls.append(wall40)
    walls.append(wall41)
    walls.append(wall42)
    walls.append(wall43)
    walls.append(wall44)
    walls.append(wall45)
    walls.append(wall46)
    walls.append(wall47)
    walls.append(wall48)
    walls.append(wall49)
    walls.append(wall50)
    walls.append(wall51)
    walls.append(wall52)
    walls.append(wall53)
    walls.append(wall54)
    walls.append(wall55)
    walls.append(wall56)
    walls.append(wall57)
    walls.append(wall58)
    walls.append(wall59)
    walls.append(wall60)
    walls.append(wall61)
    walls.append(wall62)
    walls.append(wall63)
    walls.append(wall64)
    walls.append(wall65)
    walls.append(wall66)
    walls.append(wall67)
    walls.append(wall68)
    walls.append(wall69)
    walls.append(wall70)
    walls.append(wall71)
    walls.append(wall72)
    walls.append(wall73)
    walls.append(wall74)
    walls.append(wall75)
    walls.append(wall76)
    walls.append(wall77)
    walls.append(wall78)
    walls.append(wall79)
    walls.append(wall80)
    walls.append(wall81)
    walls.append(wall82)
    walls.append(wall83)
    walls.append(wall84)
    walls.append(wall85)
    walls.append(wall86)
    walls.append(wall87)
    walls.append(wall88)
    walls.append(wall89)
    walls.append(wall90)
    walls.append(wall91)
    walls.append(wall92)
    walls.append(wall93)
    walls.append(wall94)
    walls.append(wall95)
    walls.append(wall96)
    walls.append(wall97)
    walls.append(wall98)

    return (walls)

class Goal:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.isactiv = False

    def draw(self, win):
        pygame.draw.line(win, (0, 255, 0), (self.x1, self.y1), (self.x2, self.y2), 2)
        if self.isactiv:
            pygame.draw.line(win, (255, 0, 0), (self.x1, self.y1), (self.x2, self.y2), 2)

# the file of shame
def getGoals():
    goals = []

    goal1 = Goal(0, 200, 167, 203)
    goal2 = Goal(0, 100, 161, 186)
    goal2_5 = Goal(0, 0, 150, 130)
    goal3 = Goal(120, 0, 170, 120)
    goal3_5 = Goal(200, 0, 200, 120)
    goal4 = Goal(270, 0, 270, 110)
    goal4_5 = Goal(363 ,9,367, 91)
    goal5 = Goal(450, 0, 450, 137)
    goal5_5 = Goal(525, 0, 525, 142)  #
    goal6 = Goal(583, 7, 582, 141)
    goal6_5 = Goal(642, 10, 638, 142)
    goal7_5 = Goal(685, 57, 740, 131)########
    goal8 = Goal(754, 141, 794, 16)
    goal9 = Goal(754, 141, 881, 55)
    goal9_5 = Goal(755, 142, 909, 137)
    goal10 = Goal(754, 144, 887, 232)
    goal10_5 = Goal(755, 146, 771, 275)
    goal11 = Goal(716, 139, 720, 278)
    goal12 = Goal(674, 137, 685, 275)
    goal13 = Goal(636, 136, 634, 284)
    goal13_1 = Goal(615, 182, 581, 265)
    goal15 = Goal(554, 139, 558, 277)
    goal16 = Goal(526, 138, 513, 271)
    goal17 = Goal(482, 138, 474, 268)
    goal17_1 = Goal(430, 137, 415, 281)
    goal17_2 = Goal(369, 139, 380, 271)
    goal17_3 = Goal(341, 139, 362, 285)
    goal17_4 = Goal(269, 151, 362, 284)
    goal17_5 = Goal(163, 210, 361, 282)
    goal17_6 = Goal(144, 302, 362, 286)
    goal17_7 = Goal(201, 370, 357, 289)
    goal17_8 = Goal(303, 449, 390, 314)
    goal17_9 = Goal(381, 458, 431, 310)
    goal17_10 = Goal(427, 461, 482, 308)
    goal17_11 = Goal(477, 457, 535, 314)
    goal17_12 = Goal(534, 452, 592, 314)
    goal17_13 = Goal(589, 447, 643, 312)
    goal17_14 = Goal(641, 458, 686, 309)
    goal17_14_1 = Goal(718 ,345, 730 ,432)
    goal17_16 = Goal(728, 453, 843, 319)
    goal17_17 = Goal(761, 458, 916, 367)
    goal17_18 = Goal(761, 457, 969, 456)
    goal17_19 = Goal(764, 456, 963, 545)
    goal17_20 = Goal(766, 458, 865, 594)

    goal18 = Goal(750, 460, 750, 600)
    goal19 = Goal(670, 460, 670, 600)
    goal19_5 = Goal(590, 460, 590, 600)
    goal20 = Goal(510, 460, 510, 600)
    goal20_5 = Goal(430, 460, 430, 600)
    goal21 = Goal(350, 460, 350, 600)
    goal21_5 = Goal(280, 460, 278, 600)
    goal22 = Goal(190 ,490,233, 560)
    goal22_5_1 = Goal(171 ,486,171, 599)
    goal22_5 = Goal(80,600,175,440)
    goal23 = Goal(150,420,0,570)
    goal23_5 = Goal(0,450,130,400)
    goal24 = Goal(0,380,130,380)

    goals.append(goal1)
    goals.append(goal2)
    goals.append(goal2_5)
    goals.append(goal3)
    goals.append(goal3_5)
    goals.append(goal4)
    goals.append(goal4_5)
    goals.append(goal5)
    goals.append(goal5_5)
    goals.append(goal6)
    goals.append(goal6_5)
    goals.append(goal7_5)
    goals.append(goal8)
    goals.append(goal9)
    goals.append(goal9_5)
    goals.append(goal10)
    goals.append(goal10_5)
    goals.append(goal11)
    goals.append(goal12)
    goals.append(goal13)
    goals.append(goal13_1)
    goals.append(goal15)
    goals.append(goal16)
    goals.append(goal17)
    goals.append(goal17_1)
    goals.append(goal17_2)
    goals.append(goal17_3)
    goals.append(goal17_4)
    goals.append(goal17_5)
    goals.append(goal17_6)
    goals.append(goal17_7)
    goals.append(goal17_8)
    goals.append(goal17_9)
    goals.append(goal17_10)
    goals.append(goal17_11)
    goals.append(goal17_12)
    goals.append(goal17_13)
    goals.append(goal17_14)
    goals.append(goal17_14_1)
    goals.append(goal17_16)
    goals.append(goal17_17)
    goals.append(goal17_18)
    goals.append(goal17_19)
    goals.append(goal17_20)
    goals.append(goal18)
    goals.append(goal19)
    goals.append(goal19_5)
    goals.append(goal20)
    goals.append(goal20_5)
    goals.append(goal21)
    goals.append(goal21_5)
    goals.append(goal22)
    goals.append(goal22_5_1)
    goals.append(goal22_5)
    goals.append(goal23)
    goals.append(goal23_5)
    goals.append(goal24)

    goals[len(goals) - 1].isactiv = True

    return (goals)

def distance(pt1, pt2):
    return(((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)**0.5)

def rotate(origin,point,angle):
    qx = origin.x + math.cos(angle) * (point.x - origin.x) - math.sin(angle) * (point.y - origin.y)
    qy = origin.y + math.sin(angle) * (point.x - origin.x) + math.cos(angle) * (point.y - origin.y)
    q = myPoint(qx, qy)
    return q

def rotateRect(pt1, pt2, pt3, pt4, angle):

    pt_center = myPoint((pt1.x + pt3.x)/2, (pt1.y + pt3.y)/2)

    pt1 = rotate(pt_center,pt1,angle)
    pt2 = rotate(pt_center,pt2,angle)
    pt3 = rotate(pt_center,pt3,angle)
    pt4 = rotate(pt_center,pt4,angle)

    return pt1, pt2, pt3, pt4

class myPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class myLine:
    def __init__(self, pt1, pt2):
        self.pt1 = myPoint(pt1.x, pt1.y)
        self.pt2 = myPoint(pt2.x, pt2.y)

class Ray:
    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        self.angle = angle

    def cast(self, wall):
        x1 = wall.x1 
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2

        vec = rotate(myPoint(0,0), myPoint(0,-1000), self.angle)
        
        x3 = self.x
        y3 = self.y
        x4 = self.x + vec.x
        y4 = self.y + vec.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            
        if(den == 0):
            den = 0
        else:
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

            if t > 0 and t < 1 and u < 1 and u > 0:
                pt = myPoint(math.floor(x1 + t * (x2 - x1)), math.floor(y1 + t * (y2 - y1)))
                return(pt)

class Car:
    def __init__(self, x, y):
        self.pt = myPoint(x, y)
        self.x = x
        self.y = y
        self.width = 14
        self.height = 30

        self.points = 0

        self.original_image = pygame.image.load("car.png").convert()
        self.image = self.original_image  # This will reference the rotated image.
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect().move(self.x, self.y)

        self.angle = math.radians(180)
        self.soll_angle = self.angle

        self.dvel = 1
        self.vel = 0
        self.velX = 0
        self.velY = 0
        self.maxvel = 12 # before 12

        self.angle = math.radians(180)
        self.soll_angle = self.angle

        self.pt1 = myPoint(self.pt.x - self.width / 2, self.pt.y - self.height / 2)
        self.pt2 = myPoint(self.pt.x + self.width / 2, self.pt.y - self.height / 2)
        self.pt3 = myPoint(self.pt.x + self.width / 2, self.pt.y + self.height / 2)
        self.pt4 = myPoint(self.pt.x - self.width / 2, self.pt.y + self.height / 2)

        self.p1 = self.pt1
        self.p2 = self.pt2
        self.p3 = self.pt3
        self.p4 = self.pt4

        self.distances = []
    

    def action(self, choice):
        if choice == 0:
            pass
        elif choice == 1:
            self.accelerate(self.dvel)
        elif choice == 8:
            self.accelerate(self.dvel)
            self.turn(1)
        elif choice == 7:
            self.accelerate(self.dvel)
            self.turn(-1)
        elif choice == 4:
            self.accelerate(-self.dvel)
        elif choice == 5:
            self.accelerate(-self.dvel)
            self.turn(1)
        elif choice == 6:
            self.accelerate(-self.dvel)
            self.turn(-1)
        elif choice == 3:
            self.turn(1)
        elif choice == 2:
            self.turn(-1)
        pass
    
    def accelerate(self,dvel):
        dvel = dvel * 2

        self.vel = self.vel + dvel

        if self.vel > self.maxvel:
            self.vel = self.maxvel
        
        if self.vel < -self.maxvel:
            self.vel = -self.maxvel
        
        
    def turn(self, dir):
        self.soll_angle = self.soll_angle + dir * math.radians(15)
    
    def update(self):

        #drifting code 

        # if(self.soll_angle > self.angle):
        #     if(self.soll_angle > self.angle + math.radians(10) * self.maxvel / ((self.velX**2 + self.velY**2)**0.5 + 1)):
        #         self.angle = self.angle + math.radians(10) * self.maxvel / ((self.velX**2 + self.velY**2)**0.5 + 1)
        #     else:
        #         self.angle = self.soll_angle
        
        # if(self.soll_angle < self.angle):
        #     if(self.soll_angle < self.angle - math.radians(10) * self.maxvel / ((self.velX**2 + self.velY**2)**0.5 + 1)):
        #         self.angle = self.angle - math.radians(10) * self.maxvel / ((self.velX**2 + self.velY**2)**0.5 + 1)
        #     else:
        #         self.angle = self.soll_angle
        
        self.angle = self.soll_angle

        vec_temp = rotate(myPoint(0,0), myPoint(0,self.vel), self.angle)
        self.velX, self.velY = vec_temp.x, vec_temp.y

        self.x = self.x + self.velX
        self.y = self.y + self.velY

        self.rect.center = self.x, self.y

        self.pt1 = myPoint(self.pt1.x + self.velX, self.pt1.y + self.velY)
        self.pt2 = myPoint(self.pt2.x + self.velX, self.pt2.y + self.velY)
        self.pt3 = myPoint(self.pt3.x + self.velX, self.pt3.y + self.velY)
        self.pt4 = myPoint(self.pt4.x + self.velX, self.pt4.y + self.velY)

        self.p1 ,self.p2 ,self.p3 ,self.p4  = rotateRect(self.pt1, self.pt2, self.pt3, self.pt4, self.soll_angle)

        self.image = pygame.transform.rotate(self.original_image, 90 - self.soll_angle * 180 / math.pi)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)

    def cast(self, walls):

        ray1 = Ray(self.x, self.y, self.soll_angle)
        ray2 = Ray(self.x, self.y, self.soll_angle - math.radians(30))
        ray3 = Ray(self.x, self.y, self.soll_angle + math.radians(30))
        ray4 = Ray(self.x, self.y, self.soll_angle + math.radians(45))
        ray5 = Ray(self.x, self.y, self.soll_angle - math.radians(45))
        ray6 = Ray(self.x, self.y, self.soll_angle + math.radians(90))
        ray7 = Ray(self.x, self.y, self.soll_angle - math.radians(90))
        ray8 = Ray(self.x, self.y, self.soll_angle + math.radians(180))

        ray9 = Ray(self.x, self.y, self.soll_angle + math.radians(10))
        ray10 = Ray(self.x, self.y, self.soll_angle - math.radians(10))
        ray11 = Ray(self.x, self.y, self.soll_angle + math.radians(135))
        ray12 = Ray(self.x, self.y, self.soll_angle - math.radians(135))
        ray13 = Ray(self.x, self.y, self.soll_angle + math.radians(20))
        ray14 = Ray(self.x, self.y, self.soll_angle - math.radians(20))

        ray15 = Ray(self.p1.x,self.p1.y, self.soll_angle + math.radians(90))
        ray16 = Ray(self.p2.x,self.p2.y, self.soll_angle - math.radians(90))

        ray17 = Ray(self.p1.x,self.p1.y, self.soll_angle + math.radians(0))
        ray18 = Ray(self.p2.x,self.p2.y, self.soll_angle - math.radians(0))

        self.rays = []
        self.rays.append(ray1)
        self.rays.append(ray2)
        self.rays.append(ray3)
        self.rays.append(ray4)
        self.rays.append(ray5)
        self.rays.append(ray6)
        self.rays.append(ray7)
        self.rays.append(ray8)

        self.rays.append(ray9)
        self.rays.append(ray10)
        self.rays.append(ray11)
        self.rays.append(ray12)
        self.rays.append(ray13)
        self.rays.append(ray14)

        self.rays.append(ray15)
        self.rays.append(ray16)

        self.rays.append(ray17)
        self.rays.append(ray18)


        observations = []
        self.closestRays = []

        for ray in self.rays:
            closest = None #myPoint(0,0)
            record = math.inf
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    dist = distance(myPoint(self.x, self.y),pt)
                    if dist < record:
                        record = dist
                        closest = pt

            if closest: 
                #append distance for current ray 
                self.closestRays.append(closest)
                observations.append(record)
               
            else:
                observations.append(1000)

        for i in range(len(observations)):
            #invert observation values 0 is far away 1 is close
            observations[i] = ((1000 - observations[i]) / 1000)

        observations.append(self.vel / self.maxvel)
        return observations

    def collision(self, wall):

        line1 = myLine(self.p1, self.p2)
        line2 = myLine(self.p2, self.p3)
        line3 = myLine(self.p3, self.p4)
        line4 = myLine(self.p4, self.p1)

        x1 = wall.x1 
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2

        lines = []
        lines.append(line1)
        lines.append(line2)
        lines.append(line3)
        lines.append(line4)

        for li in lines:
            
            x3 = li.pt1.x
            y3 = li.pt1.y
            x4 = li.pt2.x
            y4 = li.pt2.y

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            
            if(den == 0):
                den = 0
            else:
                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

                if t > 0 and t < 1 and u < 1 and u > 0:
                    return(True)
        
        return(False)
    
    def score(self, goal):
        
        line1 = myLine(self.p1, self.p3)

        vec = rotate(myPoint(0,0), myPoint(0,-50), self.angle)
        line1 = myLine(myPoint(self.x,self.y),myPoint(self.x + vec.x, self.y + vec.y))

        x1 = goal.x1 
        y1 = goal.y1
        x2 = goal.x2
        y2 = goal.y2
            
        x3 = line1.pt1.x
        y3 = line1.pt1.y
        x4 = line1.pt2.x
        y4 = line1.pt2.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        
        if(den == 0):
            den = 0
        else:
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

            if t > 0 and t < 1 and u < 1 and u > 0:
                pt = math.floor(x1 + t * (x2 - x1)), math.floor(y1 + t * (y2 - y1))

                d = distance(myPoint(self.x, self.y), myPoint(pt[0], pt[1]))
                if d < 20:
                    #pygame.draw.circle(win, (0,255,0), pt, 5)
                    self.points += GOALREWARD
                    return(True)

        return(False)

    def reset(self):

        self.x = 86
        self.y = 288
        self.velX = 0
        self.velY = 0
        self.vel = 0
        self.angle = math.radians(180)
        self.soll_angle = self.angle
        self.points = 0

        self.pt1 = myPoint(self.pt.x - self.width / 2, self.pt.y - self.height / 2)
        self.pt2 = myPoint(self.pt.x + self.width / 2, self.pt.y - self.height / 2)
        self.pt3 = myPoint(self.pt.x + self.width / 2, self.pt.y + self.height / 2)
        self.pt4 = myPoint(self.pt.x - self.width / 2, self.pt.y + self.height / 2)

        self.p1 = self.pt1
        self.p2 = self.pt2
        self.p3 = self.pt3
        self.p4 = self.pt4

    def draw(self, win):
        win.blit(self.image, self.rect)

class RacingEnv:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        self.fps = 120
        self.width = 1000
        self.height = 600
        self.history = []

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("RACING DQN")
        self.screen.fill((0,0,0))
        self.back_image = pygame.image.load("track.png").convert()
        self.back_rect = self.back_image.get_rect().move(0, 0)
        self.action_space = None
        self.observation_space = None
        self.game_reward = 0
        self.score = 0
 
        self.reset()

    def reset(self):
        self.screen.fill((0, 0, 0))

        self.car = Car(86, 288)
        self.walls = getWalls()
        self.goals = getGoals()
        self.game_reward = 0

    def step(self, action):

        done = False
        self.car.action(action)
        self.car.update()
        reward = LIFE_REWARD

        # Check if car passes Goal and scores
        index = 1
        for goal in self.goals:
            
            if index > len(self.goals):
                index = 1
            if goal.isactiv:
                if self.car.score(goal):
                    goal.isactiv = False
                    self.goals[index-2].isactiv = True
                    reward += GOALREWARD

            index = index + 1

        #check if car crashed in the wall
        for wall in self.walls:
            if self.car.collision(wall):
                reward += PENALTY
                done = True

        new_state = self.car.cast(self.walls)
        #normalize states
        # if done:
        #     new_state = None

        return new_state, reward, done

    def render(self, action):

        DRAW_WALLS = True
        DRAW_GOALS = True
        DRAW_RAYS = True

        pygame.time.delay(10)

        self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.back_image, self.back_rect)

        if DRAW_WALLS:
            for wall in self.walls:
                wall.draw(self.screen)
        
        if DRAW_GOALS:
            for goal in self.goals:
                goal.draw(self.screen)
                if goal.isactiv:
                    goal.draw(self.screen)
        
        self.car.draw(self.screen)

        if DRAW_RAYS:
            i = 0
            for pt in self.car.closestRays:
                pygame.draw.circle(self.screen, (0,0,255), (pt.x, pt.y), 5)
                i += 1
                if i < 15:
                    pygame.draw.line(self.screen, (255,255,255), (self.car.x, self.car.y), (pt.x, pt.y), 1)
                elif i >=15 and i < 17:
                    pygame.draw.line(self.screen, (255,255,255), ((self.car.p1.x + self.car.p2.x)/2, (self.car.p1.y + self.car.p2.y)/2), (pt.x, pt.y), 1)
                elif i == 17:
                    pygame.draw.line(self.screen, (255,255,255), (self.car.p1.x , self.car.p1.y ), (pt.x, pt.y), 1)
                else:
                    pygame.draw.line(self.screen, (255,255,255), (self.car.p2.x, self.car.p2.y), (pt.x, pt.y), 1)

        #render controll
        # pygame.draw.rect(self.screen,(255,255,255),(800, 100, 40, 40),2)
        # pygame.draw.rect(self.screen,(255,255,255),(850, 100, 40, 40),2)
        # pygame.draw.rect(self.screen,(255,255,255),(900, 100, 40, 40),2)
        # pygame.draw.rect(self.screen,(255,255,255),(850, 50, 40, 40),2)

        # if action == 4:
        #     pygame.draw.rect(self.screen,(0,255,0),(850, 50, 40, 40))
        # elif action == 6:
        #     pygame.draw.rect(self.screen,(0,255,0),(850, 50, 40, 40))
        #     pygame.draw.rect(self.screen,(0,255,0),(800, 100, 40, 40))
        # elif action == 5:
        #     pygame.draw.rect(self.screen,(0,255,0),(850, 50, 40, 40))
        #     pygame.draw.rect(self.screen,(0,255,0),(900, 100, 40, 40))
        # elif action == 1:
        #     pygame.draw.rect(self.screen,(0,255,0),(850, 100, 40, 40))
        # elif action == 8:
        #     pygame.draw.rect(self.screen,(0,255,0),(850, 100, 40, 40))
        #     pygame.draw.rect(self.screen,(0,255,0),(800, 100, 40, 40))
        # elif action == 7:
        #     pygame.draw.rect(self.screen,(0,255,0),(850, 100, 40, 40))
        #     pygame.draw.rect(self.screen,(0,255,0),(900, 100, 40, 40))
        # elif action == 2:
        #     pygame.draw.rect(self.screen,(0,255,0),(800, 100, 40, 40))
        # elif action == 3:
        #     pygame.draw.rect(self.screen,(0,255,0),(900, 100, 40, 40))

        # score
        text_surface = self.font.render(f'Points {self.car.points}', True, pygame.Color('green'))
        self.screen.blit(text_surface, dest=(0, 0))
        # speed
        text_surface = self.font.render(f'Speed {self.car.vel*-1}', True, pygame.Color('green'))
        self.screen.blit(text_surface, dest=(800, 0))

        self.clock.tick(self.fps)
        pygame.display.update()

    def close(self):
        pygame.quit()



