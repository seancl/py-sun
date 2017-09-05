import time

class Timer:
	scale = 1.0

	def __init__(self):
		self._startTime = time.time()
		self._lastTime = self._startTime
		self._lastReset = self._startTime
		self._tickRate = 0
		self._tickCount = 0
		self._elapsedTime = 0

	def update(self):
		currentTime = time.time()
		self._elapsedTime = currentTime - self._lastTime
		self._lastTime = currentTime
		self._tickCount += 1

		if self._lastTime - self._lastReset > 1:
			self.recomputeStats()

	def getElapsedTime(self):
		return self._elapsedTime * self.scale

	def recomputeStats(self):
		self._tickRate = round(self._tickCount / (self._lastTime - self._lastReset), 1)
		self._tickCount = 0
		self._lastReset = self._lastTime

	def printStats(self, screen):
		screen.addstr(0, 0, "time elapsed: " + str(self._lastTime - self._startTime))
		screen.addstr(1, 0, "ticks / sec.: " + str(self._tickRate))
		screen.addstr(2, 0, "simulated seconds / sec: "  + str(self.scale))

	def limitFpsTo(self, maxFps):
		targetTime = 1 / maxFps
		actualTime = time.time() - self._lastTime
		if actualTime < targetTime:
			time.sleep(targetTime - actualTime)
