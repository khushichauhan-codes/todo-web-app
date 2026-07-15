from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # ab har task ek dictionary hoga: {"name": "...", "done": False}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_name = request.form.get('task')
    if task_name:
        tasks.append({"name": task_name, "done": False})
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]  # toggle karega
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)