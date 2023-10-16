from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo Pydantic para uma tarefa
class Task(BaseModel):
    title: str
    description: str = None

# Lista de tarefas (simulando um banco de dados)
tasks = []

# Rota para criar uma nova tarefa
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# Rota para buscar todas as tarefas
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

# Rota para buscar uma tarefa específica por índice
@app.get("/tasks/{task_index}", response_model=Task)
def get_task(task_index: int):
    if task_index < 0 or task_index >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tasks[task_index]

# Rota para atualizar uma tarefa existente
@app.put("/tasks/{task_index}", response_model=Task)
def update_task(task_index: int, updated_task: Task):
    if task_index < 0 or task_index >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tasks[task_index] = updated_task
    return updated_task

# Rota para deletar uma tarefa
@app.delete("/tasks/{task_index}", response_model=Task)
def delete_task(task_index: int):
    if task_index < 0 or task_index >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    deleted_task = tasks.pop(task_index)
    return deleted_task

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)