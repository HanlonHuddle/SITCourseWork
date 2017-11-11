const express = require('express');
const router = express.Router();
const uuid = require('uuid/v1');

const recipesData = require("../data/recipesData");

router.get("/recipe/:recipeId", (req, res) => {
    // GET	/comments/recipe/:recipeId	Returns a list of all comments in the specified recipe, in the format of: {_id: COMMENT_ID, recipeId: RECIPE_ID, recipeTitle: RECIPE_TITLE, poster: COMMENT_NAME, comment: COMMENT}
    recipesData.getRecipeById(req.params.recipeId).then((recipeRecord) => {
        res.status(200).json(recipeRecord.comments);
    }).catch(() => {
        res.status(404).json({ error: "Recipe not found" });
    });
});

router.get("/:commentId", (req, res) => {
    // GET	/comments/:commentId	Returns the comment specified by that commentId in the format of {_id: COMMENT_ID, recipeId: RECIPE_ID, reciipeTitle: RECIPE_TITLE, poster: COMMENT_NAME, comment: COMMENT}
    recipesData.getCommentById(req.params.commentId).then((commentRecord) => {
        res.status(200).json(commentRecord.comments[0]);
    }).catch(() => {
        res.status(404).json({ error: "Comment not found" });
    });
});

router.post("/:recipeId/", (req, res) => {
    // POST	/comments/:recipeId/	Creates a new comment with the supplied data in the request body for the stated recipe, and returns the new comment
    let newComment = {};
    newComment._id = uuid();
    newComment.poster = req.body.poster;
    newComment.comment = req.body.comment;
    let getRecipe = recipesData.getRecipeById(req.params.recipeId);
    getRecipe.then((recipeRecord) => {
        let updatedData = {comments: [newComment]};
        updatedData.comments = updatedData.comments.concat(recipeRecord.comments);
        return recipesData.updateRecipe(req.params.recipeId, updatedData)
            .then((updatedRecipe) => {
                res.status(200).json(updatedRecipe);
            }).catch((e) => {
                res.status(500).json({ error: e });
            });
    }).catch(() => {
        res.status(404).json({ error: "Recipe not found" });
    });
});

router.put("/:recipeId/:commentId", (req, res) => {
    // PUT	/comments/:recipeId/:commentId	Updates the specified comment for the stated recipe with only the supplied changes, and returns the updated comment
    let updateComment = req.body;
    let getRecipe = recipesData.getRecipeById(req.params.recipeId);
    getRecipe.then((recipeRecord) => {
        for (i=0; i<recipeRecord.comments.length; i++){
            if (recipeRecord.comments[i]._id == req.params.commentId){
                recipeRecord.comments[i].poster = updateComment.poster;
                recipeRecord.comments[i].comment = updateComment.comment;
            }
        }
        return recipesData.updateRecipe(req.params.recipeId, recipeRecord)
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
    // DELETE	/comments/:id	Deletes the comment specified
    recipesData.deleteCommentById(req.params.id).then((result) => {
        res.status(200).json(result);
    }).catch(() => {
        res.status(404).json({ error: "Comment not found" });
    });
});

module.exports = router;