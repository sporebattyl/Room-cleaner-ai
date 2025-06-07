document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const taskList = document.getElementById('tasks');
    const timeToClean = document.getElementById('time-to-clean');
    const itemsIdentified = document.getElementById('items-identified');

    const API_URL = 'http://localhost:8000/api';

    const fetchTasks = async () => {
        try {
            const response = await fetch(`${API_URL}/tasks`);
            const tasks = await response.json();
            updateTaskList(tasks);
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    };

    const analyzeRoom = async () => {
        try {
            const response = await fetch(`${API_URL}/analyze`, { method: 'POST' });
            const result = await response.json();
            updateTaskList(result.messes_identified);
            itemsIdentified.textContent = result.messes_identified.length;
        } catch (error) {
            console.error('Error analyzing room:', error);
        }
    };

    const updateTaskList = (tasks) => {
        taskList.innerHTML = '';
        if (tasks.length === 0) {
            taskList.innerHTML = '<li>No tasks found.</li>';
            return;
        }
        tasks.forEach(task => {
            const li = document.createElement('li');
            li.textContent = task.description;
            taskList.appendChild(li);
        });
    };

    analyzeBtn.addEventListener('click', analyzeRoom);

    fetchTasks();
});