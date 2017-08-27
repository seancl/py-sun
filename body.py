G = 6.67408 * 10 ** -11

class Body:
	def __init__(self, mass, position, velocity):
		self.mass = mass # in kg
		self.pos = position # in m
		self.vel = velocity # in m/s

	def update(self, bodies, elapsedTime):
		for body in bodies:
			accel = self.gravityVector(body)
			self.vel['x'] += accel['x'] * elapsedTime
			self.vel['y'] += accel['y'] * elapsedTime
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

	def draw(self):
		print("mass: ", self.mass)
		print("x: ", self.pos['x'])
		print("y: ", self.pos['y'])
		print("delta x: ", self.vel['x'])
		print("delta y: ", self.vel['y'])
