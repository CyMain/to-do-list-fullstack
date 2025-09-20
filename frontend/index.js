formHTML = `
    <h1>Add a to-do</h1>
    <form id="todo-form">
        <input type="text" name="text" placeholder="Enter your task" required>
        <input type="text" name="desc" placeholder="Description">
        <label>
            Done? <input type="checkbox" name="is_done">
        </label>
        <button type="submit">Add Task</button>
    </form>
`

const contentSection = document.getElementById('content');

const formRenderBtn = document.getElementById('add-render-btn');
const listRenderBtn = document.getElementById('list-render-btn');

formRenderBtn.addEventListener('click', renderToDoAdder);
listRenderBtn.addEventListener('click', renderToDoList);

async function renderToDoList(){
    let todos = []
    console.log("Fetching To-Do List...")
    response = await fetch("http://127.0.0.1:8000/items/itemslist")
    .then(res => res.json())
    .then(data => {
        console.log(data)
        todos = data
        console.log(todos[0].text)
        listHTML = `
            <h1>Your List</h1>
            <ul id="todo-list">
                <!-- To-Do items will be populated here -->
                ${todos.map(todo => `<li class="list-item">${todo.text} - ${todo.desc? todo.desc : "No desc"} - ${todo.is_done ? 'Done' : 'Not Done'}</li>`).join('')}
            </ul>
            `
        contentSection.innerHTML = listHTML;
    })
    
}

function renderToDoAdder(){
    contentSection.innerHTML = formHTML;
    const todoform = document.getElementById('todo-form');
    todoform.addEventListener('submit', async(e)=>{
        e.preventDefault();

        const formData = new FormData(todoform);
        const data = {
            text: formData.get('text'),
            desc: formData.get('desc'),
            is_done: formData.get('is_done') === 'on' ? true : false
        };

        const response = await fetch('http://127.0.0.1:8000/items',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        console.log(result);
    })
}
