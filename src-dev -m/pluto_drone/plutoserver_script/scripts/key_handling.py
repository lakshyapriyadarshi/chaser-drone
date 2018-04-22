#!/usr/bin/env python
from plutodrone.srv import *
from plutodrone.msg import *
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import roslib,rospy,time,geometry_msgs.msg
from std_msgs.msg import Empty
from geometry_msgs.msg import PoseArray

fixed = [1,-5,25]
errorsum_z = 0

fixed = [1,-5,25]
en1 = []
en2 = []
checker = [0,0,0,0,0]
errorsum_z = 0
chaser = [0,0,0]
runner = [0,0,0]
runner_initial = [9.02,2.9,18.2]
waypoint1=[1.04,-1.45,18.50]
waypoint2=[-6.90,5.17,16]
waypoint3=[-9.63,-9.38,20]


class send_data():

	def GetData(self,data):
		self.data = data

	def position(self):
		'''#print([self.data.poses[0].position.x,self.data.poses[0].position.y,self.data.poses[0].position.z])
		file1=open("/home/lekhraj/Desktop/test.txt","r+")
		file1.seek(0,2)

		file1.write("1-"+str(self.data.poses[0].position.x)+"\n2-"+str(self.data.poses[1].position.x)+"\n")
		file1.close()'''
		return [self.data.poses[0].position.x,self.data.poses[0].position.y,self.data.poses[0].position.z,self.data.poses[1].position.x,self.data.poses[1].position.y,self.data.poses[1].position.z]



	def allocate(self):
		e = self.position()
		d1 = ((e[0]-runner_initial[0])**2 ) + ((e[1]-runner_initial[1])**2 ) + ((e[2]-runner_initial[2])**2 )
		d2 = ((e[3]-runner_initial[0])**2 ) + ((e[4]-runner_initial[1])**2 ) + ((e[5]-runner_initial[2])**2 )
		if d1 < d2 :
			return 1
		else:
			return 2

	'''def chaserposition(self):
		a = self.allocate()
		c = a[0:3]
		return c

	def runnerposition(self):
		a = self.allocate()
		c = a[3:6]
		return c'''

	def traversal(self):
		self.cmd.rcPitch = 1500
		self.cmd.rcRoll = 1500
		self.cmd.rcThrottle = 1500		
		w2= list(waypoint1)
		w1= list(waypoint2)
		w3= list(waypoint3)
		#c = self.chaserposition()
		#r = self.runnerposition()
		lerx=errsx=lery=errsy=lerz=errsz=0
		
		while True:
			
			if checker[0] == 0:
				while True:
					p = self.position()
					t = self.allocate()
					if t == 1:
						r = p[0:3]
						c = p[3:6]
					else :
						r = p[3:6]
						c = p[0:3]
					
					if (abs(c[0]-w2[0])>1 or abs(c[1]-w2[1])>1 or abs(c[2]-w2[2])>1):


						if abs(c[0]-w2[0]) > 1:
							get_factor_x = self.pidinx(w2,c[0],lerx,errsx)
							self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
							if self.cmd.rcRoll > 1515:
								self.cmd.rcRoll = 1515
							if self.cmd.rcRoll < 1470:
								self.cmd.rcRoll = 1470
							lerx=get_factor_x[1]
							errsx=get_factor_x[2]
				
						else:
							#self.cmd.rcRoll = 1488
							lerx=errsx=0
						if abs(c[1]-w2[1])>1:
							get_factor_y = self.pidiny(w2,c[1],lery,errsy)
							self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
							if self.cmd.rcPitch > 1515:
								self.cmd.rcPitch = 1515
							if self.cmd.rcPitch < 1470:
								self.cmd.rcPitch = 1470
							lery=get_factor_y[1]
							errsy=get_factor_y[2]
						else:
							#self.cmd.rcPitch = 1490
							lery=errsy=0
						if abs(c[2]-w2[2]) > 1:
							get_factor_z = self.pidinz(w2,c[2],lerz,errsz)
							self.cmd.rcThrottle = self.cmd.rcThrottle + get_factor_z[0]
							if self.cmd.rcThrottle > 2000:
								self.cmd.rcThrottle = 2000
							if self.cmd.rcThrottle < 1450:
								self.cmd.rcThrottle = 1450
							lerz=get_factor_z[1]
							errsz=get_factor_z[2]
						else:
							#self.cmd.rcThrottle = 1700
							lerz=errsz=0
						self.command_pub.publish(self.cmd)
						#c = self.chaserposition()
						
					else:
						checker[0]=1
						lerx=errsx=lery=errsy=lerz=errsz=0
						break

			if checker[1] == 0:
				while True:
					
					p = self.position()
					t = self.allocate()
					if t == 1:
						r = p[0:3]
						c = p[3:6]
					else :
						r = p[3:6]
						c = p[0:3]

					if (abs(c[0]-w3[0])>1 or abs(c[1]-w3[1])>1 or abs(c[2]-w3[2])>1):
						
						if abs(c[0]-w3[0]) > 1:
							get_factor_x = self.pidinx(w3,c[0],lerx,errsx)
							self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
							if self.cmd.rcRoll > 1515:
								self.cmd.rcRoll = 1515
							if self.cmd.rcRoll < 1470:
								self.cmd.rcRoll = 1470
							lerx=get_factor_x[1]
							errsx=get_factor_x[2]
				
						else:
							#self.cmd.rcRoll = 1488
							lerx=errsx=0
						

						if abs(c[1]-w3[1])>1:

							get_factor_y = self.pidiny(w3,c[1],lery,errsy)
							self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
							if self.cmd.rcPitch > 1515:
								self.cmd.rcPitch = 1515
							if self.cmd.rcPitch < 1470:
								self.cmd.rcPitch = 1470
							lery=get_factor_y[1]
							errsy=get_factor_y[2]
						else:
							#self.cmd.rcPitch = 1490
							lery=errsy=0
						
						if abs(c[2]-w3[2]) > 1:
							get_factor_z = self.pidinz(w3,c[2],lerz,errsz)
							self.cmd.rcThrottle = self.cmd.rcThrottle + get_factor_z[0]
							if self.cmd.rcThrottle > 2000:
								self.cmd.rcThrottle = 2000
							if self.cmd.rcThrottle < 1450:
								self.cmd.rcThrottle = 1450
							lerz=get_factor_z[1]
							errsz=get_factor_z[2]
						else:
							#self.cmd.rcThrottle = 1700
							lerz=errsz=0
						self.command_pub.publish(self.cmd)

						#c = self.chaserposition()
						
					else:
						checker[1]=1
						lerx=errsx=lery=errsy=lerz=errsz=0
						break


			if checker[2] == 0:
				while True:
					
					p = self.position()
					t = self.allocate()
					if t == 1:
						r = p[0:3]
						c = p[3:6]
					else :
						r = p[3:6]
						c = p[0:3]

					if (abs(c[0]-w1[0])>1 or abs(c[1]-w1[1])>1 or abs(c[2]-w1[2])>1):
						
						if abs(c[0]-w1[0]) > 1:
							get_factor_x = self.pidinx(w1,c[0],lerx,errsx)
							self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
							if self.cmd.rcRoll > 1515:
								self.cmd.rcRoll = 1515
							if self.cmd.rcRoll < 1470:
								self.cmd.rcRoll = 1470
							lerx=get_factor_x[1]
							errsx=get_factor_x[2]
					
						else:
							#self.cmd.rcRoll = 1488
							lerx=errsx=0
	
						if abs(c[1]-w1[1])>1:
							get_factor_y = self.pidiny(w1,c[1],lery,errsy)
							self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
							if self.cmd.rcPitch > 1515:
								self.cmd.rcPitch = 1515
							if self.cmd.rcPitch < 1470:
								self.cmd.rcPitch = 1470
							lery=get_factor_y[1]
							errsy=get_factor_y[2]
						else:
							#self.cmd.rcPitch = 1490
							lery=errsy=0
						
						
						if abs(c[2]-w1[2]) > 1:
							get_factor_z = self.pidinz(w1,c[2],lerz,errsz)
							self.cmd.rcThrottle = self.cmd.rcThrottle + get_factor_z[0]
							if self.cmd.rcThrottle > 2000:
								self.cmd.rcThrottle = 2000
							if self.cmd.rcThrottle < 1450:
								self.cmd.rcThrottle = 1450
							lerz=get_factor_z[1]
							errsz=get_factor_z[2]
						else:
							#self.cmd.rcThrottle = 1700
							lerz=errsz=0
						self.command_pub.publish(self.cmd)
	

					else:
						checker[2]=1
						lerx=errsx=lery=errsy=lerz=errsz=0
						break
			
			if checker[3] == 0:
				while True:
					
					p = self.position()
					t = self.allocate()
					if t == 1:
						r = p[0:3]
						c = p[3:6]
					else :
						r = p[3:6]
						c = p[0:3]
					
					if  (abs(c[0]-r[0])>1 or abs(c[1]-r[1])>1 or abs(c[2]-r[2])>1):
						
						if abs(c[0]-r[0]) > 1:
							get_factor_x = self.pidinx(r,c[0],lerx,errsx)
							self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
							if self.cmd.rcRoll > 1515:
								self.cmd.rcRoll = 1515
							if self.cmd.rcRoll < 1470:
								self.cmd.rcRoll = 1470
							lerx=get_factor_x[1]
							errsx=get_factor_x[2]
						
						else:
							#self.cmd.rcRoll = 1488
							lerx=errsx=0
	

						if abs(c[1]-r[1])>1:
							get_factor_y = self.pidiny(r,c[1],lery,errsy)
							self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
							if self.cmd.rcPitch > 1515:
								self.cmd.rcPitch = 1515
							if self.cmd.rcPitch < 1470:
								self.cmd.rcPitch = 1470
							lery=get_factor_y[1]
							errsy=get_factor_y[2]
						else:
							#self.cmd.rcPitch = 1490
							lery=errsy=0

						if abs(c[2]-r[2]) > 1:
							get_factor_z = self.pidinz(r,c[2],lerz,errsz)
							self.cmd.rcThrottle = self.cmd.rcThrottle + get_factor_z[0]
							if self.cmd.rcThrottle > 2000:
								self.cmd.rcThrottle = 2000
							if self.cmd.rcThrottle < 1450:
								self.cmd.rcThrottle = 1450
							lerz=get_factor_z[1]
							errsz=get_factor_z[2]
						else:
							#self.cmd.rcThrottle = 1700
							lerz=errsz=0
						self.command_pub.publish(self.cmd)

					else:
						checker[3]=1
						lerx=errsx=lery=errsy=lerz=errsz=0
						break
			#r = self.runnerposition()
			if checker[0]==1 and checker[1]==1 and  checker[2]==1 and checker[3]==1 : 
				self.disarm()
				break 




	def pidiny(self,waypoint,y,last_error_y,errorsum_y):
		time = 1
		sp_y=waypoint[1]
		pv_y = y
		kp_y = 0.001
		ki_y = 0.0000001
		kd_y = 0.00009
		vf_y = 0
		errordif_y = 0.0
		error_y = pv_y-sp_y
		errordif_y = (error_y - last_error_y)/time
		errorsum_y = errorsum_y + (error_y*time)		
		vf_y = kp_y*error_y + ki_y*errorsum_y + kd_y*errordif_y
		last_error_y = error_y
		change = [vf_y,last_error_y,errorsum_y]
		return change

	def pidinx(self,waypoint,x,last_error_x,errorsum_x):
		time = 1
		sp_x=waypoint[0]
		pv_x = x
		kp_x = 0.001
		ki_x = 0.0000001
		kd_x = 0.00009
		vf_x = 0
		errordif_x = 0.0
		error_x = sp_x-pv_x
		errordif_x = (error_x - last_error_x)/time
		errorsum_x = errorsum_x + (error_x*time)		
		vf_x = kp_x*error_x + ki_x*errorsum_x + kd_x*errordif_x
		last_error_x = error_x
		change = [vf_x,last_error_x,errorsum_x]
		return change


	def pidinz(self,waypoint,z,last_error_z,errorsum_z):
		time = 1
		sp_z=waypoint[2]
		pv_z = z
		kp_z = 0.004
		ki_z = 0.0000045
		kd_z = 0.061
		vf_z = 0
		errordif_z = 0.0
		error_z = pv_z-sp_z
		errordif_z = (error_z - last_error_z)/time
		errorsum_z = errorsum_z + (error_z*time)		
		vf_z = kp_z*error_z + ki_z*errorsum_z + kd_z*errordif_z
		last_error_z = error_z 
		change = [vf_z,last_error_z,errorsum_z]
		return change





	def __init__(self):
		rospy.init_node('drone_server')
		#self.er = rospy.Publisher('/err',Float32, queue_size=1) 
		self.command_pub = rospy.Publisher('/drone_command', PlutoMsg, queue_size=1)
		
		rospy.Subscriber("/whycon/poses",geometry_msgs.msg.PoseArray,self.GetData)
		rospy.Subscriber('/input_key', Int16, self.indentify_key )

		self.key_value =0
		#self.errorobj=Float32()
		self.cmd = PlutoMsg()
		self.cmd.rcRoll=1500
		self.cmd.rcPitch=1500
		self.cmd.rcYaw=1500
		self.cmd.rcThrottle=1500
		self.cmd.rcAUX1=1500
		self.cmd.rcAUX2=1500
		self.cmd.rcAUX3 =1500
		self.cmd.rcAUX4 =1000
		
	
	def arm(self):
		self.cmd.rcRoll=1500
		self.cmd.rcYaw=1500
		self.cmd.rcPitch =1500
		self.cmd.rcThrottle =1000
		self.cmd.rcAUX4 =1500
		self.command_pub.publish(self.cmd)
		rospy.sleep(.1)
	def disarm(self):
		self.cmd.rcThrottle =1300
		self.cmd.rcAUX4 = 1200
		self.command_pub.publish(self.cmd)
		rospy.sleep(1)
	
	def indentify_key(self, msg):
		self.key_value = msg.data
	def forward(self):
		self.cmd.rcPitch =1600
		self.command_pub.publish(self.cmd)
	def backward(self):
		self.cmd.rcPitich =1400
		self.command_pub.publish(self.cmd)
	def left(self):
		self.cmd.rcRoll = 1600
		self.command_pub.publish(self.cmd)	
	def right(self):
		self.cmd.rcRoll =1400
		self.command_pub.publish(self.cmd)
	def reset(self):
		self.cmd.rcRoll =1500
		self.cmd.rcThrottle =1500
		self.cmd.rcPitch =1500
		self.cmd.rcYaw = 1500
		self.command_pub.publish(self.cmd)
	def increase_height(self):
		self.cmd.rcThrottle = 1600
		self.command_pub.publish(self.cmd)
	def decrease_height(self):
		self.cmd.rcThrottle =1400
		self.command_pub.publish(self.cmd)

	def control_drone(self):
		while True:
			if self.key_value == 0:         
				self.disarm()
			if self.key_value == 70:
				self.arm()
			if self.key_value == 10:
				self.forward()
			if self.key_value == 20:
				self.reset()
			if self.key_value == 30:
				self.left()
			if self.key_value == 40:
				self.right()
			if self.key_value == 80:
				self.reset()
			if self.key_value == 50:
				self.traversal()
			if self.key_value == 60:
				self.decrease_height()
			if self.key_value == 110:
				self.backward()
			self.command_pub.publish(self.cmd)

if __name__ == '__main__':
	while not rospy.is_shutdown():
		test = send_data()
		test.control_drone()
		rospy.spin()
		sys.exit(1)

