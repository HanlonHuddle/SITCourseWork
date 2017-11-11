const express = require('express');
const router = express.Router();
const uuid = require('uuid/v1');

const recipesData = require("../data/recipesData");

router.get("/", (req, res) => {
    // GET	/recipes	Responds with a list of all recipes in the format of {_id: RECIPE_ID, title: RECIPE_TITLE}
    recipesData.getAllRecipes().then((recipeList) => {
        res.status(200).json(recipeList);
    }).catch(() => {
        res.status(404).json({ error: "Recipe not found" });
    });
});

router.get("/:id", (req, res) => {
    // GET	/recipes/:id	Responds with the full content of the specified recipe
    recipesData.getRecipeById(req.params.id).then((recipeList) => {
        res.status(200).json(recipeList);
    }).catch(() => {
        res.status(404).json({ error: "Recipe not found" });
    });
});

router.post("/", (req, res) => {
    // POST	/recipes	Creates a recipe with the supplied data in the request body, and returns the new recipe
    req.body._id = uuid();
    recipesData.addRecipe(req.body).then((newPost) => {
        res.status(200).json(newPost);
    }).catch((e) => {
        res.status(500).json({ error: e });
    });
});

router.put("/:id", (req, res) => {
    // PUT	/recipes/:id	Updates the specified recipe with only the supplied changes, and returns the updated recipe
    let updatedData = req.body;
    let getRecipe = recipesData.getRecipeById(req.params.id);
    getRecipe.then(() => {
        return recipesData.updateRecipe(req.params.id, updatedData)
            .then((updatedRecipe) => {
                res.status(200).json(updatedRecipe);
            }).catch((e) => {
                res.status(500).json({ error: e });
            });
    }).catch(() => {
        res.status(404).json({ error: "Recipe not found" });
    });
});

router.delete("/:id", (req, res) => {
    // DELETE	/recipes/:id	Deletes the recipe
    let getRecipe = recipesData.getRecipeById(req.params.id);
    getRecipe.then(() => {
        return recipesData.removeRecipe(req.params.id)
            .then(() => {
                res.sendStatus(200);
            }).catch((e) => {
                res.status(500).json({ error: e });
            });
    }).catch(() => {
        res.status(404).json({ error: "Recipe not found" });
    });
});

module.exports = router;