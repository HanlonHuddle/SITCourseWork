const bluebird = require("bluebird");
const connection = require("./mongoConnection");
const todoItems = require("./todo");

async function main(){
    try{
        console.log("1.Create a task and log the task:");
        const createdTask = await todoItems.createTask("Ponder Dinosaurs", "Has Anyone Really Been Far Even as Decided to Use Even Go Want to do Look More Like?");
        console.log(createdTask);
        
        console.log("\n2.Then create a new task:\n");
        const createdTask2 = await todoItems.createTask("Play Pokemon with Twitch TV", "Should we revive Helix?");
        // console.log(createdTask2);
        
        console.log("\n3.After the task is inserted, query all tasks and log them:");
        const getTasks = await todoItems.getAllTasks();
        console.log(getTasks);
        
        console.log("\n4.After all the tasks are logged, remove the first task:\n");
        const removeTask = await todoItems.removeTask(createdTask._id);
        // console.log(removeTask);
        
        console.log("5.Query all the remaining tasks and log them:");
        const getTasks2 = await todoItems.getAllTasks();
        console.log(getTasks2);
        
        console.log("\n6.Complete the remaining task:\n");
        for (var i = 0; i< getTasks2.length; i++) {
            await todoItems.completeTask(getTasks2[i]._id);
        }
        
        console.log("7.Log the task that has been completed with its new value:");
        const getTasks3 = await todoItems.getAllTasks();
        console.log(getTasks3);
    } 
    catch (error) {
        console.log(error);
    }
    process.exit();
}

main();