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

    def show_task(self): # agent returns original task
        orig_task = self.task
        return orig_task
    
    def finalize(self): #finalize task and results for it once done
        final = {}
        final["task"] = self.task
        final["results"] = self.results
        return final
    
    def run(self): 
        self.results = [] #reset the results list
        self.plan() 
        self.execute()
        return self.finalize()
        
        
    

agent = CodingAgent("Create a Python calculator")
current_task = agent.show_task()

final_result = agent.run()
print(current_task, "\n",final_result)

#File read tool for the CodingAgent
class FileTool:

    def read_file(self, filename):
        with open(filename, "r") as file:
            data = file.read()
        return data
    
    def write_file(self, filename, content):
        with open(filename, "w") as file:
            file.write(content)
        return f"Wrote: {filename}"
    
file_tool = FileTool()
result = file_tool.write_file("test.py", "print('Hello')")
print(result)