from body import Body
import time
from curses import wrapper

def main(stdscr):
	bodies = [
		Body(1.989 * 10**30, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}),
		Body(5.972 * 10**24, {'x': 152.1 * 10**9, 'y': 0}, {'x': 0, 'y': 29.29 * 1000})
	]

	startTime = time.time()
	lastTime = startTime

	while (True):
		stdscr.clear()
		currentTime = time.time()
		elapsedTime = (currentTime - lastTime) * 604800 # 1 sec = 1 week
		lastTime = currentTime

		for body in bodies:
			body.update(bodies, elapsedTime)

		bodies[0].draw(stdscr, 's')
		bodies[1].draw(stdscr, 'e')

		stdscr.addstr(20, 0, "time elapsed: " + str(currentTime - startTime))
		stdscr.refresh()

		time.sleep(.005)

wrapper(main)