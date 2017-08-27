from body import Body
import time

def main():
	bodies = [
		Body(10, {'x': 1000, 'y': 0}, {'x': 0, 'y': 0}),
		Body(100000, {'x': 0, 'y': 0}, {'x': 0, 'y': 0})
	]

	startTime = time.time()

	while (True):
		currentTime = time.time()
		elapsedTime = currentTime - startTime
		for body in bodies:
			body.update(bodies, 1)
		bodies[0].draw()

main()