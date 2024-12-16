from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [{'id': idx, 'task': task} for idx, task in enumerate(tasks)]}), 200

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        task_id = len(tasks)  
        tasks.append(task)
        return jsonify({'id': task_id, 'task': task}), 201
    return jsonify({'error': 'Task is required'}), 400

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        data = request.get_json()
        task = data.get('task')
        if task:
            tasks[task_id] = task
            return jsonify({'id': task_id, 'task': task}), 200
        return jsonify({'error': 'Task is required'}), 400
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)
        return jsonify({'task': task}), 200
    return jsonify({'error': 'Task not found'}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)





