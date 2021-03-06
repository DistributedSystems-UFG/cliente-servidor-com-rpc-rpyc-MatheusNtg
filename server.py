import rpyc
from constCS import * #-
from rpyc.utils.server import ThreadedServer

class Calculator(rpyc.Service):
	def exposed_sum(self, op1, op2):
		print(f"received sum operation with operands {op1} and {op2}")
		return op1 + op2

	def exposed_mult(self, op1, op2):
		print(f"received mult operation with operands {op1} and {op2}")
		return op1 * op2

	def exposed_div(self, op1, op2):
		print(f"received div operation with operands {op1} and {op2}")
		return op1 / op2

	def exposed_sub(self, op1, op2):
		print(f"received sub operation with operands {op1} and {op2}")
		return op1 - op2

if __name__ == "__main__":
	server = ThreadedServer(Calculator(), port = PORT)
	server.start()
