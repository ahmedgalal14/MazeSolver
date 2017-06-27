

'''
' Main just connect all files together
'''
# *5,5,5,30,6,30,7,30,7,49,8,49,9,49,9,30,10,30,11,30,12,30,13,30,14,30,15,30,15,15,16$
# import maze , pyserial time and files
import Tkinter as tk
import cPickle, copy
import serial, time
import maze, arduino_connection

# main function
def main():
        # start point
    init = [28, 28]
    # end point
    goal = [54, 17]
    # cost
    cost = 1
    # require the maze grid
    grid = cPickle.load(open('save.p', 'rb'))
        # object from maze class and perform search
    playground = maze.maze(grid, init, goal, cost)
    path = playground.search()
        # entering the port
    port = "/dev/ttyACM0"
    speed = 115200
    # sending data
    ard = arduino_connection.arduino_connection(path, port, speed)
    # start serial connection
    ard.connect()
        
if __name__ == "__main__":
    main()



