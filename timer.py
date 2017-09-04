import time

class Timer:
	def __init__(self):
		self.startTime = time.time()
		self.lastTime = self.startTime
		self.lastReset = self.startTime
		self.tickRate = 0
		self.tickCount = 0

	def update(self):
		currentTime = time.time()
		self.elapsedTime = currentTime - self.lastTime
		self.lastTime = currentTime
		self.tickCount += 1

		if self.lastTime - self.lastReset > 1:
			self.recomputeStats()

	def recomputeStats(self):
		self.tickRate = round(self.tickCount / (self.lastTime - self.lastReset), 1)
		self.tickCount = 0
		self.lastReset = self.lastTime

	def printStats(self, screen):
		stdscr.addstr(0, 0, "time elapsed: " + str(self.lastTime - self.startTime))
		stdscr.addstr(1, 0, "ticks / sec.: " + str(self.tickRate))
