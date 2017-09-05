G = 6.67408 * 10 ** -11
AU = 1.496 * 10 ** 11

class Body:
	scale = 2**13 / AU

	def __init__(self, symbol, mass, position, velocity):
		self.symbol = symbol # display character
		self.mass = mass # in kg
		self.pos = position # in m
		self.vel = velocity # in m/s

	def updateVelocity(self, bodies, elapsedTime):
		netForce = {'x': 0, 'y': 0}
		for body in bodies:
			accel = self.gravityVector(body)
			netForce['x'] += accel['x']
			netForce['y'] += accel['y']
		self.vel['x'] += netForce['x'] * elapsedTime
		self.vel['y'] += netForce['y'] * elapsedTime

	def updatePosition(self, elapsedTime):
		self.pos['x'] += self.vel['x'] * elapsedTime
		self.pos['y'] += self.vel['y'] * elapsedTime

	def distanceTo(self, otherBody):
		return (
			(self.pos['x'] - otherBody.pos['x']) ** 2
			+ (self.pos['y'] - otherBody.pos['y']) ** 2
		) ** 0.5

	def gravityVector(self, body):
		dist = self.distanceTo(body)

		if dist == 0:
			return {'x': 0, 'y': 0}

		accel = G * body.mass / dist**2
		return {
			'x': -accel * (self.pos['x'] - body.pos['x']) / dist,
			'y': -accel * (self.pos['y'] - body.pos['y']) / dist
		}

	def draw(self, screen, cameraPos):
		height,width = screen.getmaxyx()
		centerX = round(width / 2)
		centerY = round(height / 2)
		x = centerX + round((self.pos['x'] - cameraPos['x']) * self.scale)
		y = centerY - round((self.pos['y'] - cameraPos['y']) * self.scale)
		if 0 <= x < width and 0 <= y < height:
			screen.addstr(y, x, self.symbol)

	def dump(self, screen, offset):
		screen.addstr(offset + 0, 0, "mass: " + str(self.mass))
		screen.addstr(offset + 1, 0, "x: " + str(round(self.pos['x'] / AU, 5)) + " AU")
		screen.addstr(offset + 2, 0, "y: " + str(round(self.pos['y'] / AU, 5)) + " AU")
		screen.addstr(offset + 3, 0, "delta x: " + str(self.vel['x']))
		screen.addstr(offset + 4, 0, "delta y: " + str(self.vel['y']))
