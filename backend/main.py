from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # your frontend origin
    allow_credentials=True,
    allow_methods=["*"],   # or ["GET", "POST"] if you want to restrict
    allow_headers=["*"],   # or specific headers
)

class Item(BaseModel):
    text: str
    desc:str = None
    is_done: bool = False

newItem = Item(text="Sample Task", desc="This is a sample task", is_done=False)

items= []

items.append(newItem)

@app.get("/")
def root():
    return {"Hello" : "World"}

@app.get("/items/itemslistlimit", response_model = list[Item])
def list_items(limit:int = 10):
    lim_items = items[:limit]
    return lim_items

@app.get("/items/itemslist", response_model = list[Item])
def get_items():
    return items

@app.get("/items/{item_id}", response_model = Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        item = items[item_id]
        return item
    raise HTTPException(status_code=404, detail=f"Item {item_id} not found.")
    

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items
#having "item" as the parameter for the route makes it so
# for you to add an item through the route URL
# you would have to do /items?item=your_item
# this is because FastAPI automatically interprets
# function parameters as query parameters for GET requests
# for POST requests, you would typically send the data
# in the request body, not as a query parameter.
# If you want to send data in the body of a POST request,
# you would define a Pydantic model and use it as the parameter type.
# Example:
# from pydantic import BaseModel
# class Item(BaseModel):
#     name: str
#     description: str = None
# @app.post("/items")
# def create_item(item: Item):
#     items.append(item)
#     return items
# This way, you can send a JSON object in the body of the POST request
# with the fields defined in the Item model.
# Example JSON body:
# {
#     "name": "Sample Item",
#     "description": "This is a sample item."
# }
# The above code will correctly parse the JSON body
# and add the item to the items list.
# Remember to install FastAPI and Uvicorn to run this code:
# pip install fastapi uvicorn
# To run the application, use the command:
# uvicorn backend.main:app --reload
# Make sure to run this command in the directory
# where your main.py file is located.
# The --reload flag is useful during development
# as it automatically reloads the server
# when you make changes to the code.
# You can then access the API at http://
# localhost:8000
# and the interactive API docs at http://
# localhost:8000/docs
# or the alternative docs at http://
# localhost:8000/redoc
# Happy coding!
# Note: The above comments are for explanation purposes
# and should not be included in the actual code file.
# They are meant to guide you through the process
# of setting up and running a FastAPI application.
# Remove these comments in your actual code file.
# Also, ensure that you have Python installed
# and that you are using a virtual environment
# to manage your project dependencies.
# You can create a virtual environment using:
# python -m venv venv
# Activate it using:
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
# Then install the required packages.
# pip install fastapi uvicorn
# This helps keep your project dependencies isolated
# and manageable.
# Finally, remember to test your API endpoints
# using tools like Postman or curl
# to ensure they work as expected.
# You can also write unit tests using frameworks
# like pytest to automate the testing process.
# This is especially important as your application
# grows in complexity.
# Good luck with your FastAPI project!
# If you have any questions or need further assistance,
# feel free to ask.
# This is a basic example to get you started.
# You can expand upon this by adding more routes,
# implementing error handling, and integrating with a database.
# FastAPI is a powerful framework that allows you
# to build APIs quickly and efficiently.
# Explore the FastAPI documentation for more features
# and best practices: https://fastapi.tiangolo.com/
# Enjoy building your application!
# Remember to keep your code clean and well-documented
# as your project evolves.
# This will help you and others understand the code
# in the future.
# Happy coding with FastAPI!
# End of code

#curl -X POST -H "Content-Type: application/json" 'http://http://127.0.0.1:8000/items?item=apple'
