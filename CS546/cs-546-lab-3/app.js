const bluebird = require("bluebird");
const fileData = require("./fileData.js");
const testMertics = require("./textMetrics.js");

const fs = bluebird.promisifyAll(require("fs"));

async function doSthToFile(path){
    if (!path) throw "You must provide a path";
    if (typeof path !== "string") throw "You must provide a string as path";
    // Get the base URL of path
    var baseURL = path.substr(0, path.lastIndexOf("/")+1);
    // Get the full name of the file
    var fnamewithext = path.replace(/^.*[\\\/]/, '');
    // Get the name of file with out extension
    var filename = fnamewithext.replace(/\.[^/.]+$/, "");
    // Get the extension name (only last one) | Not used in this task
    // var extension = fnamewithext.slice((Math.max(0, fnamewithext.lastIndexOf(".")) || Infinity) + 1);
    
    // Check if result file exists
    var resultFilePath = baseURL+filename+".result.json";
    if (fs.existsSync(resultFilePath)) {
        try {
            jsonObj = await fileData.getFileAsJSON(resultFilePath);
            console.log(jsonObj);
        }
        // handle the promise reject 
        catch (error) {
            console.log(error);
        }
    }
    else {
        try {
            rawString = await fileData.getFileAsString(path);
            simpString = testMertics.simplify(rawString);
            successf1 = await fileData.saveStringToFile(baseURL+filename+".debug.text", simpString);
            jsonObj = testMertics.createMetrics(simpString);
            console.log(jsonObj);
            successf2 = await fileData.saveJSONToFile(baseURL+filename+".result.json",jsonObj);
        }
        catch(error) {
            console.log(error);
        }
    }
}

async function main(){
    await doSthToFile("./chapter1.txt");
    await doSthToFile("./chapter2.txt");
    await doSthToFile("./chapter3.txt");
}

main();