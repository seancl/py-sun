from body import Body
import time
from curses import wrapper

def main(stdscr):
	stdscr.clear()
	bodies = [
		Body(10, {'x': 1, 'y': 0}, {'x': 0, 'y': 0.1}),
		Body(1000000000, {'x': 0, 'y': 0}, {'x': 0, 'y': 0})
	]

	startTime = time.time()
	lastTime = startTime

	while (True):
		stdscr.clear()
		currentTime = time.time()
		elapsedTime = currentTime - lastTime
		lastTime = currentTime

		for body in bodies:
			body.update(bodies, elapsedTime)

		bodies[0].draw(stdscr, 0)
		bodies[1].draw(stdscr, 6)

		stdscr.addstr(20, 0, "time elapsed: " + str(currentTime - startTime))
		stdscr.refresh()

		time.sleep(.005)

wrapper(main)