from fastapi import FastAPI
from pydantic import BaseModel
from retrieval import retrieve_function
from code_generator import generate_code
from memory import SessionMemory

app = FastAPI()  # ✅ This should be defined

memory = SessionMemory()

class RequestBody(BaseModel):
    prompt: str

@app.post("/execute")
async def execute_function(request: RequestBody):
    user_query = request.prompt
    function_name = retrieve_function(user_query)
    
    if function_name:
        generated_code = generate_code(function_name)
        memory.add_to_history(user_query, function_name)
        return {"function": function_name, "code": generated_code}
    
    return {"error": "No matching function found"}

# ✅ Ensure this file is saved as "api.py"
from fastapi import FastAPI

app = FastAPI()

@app.post("/execute")  # Ensure it's a POST request
async def execute_command(data: dict):
    prompt = data.get("prompt")
    if prompt == "Open calculator":
        import os
        os.system("calc")  # Opens the calculator (Windows)
        return {"message": "Calculator opened!"}
    return {"error": "Invalid command"}
