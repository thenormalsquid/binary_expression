class Node(object):
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None

	def set_left(self, node):
		self.left = node

	def set_right(self, node):
		self.right = node

	def set_data(self, data):
		self.data = data

	def __str__(self):
		return "Data: %(data) , left: %(left) , right: %(right)" % \
			{'data': self.data, 'left': self.left, 'right': self.right}



class BET(object):
	def __init__(self):
		self.operand_stack = []
		self.operator_stack = []
		self.op_table ={"(": 1, ")": 1, "*":2, "/":2, "-":3, "+":3}

	def add_operator(self, operator):
        self.operator_stack.append(str(operator))

    def pop_operator(self):
