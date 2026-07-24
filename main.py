import subprocess

# result = subprocess.run(["python", "test.py"], capture_output=True, text=True) # run the test.py and capture the results
# if result.returncode == 0: # no errors return the code
#     print(result.stdout)
# else:                   # if there is an error print the error
#     print(result.stderr) 

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
    


# Code running tool    
class CodeTool:
    def run_code(self, filename):
        result = subprocess.run(["python", filename], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
       
    



#Agent class    
class CodingAgent:
    def __init__(self, task): #store task parameter as attribute upon initiation
        self.task = task
        self.results = [] # list to store results
        self.file_tool = FileTool() #give access to read/write from FileTool class
        self.code_tool = CodeTool() # give access to run code from CodeTool
        self.tools = {
            "read_file": self.read_file,
            "write_file": self.write_file,      #tools registry
            "run_code": self.run_code
        }
    def create_and_run(self, filename, content):
        self.write_file(filename, content)
        result = self.run_code(filename)
        return result

    def read_file(self, filename): #read file from FileTool
        result = self.file_tool.read_file(filename)
        return result
    
    def write_file(self, filename, content): #rite file form FileTool
        result = self.file_tool.write_file(filename, content)
        return result
    
    def run_code(self, code): #Run code from Code
        result = self.code_tool.run_code(code)
        return result

    def plan(self): # plan with actual steps
        parts = self.task.split() # split task in a list
        if len(parts) < 2:
            self.results.append("Invalid task: missing filename")
            self.steps = [] # if less than 2 items, store empty list followed by return
            return 
        command = parts[0].lower() # store the first word of the parts list as command
        filename = " ".join(parts[1:])
        if command == "read": # if command is read
            steps = [
                {
                    "tool": "read_file",
                    "args": {
                        "filename": filename # read second item
                    }
                }
            ]
        elif command == "run":
            steps = [
                {
                    "tool": "run_code",
                    "args": {
                        "filename": filename # read second item
                    }
                }
            ]
        elif command== "write":
            steps = [
                {
                    "tool": "write_file",
                    "args": {
                        "filename": filename, # read second item
                        "content": 'print("Hello World")'
                    }  
                }
            ]
        else:
            self.results.append(f"Unsupported command: {command}")
            self.steps = []
            return
        self.steps = steps

    def execute(self): 
        for step in self.steps: #loops through every step and chooses tool based on tool key
            tool = self.tools.get(step["tool"])

            if tool is None:
                self.results.append(f"Unknown tool: {step['tool']}") # Unknown tools fault tolerance
                continue
            try:
                result = tool(**step["args"])
            except TypeError:
                self.results.append(f"Invalid arguments for tool: {step['tool']}") #Bad arguments( no arguments, etc) fault tolerance
                continue
            except Exception as error:
                self.results.append(f"Tool failed: {step['tool']} - {error}") # tool failed fault tolerance
                continue
            self.results.append(result)
            # if step["tool"] == "write_file":
            #     result = self.write_file(step["filename"], step["content"])
            # elif step["tool"] == "run_code":
            #     result = self.run_code(step["filename"])
            # executed_step = f"Completed: {step}" #stores it inside completed variable with a completion string
            # self.results.append(executed_step) # append executed step to results

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
        
        
    

agent = CodingAgent("Delete hello.py")

# result = agent.create_and_run("test.py", "print('Created and run by agent')")
# print(result)
# run_result = agent.run_code("test.py")
# print(run_result)

#current_task = agent.show_task()
final_result = agent.run()
print(final_result)
#print(current_task, "\n",final_result)
#code_tool = CodeTool()
#result = code_tool.run_code("print('Hello')")
#print(result)
#file_tool = FileTool()
#result = file_tool.write_file("test.py", "print('Hello')")
#print(result)



