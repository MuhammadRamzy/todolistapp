from flask import Flask, render_template, request,redirect

app = Flask(__name__)

todoList = []

@app.route('/')
def index():
    return render_template('index.html', 
        list=todoList,
        count=len(todoList)
    )

@app.route('/add', methods=['POST'])
def add():

    data = request.form.get('data')
    todoList.append(data)
    return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():

    indexNo = request.form.get('index')

    if (int(indexNo)) <= len(todoList):
        delData = todoList[int(indexNo)-1]
        todoList.remove(delData)
        return redirect('/')
    else:
        return render_template('index.html', 
            message="Please input a valid number",
            list=todoList,
            count=len(todoList)
        )

@app.route('/dltAll')
def allDlt():
    todoList.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
