/*jshint esversion: 6 */

const printShape = require("./printShape");

for (lin = 1; lin<=10; lin++){
    console.log("Result of triangle(",lin,"):");
    printShape.triangle(lin);
}

for (lin = 2; lin<=11; lin++){
    console.log("\nResult of square(",lin,"):");
    printShape.square(lin);
}

for (lin = 1; lin<=10; lin++){
    console.log("\nResult of rhombus(",lin*2,"):");
    printShape.rhombus(lin*2);
}