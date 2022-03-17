import pyautogui
import math
import asyncio



async def mouse_movement(every, until, timeout):

	iteration = 0
	pixel_log = []
  x_prev, y_prev = pyautogui.position()
  
	while sum(pixel_log) < until and iteration * every < timeout:

		x, y = pyautogui.position()
		pixel_log.append(abs(x - x_prev))
		pixel_log.append(abs(y - y_prev))

		asyncio.sleep(every)
		x_prev, y_prev = x, y
		iteration += 1

	return pixel_log




def benford_correlation(dataset):

	first_digits = [int(n / pow(10, math.floor(math.log10(n)))) for n in dataset if n != 0] 
	N = len(first_digits)

	distrubution = [first_digits.count(i) / N for i in range(1, 10)]

	benford_distrubution = [math.log10(1 + (1 / x)) for x in range(1, 10)] 
	integral = sum([abs(a - b) for a, b in zip(distrubution, benford_distrubution)])

	return integral




class BeCaptcha:

	def __init__(self, function, min_movement=0.4, every=0.025, threshold=0.7, timeout=5):

		self.function = function
		self.min_movement = min_movement
		self.every = every
		self.threshold = threshold
		self.timeout = timeout


	def __call__(self, *args, **kwargs):

		mouse_log = mouse_movement(every=self.every, until=self.min_movement * sum(pyautogui.size()), timeout=self.timeout)
		benford_distrubution_integral = benford_correlation(mouse_log)
		results = self.function(*args, **kwargs)

		print(benford_distrubution_integral)

		return (True, results) if benford_distrubution_integral < self.threshold else (False, results)

