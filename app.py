from flask import Flask, render_template, request, redirect

# create a flask app
app = Flask(__name__)

# create a list to store tasks
tasks = []

# define the home route
@app.route('/')
def index():
    # render the template and pass the tasks list
    return render_template('index.html', tasks=tasks)

# route to handle form submission for adding a task
@app.route('/add', methods=['POST'])
def add():
    # get task from form
    task = request.form.get('task')

    # check if task is not empty
    if task:
        # append task to the list
        tasks.append(task)

    # redirect back to home
    return redirect('/')

# route to delete a task by its index
@app.route('/delete/<int:index>')
def delete(index):
    # check if index is valid
    if 0 <= index < len(tasks):
        # remove task at that index
        tasks.pop(index)

    # redirect back to home
    return redirect('/')

# run the app
if __name__ == '__main__':
    app.run(debug=True)
g
