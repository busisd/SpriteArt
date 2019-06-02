from graphics import *
import time

def a():
	i=0
	cur_time = time.time()
	while i<10:
		prev_time = cur_time
		cur_time = time.time()
		print(cur_time-prev_time)
		i+=1
		time.sleep(.2)
		
def main():
	win = GraphWin('Animation!', 640, 640)
	idle_sprite0 = Image(Point(320,320), 'sprite1/idle0_big.png')
	idle_sprite1 = Image(Point(320,320), 'sprite1/idle1_big.png')
	idle_sprite2 = Image(Point(320,320), 'sprite1/idle2_big.png')
	idle_sprite3 = Image(Point(320,320), 'sprite1/idle3_big.png')
	idle = [idle_sprite0, idle_sprite1, idle_sprite2, idle_sprite3]
	
	key = None
	cur_mode = idle
	cur_img = cur_mode[0]
	cur_img.draw(win)
	cur_index = 0
	while (key != 'z'):
		time.sleep(.1)

		key = win.checkKey()
		if key != '':
			print(key)
		
		cur_img.undraw()
		cur_index = (cur_index+1)%len(cur_mode)
		cur_img = cur_mode[cur_index]
		cur_img.draw(win)		

if __name__ == '__main__':
	main()
