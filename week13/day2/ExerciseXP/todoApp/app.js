import { TodoList } from './todo.js';

const todos = new TodoList();

todos.addTask("Buy milk");
todos.addTask("Walk the dog");
todos.markTaskComplete(1);

todos.listTasks();
console.log(todos.listTasks());