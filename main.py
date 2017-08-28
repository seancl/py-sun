from body import Body
import time
from curses import wrapper
import curses

def checkInput(screen):
	try:
		c = screen.getkey()
	except curses.error:
		pass
	else:
		if c == '+' or c == '=':
			Body.scale *= 2
		elif c == '-':
			Body.scale *= 0.5
		elif c == 'q':
			return 'quit'

def main(stdscr):
	bodies = [
		# Sol
		Body('S', 1.989 * 10**30, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}),
		# Mercury at aphelion
		Body('h', 0.330 * 10**24, {'x': 69.8 * 10**9, 'y': 0}, {'x': 0, 'y': 38.86 * 1000}),
		# Venus at aphelion
		Body('v', 4.870 * 10**24, {'x': 108.9 * 10**9, 'y': 0}, {'x': 0, 'y': 34.79 * 1000}),
		# Earth at aphelion
		Body('e', 5.972 * 10**24, {'x': 152.1 * 10**9, 'y': 0}, {'x': 0, 'y': 29.29 * 1000}),
		# Mars at aphelion
		Body('m', 0.642 * 10**24, {'x': 249.2 * 10**9, 'y': 0}, {'x': 0, 'y': 21.97 * 1000}),
		# Jupiter at aphelion
		Body('j', 1.898 * 10**27, {'x': 816.6 * 10**9, 'y': 0}, {'x': 0, 'y': 12.44 * 1000}),
		# Saturn at aphelion
		Body('s', 0.568 * 10**27, {'x': 1514.5 * 10**9, 'y': 0}, {'x': 0, 'y': 9.09 * 1000}),
		# Uranus at aphelion
		Body('u', 86.80 * 10**24, {'x': 3003.6 * 10**9, 'y': 0}, {'x': 0, 'y': 6.49 * 1000}),
		# Neptune at aphelion
		Body('n', 0.102 * 10**27, {'x': 4545.7 * 10**9, 'y': 0}, {'x': 0, 'y': 5.37 * 1000}),
	]

	stdscr.nodelay(True)
	startTime = time.time()
	lastTime = startTime
	tickTimer = startTime
	tickRate = 0
	frameCount = 0

	while (True):
		if checkInput(stdscr) == 'quit':
			break

		stdscr.erase()

		currentTime = time.time()
		elapsedTime = (currentTime - lastTime) * 604800 # 1 sec = 1 week
		lastTime = currentTime
		frameCount += 1

		if currentTime - tickTimer > 1:
			tickRate = round(frameCount / (currentTime - tickTimer), 1)
			frameCount = 0
			tickTimer = currentTime

		for body in bodies:
			body.update(bodies, elapsedTime)
			body.draw(stdscr)

		stdscr.addstr(0, 0, "time elapsed: " + str(currentTime - startTime))
		stdscr.addstr(1, 0, "ticks / sec.: " + str(tickRate))
		stdscr.refresh()

		time.sleep(.005)

wrapper(main)