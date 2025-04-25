from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks (dictionary to simulate database)
tasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_id = len(tasks) + 1
    task_content = request.form['content']
    tasks[task_id] = task_content
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if task_id in tasks:
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
