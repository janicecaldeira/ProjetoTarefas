from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'todolist'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rurtvsom:zz_0duQtTZ-g8ZqV7ErkE-5ZZW5ujLlv@kesavan.db.elephantsql.com/rurtvsom'
db = SQLAlchemy(app)

class Tarefas(db.Model):
   id = db.Column(db.Integer, primary_key = True, autoincrement = True)
   item = db.Column(db.String(200), nullable = False)

   def __init__(self,item):
      self.item = item

@app.route('/')
def index():
   titulo = 'Lista de Tarefas'
   tarefas = Tarefas.query.all()
   return render_template('index.html', titulo=titulo, tarefas=tarefas)

@app.route('/new', methods=['GET', 'POST'])
def new():
   if request.method == 'POST':
      tarefas = Tarefas(
         request.form['item']
      )
   db.session.add(tarefas)
   db.session.commit()
   flash('Tarefa criada!')
   return redirect('/')

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
   tarefa = Tarefas.query.get(id)
   if request.method == 'POST':
      tarefa.item = request.form['item']
      db.session.commit()
      return redirect('/')
   return render_template('index.html', tarefa=tarefa)

@app.route('/delete/<id>')
def delete(id):
   tarefa = Tarefas.query.get(id)
   db.session.delete(tarefa)
   db.session.commit()
   flash('Tarefa excluída')
   return redirect('/')

@app.route('/clear')
def clear():
   tarefas = Tarefas.query.all()
   for i in tarefas:
      itens = Tarefas.query.get(i.id)
      db.session.delete(itens)
      db.session.commit()
   flash('Todas as tarefas foram excluídas')
   return redirect('/')

if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)