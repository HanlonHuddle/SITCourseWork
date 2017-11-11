console.log("Function #1:");
function sumOfSquares(a, b, c) {
    if (arguments.length !== 3)
        throw ("Please give three arguements");
    if (isNaN(a) || isNaN(b) || isNaN(c))
        throw ("Please input three numbers");
    return a*a + b*b + c*c;
}
console.log(sumOfSquares(3, 5 ,10));
console.log(sumOfSquares(-3, -5 ,10));
console.log(sumOfSquares(2, -9.6 ,0));
console.log(sumOfSquares(6, -1 ,1));
console.log(sumOfSquares(0, 1 ,1.8));

console.log("\nFunction #2:");
function sayHelloTo(firstName, lastName, title) {
    if (arguments.length === 0)
        throw("You will need at least one parameter to run this function");
    
    if (arguments.length === 1) 
        if (typeof firstName === "string"){
            console.log("Hello, "+firstName+"!");
            return;
        }
        else
            throw("Please input strings as parameter");
    
    if (arguments.length === 2) 
        if (typeof firstName === "string" && typeof lastName === "string"){
            console.log("Hello, "+firstName+" "+lastName+". I hope you are having a good day!");
            return;
        }
        else
            throw("Please input strings as parameter");
        
        if (arguments.length === 3)
            if (typeof firstName === "string" && typeof lastName === "string" && typeof title === "string")
                console.log("Hello, "+title+" "+firstName+" "+lastName+"! Have a good evening!");
            else
                throw("Please input strings as parameter");
        else
            throw("Arguments should not exceed three");
}
sayHelloTo("Phil");
sayHelloTo("Phil", "Barresi");
sayHelloTo("Phil", "Barresi", "Mr.");

console.log("\nFunction #3:");
function cupsOfCoffee(howManyCups) {
    if (arguments.length===0 || isNaN(howManyCups))
        throw("Please input an integer");
    if (howManyCups !== parseInt(howManyCups, 10))
        throw("This is not an integer, try again");
    if (howManyCups <= 0)
        throw("Please input a positive int");
    var result = "";
    for (a=howManyCups; a>1; a--) {
        result+=a+" cups of coffee on the desk! "+a+" cups of coffee!\n";
        result+="Pick one up, drink the cup, "+(a-1)+" cups of coffee on the desk!\n\n";
    }
    result+="1 cup of coffee on the desk! 1 cup of coffee!\n";
    result+="Pick it up, drink the cup, no more coffee left on the desk!";
    return result;
}
console.log(cupsOfCoffee(5));

console.log("\nFunction #4:");
function occurrencesOfSubstring(fullString, substring){
    // new RegExp(substring, "g");
    // return (fullString.match(new RegExp(substring, "g")) || []).length;
    var lastind = 0;
    var result = 0;
    while (lastind < fullString.length) {
        var ind = fullString.indexOf(substring, lastind);
        if ( ind !== -1){
            result++;
            lastind = ind+1;
        }
        else 
            return result;
    }
    return result;
}
console.log(occurrencesOfSubstring("hello world", "o"));
console.log(occurrencesOfSubstring("Helllllllo, class!", "ll"));

console.log("\nFunction #5:");
function randomizeSentences(paragraph) {
    if (typeof paragraph !== "string")
        throw("Please input a string as your sentence");
    var arr = paragraph.split(".");

    for (var i=arr.length-1; i>0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    var result = "";

    // simple trim function
    for (i=arr.length-1; i>=0; i--) {
        arr[i] = arr[i].replace(/^\s+|\s+$/g, '');
        if (arr[i] !== "")
            result+=arr[i]+". ";
    }

    return(result);
}
var paragraph = "Hello, world! I am a paragraph. You can tell that I am a paragraph because there are multiple sentences that are split up by punctuation marks. Grammar can be funny, so I will only put in paragraphs with periods, exclamation marks, and question marks -- no quotations.";
console.log(randomizeSentences(paragraph));
