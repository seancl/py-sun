G = 6.67408 * 10 ** -11
AU = 1.496 * 10 ** 11

class Body:
	def __init__(self, mass, position, velocity):
		self.mass = mass # in kg
		self.pos = position # in m
		self.vel = velocity # in m/s

	def update(self, bodies, elapsedTime):
		netForce = {'x': 0, 'y': 0}
		for body in bodies:
			accel = self.gravityVector(body)
			netForce['x'] += accel['x']
			netForce['y'] += accel['y']
		self.vel['x'] += netForce['x'] * elapsedTime / self.mass
		self.vel['y'] += netForce['y'] * elapsedTime / self.mass
		self.pos['x'] += self.vel['x'] * elapsedTime
		self.pos['y'] += self.vel['y'] * elapsedTime

	def gravityVector(self, body):
		distSqared = (
			(self.pos['x'] - body.pos['x']) ** 2
			+ (self.pos['y'] - body.pos['y']) ** 2
		)

		if distSqared == 0:
			return {'x': 0, 'y': 0}

		force = G * self.mass * body.mass / distSqared
		return {
			'x': -force * (self.pos['x'] - body.pos['x']) / distSqared ** 0.5,
			'y': -force * (self.pos['y'] - body.pos['y']) / distSqared ** 0.5
		}

	def draw(self, screen, char):
		height,width = screen.getmaxyx()
		centerX = round(width / 2)
		centerY = round(height / 2)
		scale = 10 / AU
		x = centerX + round(self.pos['x'] * scale)
		y = centerY - round(self.pos['y'] * scale)
		if 0 <= x < width && 0 <= y < height:
			screen.addstr(y, x, char)

	def dump(self, screen, offset):
		screen.addstr(offset + 0, 0, "mass: " + str(self.mass))
		screen.addstr(offset + 1, 0, "x: " + str(round(self.pos['x'] / AU, 5)) + " AU")
		screen.addstr(offset + 2, 0, "y: " + str(round(self.pos['y'] / AU, 5)) + " AU")
		screen.addstr(offset + 3, 0, "delta x: " + str(self.vel['x']))
		screen.addstr(offset + 4, 0, "delta y: " + str(self.vel['y']))
