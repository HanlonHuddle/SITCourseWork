const bluebird = require("bluebird");
// const Promise = bluebird.Promise;
const fs = bluebird.promisifyAll(require("fs"));

module.exports = {
    async getFileAsString(path) {
        if (!path) throw "You must provide a path";
        if (typeof path !== "string") throw "You must provide a string as path";
        try {
            const content = await fs.readFileAsync(path, "utf-8");
            return content;
        }
        catch(error) {
            // throw error occured during fs reading
            console.log(error);
            throw error;
        }
    },
    async getFileAsJSON(path) {
        if (!path) throw "You must provide a path";
        if (typeof path !== "string") throw "You must provide a string as path";
        try {
            const content = JSON.parse(await fs.readFileAsync(path, "utf-8"));
            return content;
        }
        catch(error) {
            // throw error occured during fs write
            console.log(error);
            throw error;
        }
    },
    async saveStringToFile(path, text) {
        if (!path) throw "You must provide a path";
        if (!text) throw "You must provide a text";
        if (typeof path !== "string") throw "You must provide a string as path";
        if (typeof text !== "string") throw "You must provide a string as text";
        try {
            const stats = await fs.writeFileAsync(path, text);
            return true;
        }
        catch(error) {
            // throw error occured during fs reading
            console.log(error);
            throw error;
        }
    },
    async saveJSONToFile(path, obj) {
        if (!path) throw "You must provide a path";
        if (typeof path !== "string") throw "You must provide a string as path";
        if (!obj) throw "You must provide a JSON object";
        if (typeof obj !== "object") throw "You must provide a JSON object as obj";
        try {
            const stats = await fs.writeFileAsync(path, JSON.stringify(obj));
            return true;
        }
        catch(error) {
            // throw error occured during fs write
            console.log(error);
            throw error;
        }
    }
};