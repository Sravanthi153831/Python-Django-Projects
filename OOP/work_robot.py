class WorkRobot:
	   def __init__(self, name, memory):
	   	 self.name = name
	   	 self.memory = memory
	   def display_status(self):
	   	 print(f"Robot Name:{self.name}")
	   	 print(f"Work level:{self.memory}%")
my_robot = WorkRobot("S-AI Bot", 100)
my_robot.display_status()
print("\n[Robot Compled Successfully!]")
	   	 
	   	 
	   	 
	   	 
	   	 
	   	 
