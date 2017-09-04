import time

class Timer:
	def __init__(self):
		self._startTime = time.time()
		self._lastTime = self._startTime
		self._lastReset = self._startTime
		self._tickRate = 0
		self._tickCount = 0
		self.elapsedTime = 0

	def update(self):
		currentTime = time.time()
		self.elapsedTime = currentTime - self._lastTime
		self._lastTime = currentTime
		self._tickCount += 1

		if self._lastTime - self._lastReset > 1:
			self.recomputeStats()

	def recomputeStats(self):
		self._tickRate = round(self._tickCount / (self._lastTime - self._lastReset), 1)
		self._tickCount = 0
		self._lastReset = self._lastTime

	def printStats(self, screen):
		stdscr.addstr(0, 0, "time elapsed: " + str(self._lastTime - self._startTime))
		stdscr.addstr(1, 0, "ticks / sec.: " + str(self._tickRate))
