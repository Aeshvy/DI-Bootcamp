export class TodoList {
  constructor() {
    this.tasks = [];
  }

  addTask(task) {
    this.tasks.push({ task, completed: false });
  }

  markTaskComplete(index) {
    if (index >= 0 && index < this.tasks.length) {
      this.tasks[index].completed = true;
    } else {
      throw new Error("Task index out of bounds");
    }
  }

  listTasks() {
    return this.tasks.map((task, index) => ({
      index,
      task: task.task,
      completed: task.completed,
    }));
  }
}

export default TodoList;
