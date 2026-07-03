class CodingAgent:
    def __init__(self, task): #store task parameter as attribute upon initiation
        self.task = task
    def run(self):  
        print(self.task)

agent = CodingAgent("Create a Python calculator")

agent.run()