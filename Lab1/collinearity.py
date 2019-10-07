
class Point:
	def __init__(self, coordinateX = 0, coordinateY = 0, coordinateZ = 0):
		self.__coordinateX = coordinateX
		self.__coordinateY = coordinateY
		self.__coordinateZ = coordinateZ

	def readData(self):
		self.__coordinateX = float(input("Enter the first coordinate of the point: "))
		self.__coordinateY = float(input("Enter the second coordinate of the point: "))
		self.__coordinateZ = float(input("Enter the third coordinate of the point: "))


	def writeData(self):
		print("The first coordinate of the point is {}".format(self.__coordinateX))
		print("The second coordinate of the point is {}".format(self.__coordinateY))
		print("The third coordinate of the point is {}".format(self.__coordinateZ))


	def __checkEqual(self, anotherPoint):
		if self.__coordinateX != anotherPoint.__coordinateX:
			return 0
		if self.__coordinateY != anotherPoint.__coordinateY:
			return 0
		if self.__coordinateZ != anotherPoint.__coordinateZ:
			return 0
		return 1


	def getAlpha(self, point1, point2):
		if point1.__coordinateX - self.__coordinateX:
			return (point2.__coordinateX - self.__coordinateX)/(point1.__coordinateX - self.__coordinateX)

		if point1.__coordinateY - self.__coordinateY:
			return (point2.__coordinateY - self.__coordinateY)/(point1.__coordinateY - self.__coordinateY)

		if point1.__coordinateZ - self.__coordinateZ:
			return (point2.__coordinateZ - self.__coordinateZ)/(point1.__coordinateZ - self.__coordinateZ)


	def __checkCollinearity(self, point1, point2):
		if self.__checkEqual(point1) or self.__checkEqual(point2) or point1.__checkEqual(point2):
			return 1
		else:
			alpha = self.getAlpha(point1, point2)
			contor = 0
			if point2.__coordinateX - self.__coordinateX == alpha * (point1.__coordinateX - self.__coordinateX):
				contor += 1
			if point2.__coordinateY - self.__coordinateY == alpha * (point1.__coordinateY - self.__coordinateY):
				contor += 1
			if point2.__coordinateZ - self.__coordinateZ == alpha * (point1.__coordinateZ - self.__coordinateZ):
				contor += 1

			if contor == 3:
				return 1
			else:
				return 0

	def collinearity(self, point1, point2):
		if self.__checkCollinearity(point1, point2):
			print("The points are collinear.")
		else:
			print("The points are not collinear.")

	def affineCombination(self, point1, point2):
		if self.__checkCollinearity(point1, point2):
			if self.__checkEqual(point1):
				print("A1 = 1 * A2 + 0 * A3")
			elif self.__checkEqual(point2):
				print("A1 = 0 * A2 + 1 * A3")
			elif point1.__checkEqual(point2):
				print("A2 = 0 * A1 + 1 * A3")
			else:
				alpha = self.getAlpha(point1, point2)
				print("A3 = {0} * A1 + {1} * A2".format(1-alpha, alpha))


