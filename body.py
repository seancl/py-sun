G = 6.67408 * 10 ** -11
AU = 1.496 * 10 ** 11

class Body:
	scale = 2**15 / AU

	def __init__(self, symbol, mass, position, velocity):
		self.symbol = symbol # display character
		self.mass = mass # in kg
		self.pos = position # in m
		self.vel = velocity # in m/s

	def updateVelocity(self, bodies, elapsedTime):
		vectors = list(self.gravityVector(body) for body in bodies)
		netAccel = tuple(sum(v) for v in zip(*vectors))
		self.vel = tuple(v + a*elapsedTime for v,a in zip(self.vel, netAccel))

	def updatePosition(self, elapsedTime):
		self.pos = tuple(p + v*elapsedTime for p,v in zip(self.pos, self.vel))

	def distanceTo(self, otherBody):
		return sum((s - ob)**2 for s,ob in zip(self.pos, otherBody.pos)) ** 0.5

	def gravityVector(self, body):
		dist = self.distanceTo(body)

		if dist == 0:
			return (0, 0)

		accel = G * body.mass / dist**2
		return tuple(-accel * (s - b) / dist for s,b in zip(self.pos, body.pos))

	def draw(self, screen, cameraPos):
		height,width = screen.getmaxyx()
		middlePoint = (round(width/2), round(height/2))
		x,y = tuple(m + round((s - c) * self.scale) for m,s,c in zip(middlePoint, self.pos, cameraPos))
		if 0 <= x < width and 0 < y <= height:
			screen.addstr(height - y, x, self.symbol)

	def dump(self, screen, offset):
		screen.addstr(offset + 0, 0, "mass: " + str(self.mass))
		screen.addstr(offset + 1, 0, "x: " + str(round(self.pos[0] / AU, 5)) + " AU")
		screen.addstr(offset + 2, 0, "y: " + str(round(self.pos[1] / AU, 5)) + " AU")
		screen.addstr(offset + 3, 0, "delta x: " + str(self.vel[0]))
		screen.addstr(offset + 4, 0, "delta y: " + str(self.vel[1]))
