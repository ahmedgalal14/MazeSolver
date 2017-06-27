'''
' connection class takes an object from the serial library
' and send some data to serial port which in our case an arduino nano
' clean_path is a function we made to send the path in a suitable form
' connect is a function that sends the data
'''
# import pyserial library, and time library will be used for sleep
import serial, time
class arduino_connection(object):
	'''
	' Our beatiful constructor takes the path and port
	'''
	def __init__(self, path, port, speed):
		self.path = path
		self.port = port
		self.speed = speed
	'''
	' clean_path is a function that get rid off some staff we don't need
	' and returns a clean path ready to send to arduino
	'''
	def clean_path(self, old_path):
		# convert the list to string
	    path_to_ard = str(old_path)
	    # iterate over the list to eliminate brackets and parantesess
	    for i in ["[","]","("," "] :  
	        path_to_ard = path_to_ard.replace(i,"")
	    path_to_ard = path_to_ard.replace("),", ",")
	    path_to_ard = path_to_ard.replace(")", "")
	    # concatenate a $ symbol just to let arduino know the end of receive
	    path_to_ard = "*" + path_to_ard + "$"
	    return path_to_ard

	def short_path(self):
                new = []
                x = self.path
                i = 0
                new.append(x[0])
                while i < len(x) - 1:
                        if x[i][0] == x[i + 1][0]:
                                i += 1
                        else:
                                if x[i] not in new:
                                        new.append(x[i])
                                new.append(x[i+1])
                                i += 1
                return new

                
	'''
	' connect is a function that sends the data to arduino 
	'''
	def connect(self):
                print self.clean_path(self.short_path())
                print len(self.clean_path(self.short_path()))
		try:
                        # take an object from serial library
                        arduino = serial.Serial(self.port, self.speed)
                        # delay to give the serial some time to initalize
                        time.sleep = 2
                        # get the final - clean path
                        final_path = self.clean_path(self.short_path())
                        # write the data
                        arduino.write(final_path)
                        print "Successfully written , watch out, the robot! :p"
		except serial.SerialException:
                        print "Ooops, No serial avaliable, Please check the usb port!"
