# This is a sample Python script.

import json
from cgshop2021_pyutils import Solution, SolutionStep, SolutionZipWriter, Direction
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase
import numpy as np

from Point import Point
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase

from queueNode import queueNode
from shortestPath import BFS

x=0
idb = InstanceDatabase("/home/ohad/Downloads/cgshop_2021_instances_01.zip")
for i in idb:
    print("Instance:", i)
    x = x + 1
    if x == 2:
        break

board = np.zeros((50, 50))
RobotList = []
robotMatrix = [[0 for i in range(50)] for j in range(50)]


i: Instance #just to enable typing
# print ("I Equal to: ", i)
# i : Instance ("CG:SHOP2021.Instance(name=large_free_005_100x100_50_5000)")
for r in range(i.number_of_robots):
    # print("Robot", i, "starts at", i.start_of(r)," and has to go to ", i.target_of(r))
    start = Point(i.start_of(r)[0], i.start_of(r)[1])
    end = Point(i.target_of(r)[0], i.target_of(r)[1])
    r1 = Robot(start,start,end)
    RobotList.append(r1)
    robotMatrix[i.start_of(r)[0]][i.start_of(r)[1]] = r1
#
for o in i.obstacles:
    x = o[0]
    y = o[1]
    robotMatrix[x][y] = 13

    # print(board)
    # print(o, "is blocked")
# print(RobotList)

# print(robotMatrix)
#
# for i in RobotList:
#     a = BFS(robotMatrix, i.startPlace, i.endPlace)
#     print(a)
    # for p in a.path:
    #     print("X=  " + p[0] + "  Y = " + p[1])


r1 = Robot(Point(0,0), Point(0,0), Point(0,3))
r2 = Robot(Point(2,2), Point(2,2), Point(3,3))
r3 = Robot(Point(1,1), Point(1,1), Point(3,0))

RobotList2 = []
RobotList2.append(r1)
RobotList2.append(r2)
RobotList2.append(r3)
robotMatrix2 = [[0 for i in range(4)] for j in range(4)]
robotMatrix2[0][0] = r1
robotMatrix2[2][2] = r2
robotMatrix2[1][1] = r3

print(robotMatrix2)


for i in RobotList2:
    v = BFS(robotMatrix2, i.startPlace, i.endPlace)
    print(v)
