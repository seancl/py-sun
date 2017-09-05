from body import Body
from timer import Timer
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
		elif c == ']':
			Timer.scale *= 2
		elif c == '[':
			Timer.scale *= 0.5
		elif c == 'q':
			return 'quit'

def main(stdscr):
	# Spawn player as the moon
	player = Body('@', 1, (152.1 * 10**9 + 7378000, 0), (0, (29.29 + 7.35) * 1000))

	bodies = [
		# Sol
		Body('S', 1.989 * 10**30, (0, 0), (0, 0)),
		# Mercury at aphelion
		Body('h', 0.330 * 10**24, (69.8 * 10**9, 0), (0, 38.86 * 1000)),
		# Venus at aphelion
		Body('v', 4.870 * 10**24, (108.9 * 10**9, 0), (0, 34.79 * 1000)),
		# Earth at aphelion
		Body('e', 5.972 * 10**24, (152.1 * 10**9, 0), (0, 29.29 * 1000)),
		# Mars at aphelion
		Body('m', 0.642 * 10**24, (249.2 * 10**9, 0), (0, 21.97 * 1000)),
		# Jupiter at aphelion
		Body('j', 1.898 * 10**27, (816.6 * 10**9, 0), (0, 12.44 * 1000)),
		# Saturn at aphelion
		Body('s', 0.568 * 10**27, (1514.5 * 10**9, 0), (0, 9.09 * 1000)),
		# Uranus at aphelion
		Body('u', 86.80 * 10**24, (3003.6 * 10**9, 0), (0, 6.49 * 1000)),
		# Neptune at aphelion
		Body('n', 0.102 * 10**27, (4545.7 * 10**9, 0), (0, 5.37 * 1000)),
		# Luna at apogee
		Body('l', 0.07346 * 10**24, ((152.1 + 0.4055) * 10**9, 0), (0, (29.29 + 0.97) * 1000)),
		# player
		player
	]

	stdscr.nodelay(True)
	timer = Timer()

	while (True):
		if checkInput(stdscr) == 'quit':
			break

		stdscr.erase()
		timer.update()

		for body in bodies:
			body.updateVelocity(bodies, timer.getElapsedTime())

		# update positions only after all velocity calculations are done
		for body in bodies:
			body.updatePosition(timer.getElapsedTime())
			body.draw(stdscr, player.pos)

		timer.printStats(stdscr)
		player.dump(stdscr, 4)
		stdscr.refresh()

		timer.limitFpsTo(200)


wrapper(main)