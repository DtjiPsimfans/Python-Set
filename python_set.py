# Python Set


class PythonSet:
	"""
	This class contains attributes of a python set.
	"""
	
	def __init__(self, elements=[]):
		# type: (list or str) -> None
		self.elements: list = []  # initial value
		for element in elements:
			if element not in self.elements:
				self.elements.append(element)
				
		self.elements = sorted(self.elements)
		
	def add(self, element):
		# type: (object) -> bool
		if element not in self.elements:
			self.elements.append(element)
			self.elements = sorted(self.elements)
			return True
		return False
		
	def remove(self, element):
		# type: (object) -> bool
		if element in self.elements:
			self.elements.remove(element)
			return False
		return True
		
	def concat(self, other):
		# type: (PythonSet) -> None
		for element in other.elements:
			self.add(element)
			
	def subtract(self, other):
		# type: (PythonSet) -> None
		for element in other.elements:
			self.remove(element)
		
	def clear(self):
		# type: () -> None
		self.elements = []
		
	def length(self):
		# type: () -> int
		return len(self.elements)
		
	def __str__(self):
		# type: () -> str
		return str(self.elements)
		
		
# Testing
a: PythonSet = PythonSet()
b: PythonSet = PythonSet([1, 2, 3])
c: PythonSet = PythonSet([1, 4, 4, 2])
d: PythonSet = PythonSet("abc")
print("a = " + str(a))
print("b = " + str(b))
print("c = " + str(c))
print("d = " + str(d))
a.add(5)
print("a = " + str(a))
a.concat(b)
print("a = " + str(a))
a.concat(c)
print("a = " + str(a))
a.subtract(b)
print("a = " + str(a))
b.subtract(c)
print("b = " + str(b))