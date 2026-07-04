class CodingAgent:
    def __init__(self, task): #store task parameter as attribute upon initiation
        self.task = task
        self.results = [] # list to store results

    def plan(self):
        
        steps = [
            self.task, # initial task from agent creation
            "Write the code",
            "Test the code"
        ]
        self.steps = steps

    def execute(self): 
        for step in self.steps: #loops through every step 
            executed_step = f"Completed: {step}" #stores it inside completed variable with a completion string
            self.results.append(executed_step) # append executed step to results

    def run(self): 
        self.results = [] #reset the results list
        self.plan() 
        self.execute()
        return self.results
        
    

agent = CodingAgent("Create a Python calculator")

final_result = agent.run()
print(final_result)