import sys,tty,termios,atexit
from select import select


def kbhit():
	dr,dww,dde = select([sys.stdin],[],[],0)
	return dr <> []

class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(3)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def get(Antenna):
	if kbhit():
		inkey = _Getch()
		while(1):
			k=inkey()
			if k!='':break
		if k== '\x1b[A':
			Antenna.wpitch += 1
		#	print "UP"
		elif k == '\x1b[B' :
			Antenna.wpitch -= 1
		#	print "down"
		elif k == '\x1b[C':
			Antenna.wyaw += 1
		#	print 'right'
		elif k == '\x1b[D' :
			Antenna.wyaw -= 1
		#	print 'left'

		else:
			print "not an arrow key!"

	 
"""
def main():
	for i in range(0,20):
		get()

if __name__=='__main__':

	main()
"""
