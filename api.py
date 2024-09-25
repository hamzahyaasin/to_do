from flask import Flask, jsonify, request

app = Flask(__name__)



#initial data
tasks = [
    {"id": 1, "name": "Task 1", "description": "This is task 1"},
    {"id": 2, "name": "Task 2", "description": "This is task 2"},
    {"id": 3, "name": "Task 3", "description": "This is task 3"}
]

@app.route('/')
def home():
    return "Welcome to the TO DO LIST App"

## Get:

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

##POST

app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Task not found"}), 404
    new_task={
        "id":data[-1]['id']+1 if tasks else 1,
        "name": request.json['name'],
        "description":request.json["description"]
    }
    tasks.append(new_task)
    return jsonify(new_task)


## PUT
@app.route('/tasks/<int:task_id>',methods=['PUT'])
def updated_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({"error": "Task not found"}), 404
    task["name"] = request.json.get("name", task["name"])
    task["description"] = request.json.get("name", task["description"])
    
    return jsonify(task)


##DELETE
@app.route('/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"result":"Task deleted successfully"})
        
    


if __name__ == '__main__':
    app.run(debug=True)