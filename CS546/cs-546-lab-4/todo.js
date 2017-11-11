const bluebird = require("bluebird");
const todoItemsCollection = require("./mongoCollections");
const todoItems = todoItemsCollection.todoItems;
const uuidv1 = require('uuid/v1');

let exportedMethods = {
    async createTask(title, description) {
        if (!title) 
            throw "You must provide a title for the task";
        let newItem={};
        if (!description) 
            throw "You must provide a description for the task";
            await todoItems().then((todoItemsCollection) => {
            let newTodo = {
                _id: uuidv1(),
                title: title,
                description: description,
                completed: false,
                completedAt: null
            };
            todoItemsCollection.insertOne(newTodo);
            newItem = newTodo;
        });
        // resolve to the newly created to-do list object
        return newItem;
    },

    async getAllTasks() {
        return todoItems().then((todoItemsCollection) => {
            let documents = todoItemsCollection.find().toArray();
            return documents;
        });
    },

    async getTask(id) {
        if (!id) 
            throw "You must provide an id to search for";
        let result = await todoItems().then((todoItemsCollection) => {
            return todoItemsCollection.findOne({_id: id});
        });
        if (result == null)
            throw "No result found";
        else
            return result;
    },

    async completeTask(taskId) {
        if (!taskId)
            throw "You must provide an id to search for";
        let task = await this.getTask(taskId); // will reject if not found, since getTask did the job
        if (task == "No result found")
            throw "No result found, in completeTask" ; // useless
        let completedTodo = {
            _id: task._id,
            title: task.title,
            description: task.description,
            completed: true,
            completedAt: new Date()
        };
        result = await todoItems().then((todoItemsCollection) => {
            try {
                todoItemsCollection.updateOne({ _id: taskId }, completedTodo);
            }
            // if by any reason not able to update, will reject
            catch(error) {
                throw error;
            }
        });
        return completedTodo;
    },

    async removeTask(id) {
        if (!id)
            throw "You must provide an id to search for";
        let info = await todoItems().then((todoItemsCollection) => {
            return todoItemsCollection.removeOne({ _id: id });
        });
        if (info.deletedCount == 0) {
            throw "Nothing to delete";
        }
        return true;
    }
}

module.exports = exportedMethods;