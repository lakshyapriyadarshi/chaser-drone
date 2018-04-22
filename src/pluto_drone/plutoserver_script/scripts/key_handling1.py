#!/usr/bin/env python
from plutodrone.srv import *
from plutodrone.msg import *
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import roslib,rospy,time,geometry_msgs.msg
from std_msgs.msg import Empty
from geometry_msgs.msg import PoseArray
from pid_tune.msg import PidTune


fixed = [1,-5,25]
errorsum_z = 0
class send_data():

	def GetData(self,data):
		self.data = data
	def set_pid_value(self,data):
		self.kp_x = data.Kp 
		self.kp_y = data.Kp 
		self.kp_z = data.Kp
		
		self.kd_x = data.Kd
		self.kd_y = data.Kd
		self.kd_z = data.Kd
		
		self.ki_x = data.Ki
		self.ki_y = data.Ki
		self.ki_z = data.Ki

		list_x = [self.kp_x,self.ki_x,self.kd_x]
		list_y = [self.kp_y,self.ki_y,self.kd_y]
		list_z = [self.kp_z,self.ki_z,self.kd_z]
		#return [list_x,list_y,list_z]
		return list_x


	def position(self):
		#print([self.data.poses[0].position.x,self.data.poses[0].position.y,self.data.poses[0].position.z])
		return [self.data.poses[0].position.x,self.data.poses[0].position.y,self.data.poses[0].position.z]

	def __init__(self):
		rospy.init_node('drone_server')
		#self.er = rospy.Publisher('/err',Float32, queue_size=1) 
		self.command_pub = rospy.Publisher('/drone_command', PlutoMsg, queue_size=1)
		
		rospy.Subscriber("/whycon/poses",geometry_msgs.msg.PoseArray,self.GetData)
		rospy.Subscriber('/input_key', Int16, self.indentify_key )
		rospy.Subscriber('/pid_tuning', PidTune, self.set_pid_value )

		self.key_value =0
		#self.errorobj=Float32()
		self.cmd = PlutoMsg()
		self.cmd.rcRoll=self.cmd.rcPitch=self.cmd.rcYaw=self.cmd.rcThrottle=self.cmd.rcAUX1=self.cmd.rcAUX2=self.cmd.rcAUX3 =1500
		self.cmd.rcAUX4 =1000
		
	def pidz(self,z,last_error_z,errorsum_z):
		time = 1
		sp_z=fixed[2]
		pv_z = z
		'''kp_z = 0.04
		ki_z = 0.0000045
		kd_z = 0.061'''
		kp_z = 0
		vf_z = 0
		errordif_z = 0.0
		error_z = pv_z-sp_z
		errordif_z = (error_z - last_error_z)/time
		errorsum_z = errorsum_z + (error_z*time)		
		vf_z = kp_z*error_z + ki_z*errorsum_z + kd_z*errordif_z
		last_error_z = error_z 
		change = [vf_z,last_error_z,errorsum_z]
		return change

	def pidx(self,x,last_error_x,errorsum_x):
		time = 1
		sp_x=fixed[0]
		pv_x = x
		kp_x = 0.0009
		ki_x = 0.0000001
		kd_x = 0.0002
		vf_x = 0
		errordif_x = 0.0
		error_x = sp_x-pv_x
		errordif_x = (error_x - last_error_x)/time
		errorsum_x = errorsum_x + (error_x*time)		
		vf_x = kp_x*error_x + ki_x*errorsum_x + kd_x*errordif_x
		last_error_x = error_x
		change = [vf_x,last_error_x,errorsum_x]
		return change

	def pidy(self,y,last_error_y,errorsum_y):
		time = 1
		sp_y=fixed[1]
		pv_y = y
		kp_y = 0.0009
		ki_y = 0.0000001
		kd_y = 0.0002
		vf_y = 0
		errordif_y = 0.0
		error_y = pv_y-sp_y
		errordif_y = (error_y - last_error_y)/time
		errorsum_y = errorsum_y + (error_y*time)		
		vf_y = kp_y*error_y + ki_y*errorsum_y + kd_y*errordif_y
		last_error_y = error_y
		change = [vf_y,last_error_y,errorsum_y]
		return change

	def throttle_control(self):
		#rospy.sleep(0.1)
		self.cmd.rcRoll = 1494
		self.cmd.rcPitch = 1494
		self.cmd.rcThrottle = 1650
		while (1):
			self.command_pub.publish(self.cmd)
			time.sleep(0.022000)
		'''#rospy.sleep(0.1)
		self.cmd.rcThrottle = 1700
		self.command_pub.publish(self.cmd)
		#time.sleep(0.022000)
		#rospy.sleep(0.1)
		self.cmd.rcThrottle = 1800
		#time.sleep(0.022000)
		self.command_pub.publish(self.cmd)
		self.cmd.rcThrottle = 1900
		#time.sleep(0.022000)
		self.command_pub.publish(self.cmd)
		while(1):
			self.cmd.rcThrottle = 2000
			self.cmd.rcRoll = 1500
			self.cmd.rcPitch =1500
			self.command_pub.publish(self.cmd)
		#rospy.sleep(0.1)
			time.sleep(0.022000)'''


	
	def pid_in_throttle(self):
		self.cmd.rcRoll =1488
		self.cmd.rcPitch =1490
		self.cmd.rcThrottle = 1500
		lerz=errsz=0
		while (1):
			pos = self.position()
			if abs(fixed[2]-pos[2])>0.5:
				get_factor_z = self.pidz(pos[2],lerz,errsz)
				self.cmd.rcThrottle = self.cmd.rcThrottle + get_factor_z[0]
				if self.cmd.rcThrottle > 2000:
					self.cmd.rcThrottle = 2000
				if self.cmd.rcThrottle < 1450:
					self.cmd.rcThrottle = 1450
				lerz=get_factor_z[1]
				errsz=get_factor_z[2]
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)
			else:
				#self.cmd.rcThrottle = 1700
				lerz=errsz=0
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)

	def pid_in_xyz_1(self):
		lerx=errsx=lery=errsy=lerz=errsz=0
		self.cmd.rcRoll =1488
		self.cmd.rcPitch =1490
		self.cmd.rcThrottle = 1500
		
		while (1):
			pos = self.position()
			if abs(fixed[2]-pos[2])>0.5 or abs(fixed[1]-pos[1])>0.5 or abs(fixed[0]-pos[0])>0.5:
				if abs(fixed[2]-pos[2])>0.5:
					get_factor_z = self.pidz(pos[2],lerz,errsz)
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
				
				if abs(fixed[0]-pos[0])>1:
					get_factor_x = self.pidx(pos[0],lerx,errsx)
					self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
					if self.cmd.rcRoll > 1515:
						self.cmd.rcRoll = 1515
					if self.cmd.rcRoll < 1470:
						self.cmd.rcRoll = 1470
					lerx=get_factor_x[1]
					errsx=get_factor_x[2]
				
				else:
					self.cmd.rcRoll = 1488
					lerx=errsx=0
					
				if abs(fixed[1]-pos[1])>1:
					get_factor_y = self.pidy(pos[1],lery,errsy)
					self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
					if self.cmd.rcPitch > 1515:
						self.cmd.rcPitch = 1515
					if self.cmd.rcPitch < 1470:
						self.cmd.rcPitch = 1470
					lery=get_factor_y[1]
					errsy=get_factor_y[2]
				else:
					self.cmd.rcPitch = 1490
					lery=errsy=0
	


				lerx=get_factor_x[1]
				errsx=get_factor_x[2]
				lery=get_factor_y[1]
				errsy=get_factor_y[2]
				lerz=get_factor_z[1]
				errsz=get_factor_z[2]
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)
			else:
				#self.cmd.rcThrottle = 1700
				lerz=errsz=lerx=errsx=lery=errsy=0
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)


	def pid_in_roll_pitch(self):
		lerx=errsx=lery=errsy=0
		self.cmd.rcRoll =1500
		self.cmd.rcThrottle = 1700
		self.cmd.rcPitch = 1493
		while (1):
			pos=self.position()
			while not (abs(fixed[0]-pos[0])<1 and abs(fixed[1]-pos[1])<1):
				pos=self.position()
				if abs(fixed[0]-pos[0])>1:
					get_factor_x = self.pidx(pos[0],lerx,errsx)
					self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
					if self.cmd.rcRoll > 1550:
						self.cmd.rcRoll = 1550
					if self.cmd.rcRoll < 1450:
						self.cmd.rcRoll = 1450
					lerx=get_factor_x[1]
					errsx=get_factor_x[2]
				
				else:
					self.cmd.rcRoll = 1500
					lerx=errsx=0
					
				if abs(fixed[1]-pos[1])>1:
					get_factor_y = self.pidy(pos[1],lery,errsy)
					self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
					if self.cmd.rcPitch > 1550:
						self.cmd.rcPitch = 1550
					if self.cmd.rcPitch < 1450:
						self.cmd.rcPitch = 1450
					lery=get_factor_y[1]
					errsy=get_factor_y[2]
				else:
					self.cmd.rcPitch = 1493
					lery=errsy=0
				self.cmd.rcThrottle = 1700
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)


			self.cmd.rcRoll =1500
			self.cmd.rcThrottle =1700
			self.cmd.rcPitch =1493
			self.cmd.rcYaw = 1500
			self.command_pub.publish(self.cmd)
			time.sleep(0.022000)
			lerx=errsx=lery=errsy=lerz=errsz=0



	def pid_in_pitch(self):
		lery=errsy=0
		self.cmd.rcRoll =1500
		self.cmd.rcThrottle = 1900
		self.cmd.rcPitch = 1490
		while (1):
			pos = self.position()
			if abs(fixed[1]-pos[1])>1:
				get_factor_y = self.pidy(pos[1],lery,errsy)
				self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
				self.cmd.rcRoll =1500
				self.cmd.rcThrottle = 1900
				if self.cmd.rcPitch > 1550:
					self.cmd.rcPitch = 1550
				if self.cmd.rcPitch < 1450:
					self.cmd.rcPitch = 1450
				lery=get_factor_y[1]
				errsy=get_factor_y[2]
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)


			else:
				self.cmd.rcPitch = 1500
				self.cmd.rcRoll =1500
				self.cmd.rcThrottle = 1900
				lery=errsy=0
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)


	def pid_in_roll(self):
		self.cmd.rcPitch =1493
		self.cmd.rcRoll =1500
		self.cmd.rcThrottle = 1800
		lerx=errsx=0
		while (1):
			pos = self.position()
			if abs(fixed[0]-pos[0])>1:
				get_factor_x = self.pidx(pos[0],lerx,errsx)
				self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
				self.cmd.rcPitch = 1493
				self.cmd.rcThrottle = 1800
				if self.cmd.rcRoll > 1550:
					self.cmd.rcRoll = 1550
				if self.cmd.rcRoll < 1450:
					self.cmd.rcRoll = 1450
				lerx=get_factor_x[1]
				errsx=get_factor_x[2]
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)

			else:
				self.cmd.rcPitch = 1493
				self.cmd.rcRoll =1500
				self.cmd.rcThrottle = 1800
				lerx=errsx=0
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)

	def pid_in_roll_pitch(self):
		lerx=errsx=lery=errsy=0
		self.cmd.rcRoll =1500
		self.cmd.rcThrottle = 1700
		self.cmd.rcPitch = 1493
		while (1):
			pos=self.position()
			while not (abs(fixed[0]-pos[0])<1 and abs(fixed[1]-pos[1])<1):
				pos=self.position()
				if abs(fixed[0]-pos[0])>1:
					get_factor_x = self.pidx(pos[0],lerx,errsx)
					self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
					if self.cmd.rcRoll > 1550:
						self.cmd.rcRoll = 1550
					if self.cmd.rcRoll < 1450:
						self.cmd.rcRoll = 1450
					lerx=get_factor_x[1]
					errsx=get_factor_x[2]
				
				else:
					self.cmd.rcRoll = 1500
					lerx=errsx=0
					
				if abs(fixed[1]-pos[1])>1:
					get_factor_y = self.pidy(pos[1],lery,errsy)
					self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
					if self.cmd.rcPitch > 1550:
						self.cmd.rcPitch = 1550
					if self.cmd.rcPitch < 1450:
						self.cmd.rcPitch = 1450
					lery=get_factor_y[1]
					errsy=get_factor_y[2]
				else:
					self.cmd.rcPitch = 1493
					lery=errsy=0
				self.cmd.rcThrottle = 1700
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)


			self.cmd.rcRoll =1500
			self.cmd.rcThrottle =1700
			self.cmd.rcPitch =1493
			self.cmd.rcYaw = 1500
			self.command_pub.publish(self.cmd)
			time.sleep(0.022000)
			lerx=errsx=lery=errsy=lerz=errsz=0

	def motion_in_xyz_task(self):
		lerx=errsx=lery=errsy=lerz=errsz=0
		self.cmd.rcPitch = 1495
		self.cmd.rcRoll = 1495
		self.cmd.rcThrottle = 1525		
		initial_position = self.position()
		while (1):
			pos=self.position()
			#change = abs(initial_position[2]-pos[2])
			if not (abs(fixed[0]-pos[0])<0.1 and abs(fixed[1]-pos[1])<0.1 and abs(fixed[2]-pos[2])<0.1 ):
				
				if abs(fixed[2]-pos[2])>0.5:
					get_factor_z = self.pidz(pos[2],lerz,errsz)
					self.cmd.rcThrottle = self.cmd.rcThrottle + get_factor_z[0]
					if self.cmd.rcThrottle > 1990:
						self.cmd.rcThrottle = 1990
					if self.cmd.rcThrottle < 1450:
						self.cmd.rcThrottle = 1450
					lerz=get_factor_z[1]
					errsz=get_factor_z[2]
				else:
					lerz=errsz=0

				'''if change < 1:
					self.command_pub.publish(self.cmd)
					time.sleep(0.022000)
					continue'''


				if abs(fixed[0]-pos[0])>0.5:
					get_factor_x = self.pidx(pos[0],lerx,errsx)
					self.cmd.rcRoll = self.cmd.rcRoll + get_factor_x[0]
					if self.cmd.rcRoll > 1515:
						self.cmd.rcRoll = 1515
					if self.cmd.rcRoll < 1485:
						self.cmd.rcRoll = 1485
					lerx=get_factor_x[1]
					errsx=get_factor_x[2]

				else:
					self.cmd.rcRoll = 1500
					lerx=errsx=0
					
				if abs(fixed[1]-pos[1])>0.5:
					get_factor_y = self.pidy(pos[1],lery,errsy)
					self.cmd.rcPitch = self.cmd.rcPitch + get_factor_y[0]
					if self.cmd.rcPitch > 1515:
						self.cmd.rcPitch = 1515
					if self.cmd.rcPitch < 1485:
						self.cmd.rcPitch = 1485
					lery=get_factor_y[1]
					errsy=get_factor_y[2]

				else:
					self.cmd.rcPitch = 1500
					lery=errsy=0
				
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)

			else :
				self.cmd.rcRoll = 1500
				self.cmd.rcPitch = 1500
				self.command_pub.publish(self.cmd)
				time.sleep(0.022000)
				lerx=errsx=lery=errsy=lerz=errsz=0


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
				#self.throttle_control()
				#self.motion_control()
				#self.pid_in_pitch()
				#self.pid_in_roll()
				#self.pid_in_roll_pitch()
				#self.pid_in_throttle()
				self.pid_in_xyz_1()
				#self.motion_in_xyz_task()
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

