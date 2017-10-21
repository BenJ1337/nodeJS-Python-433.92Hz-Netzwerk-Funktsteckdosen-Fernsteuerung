import time 
import sys
import RPi.GPIO as GPIO

#Only for Reciver
#from datetime import datetime
#import matplotlib.pyplot as pyplot

class TransmitterE:
	def __init__( self ):
		self.dauer = 2
		self.pin = 17
		
	def empfangen( self ):
		empfangeneSignale = [[],[]]
		try:
			GPIO.setmode( GPIO.BCM )
			GPIO.setup( self.pin, GPIO.IN )
			duration = 0
			start_point = datetime.now()
    		
    			print("start")
    			while ( duration < self.dauer ):
      				zeitunterschied = datetime.now() - start_point
      				duration = zeitunterschied.seconds
      				empfangeneSignale[0].append( zeitunterschied )
      				empfangeneSignale[1].append( GPIO.input( self.pin ) )
      		
      			print("end")
      			GPIO.cleanup()
  			pyplot.plot( empfangeneSignale[0], empfangeneSignale[1] )
  			pyplot.axis( [1.34, 1.4, -1, 2] )
 			pyplot.show()
  		except Exception:
    			GPIO.cleanup()
  			for i in range( len( empfangeneSignale[0] ) ):
    				empfangeneSignale[0][i] = empfangeneSignale[0][i].seconds + empfangeneSignale[0][i].microseconds/1000000.0


class TransmitterS:
	def __init__( self ):
		self.a_on = '11101100110000110'
		self.a_off = '11101100110000011'
		self.b_on = '11101100011000110'
		self.b_off = '11101100011000011'
		self.c_on = '11101100001100110'
		self.c_off = '11101100001100011'
		self.d_on = '11101100000110110'
		self.d_off = '11101100000110011'
				
		self.short_delay = 0.00025
		self.mid_delay = 0.00045
		self.long_delay = 0.00090
		self.delay = 0.009
		self.numb_iterations = 10
		self.pin = 4

	def transmit_code( self, code ):
  		try:
    			GPIO.setmode(GPIO.BCM) 
    			GPIO.setup( self.pin, GPIO.OUT )
    			for t in range( self.numb_iterations ):
      				for i in code:
       					if( i == '1' ):
         					GPIO.output( self.pin, 1 )
         					time.sleep( self.short_delay )
  	       				 	GPIO.output( self.pin, 0 )
        	  				time.sleep( self.long_delay )
        				elif (i == '0'):
        					GPIO.output( self.pin, 1 )
          					time.sleep( self.long_delay )
     	     					GPIO.output( self.pin, 0 )
        					time.sleep( self.mid_delay )
         		 			GPIO.output( self.pin, 1 )
          					time.sleep( self.short_delay )
          					GPIO.output( self.pin, 0 )
          					time.sleep( self.long_delay )
       		 			else:
         		 			print('Error_ Transmitter.')
      						GPIO.output( self.pin , 0 )
      						time.sleep( self.delay )
    			GPIO.cleanup()
  		except Exception as e: 
    			print(e)
    			GPIO.cleanup()

