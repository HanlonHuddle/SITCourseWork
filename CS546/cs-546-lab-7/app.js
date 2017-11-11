const bluebird = require("bluebird");
const bodyParser = require("body-parser");

const express = require("express");
let app = express();
app.use(bodyParser.json());
let configRoutes = require("./routes");

configRoutes(app);

app.listen(3000, () => {
    console.log("We've now got a server!");
    console.log("Your routes will be running on http://localhost:3000");
});