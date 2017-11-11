const palindromesRoutes = require("./palindromes");

const constructorMethod = (app) => {
    app.use("/", palindromesRoutes);
};

module.exports = constructorMethod;