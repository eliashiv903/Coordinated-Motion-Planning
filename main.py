# This is a sample Python script.

import json
from cgshop2021_pyutils import Solution, SolutionStep, SolutionZipWriter, Direction
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase
import numpy as np
from Robot import Robot
from cgshop2021_pyutils import Instance
from cgshop2021_pyutils import InstanceDatabase




x=0
idb = InstanceDatabase("/home/ohad/Downloads/cgshop_2021_instances_01.zip")
for i in idb:
    print("Instance:", i)
    x = x + 1
    if x == 2:
        break

board = np.zeros((50, 50))
RobotList = []
robotMatrix = [ [ 0 for i in range(50) ] for j in range(50) ]


i: Instance #just to enable typing
# print ("I Equal to: ", i)
# i : Instance ("CG:SHOP2021.Instance(name=large_free_005_100x100_50_5000)")
for r in range(i.number_of_robots):
    # print("Robot", i, "starts at", i.start_of(r)," and has to go to ", i.target_of(r))
    r1 = Robot(i.start_of(r),i.start_of(r),i.target_of(r))
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


print(robotMatrix)
