const mongoCollections = require("../config/mongoCollections");
const recipes = mongoCollections.recipes;
const uuid = require('uuid/v1');

let exportedMethods = {
    
    getAllRecipes() {
        return recipes().then((recipeCollection) => {
            return recipeCollection.find({}).toArray();
        });
    },
    
    getRecipeById(id) {
        return recipes().then((recipeCollection) => {
            return recipeCollection
            .findOne({_id: id})
            .then((recipe) => {
                if (!recipe) 
                throw "Post not found";
                return recipe;
            });
        });
    },
    
    addRecipe(recipeObj) {
        if (typeof recipeObj.title !== "string")
            return Promise.reject("No title provided");

        return recipes().then((recipeCollection) => {
            return recipeCollection
                .insertOne(recipeObj)
                .then((newInsertInformation) => {
                    return newInsertInformation.insertedId;
                })
                .then((newId) => {
                    return this.getRecipeById(newId);
                });
        });
    },
    
    updateRecipe(id, updatedRecipe) {
        return recipes().then((recipeCollection) => {
            let updateCommand = {
                $set: updatedRecipe
            };

            return recipeCollection.updateOne({
                _id: id
            }, updateCommand).then((result) => {
                return this.getRecipeById(id);
            });
        });
    },

    removeRecipe(id) {
        return recipes().then((recipeCollection) => {
            return recipeCollection
                .removeOne({_id: id})
                .then((deletionInfo) => {
                    if (deletionInfo.deletedCount === 0) {
                        throw(`Could not delete post with id of ${id}`)
                    } else {}
                });
        });
    },

    // Comment
    getCommentById(id) {
        return recipes().then((recipeCollection) => {
            return recipeCollection
            .findOne({"comments._id": id},
                {_id : 0, "comments.$": true})
            .then((comment) => {
                if (!comment)
                    throw "Comment not found";
                return comment;
            });
        });
    },

    deleteCommentById(id) {
        return recipes().then((recipeCollection) => {
            return recipeCollection.update( {}, 
                { $pull : { comments : {"_id": id} } }, false, false )
        })
    }
}

module.exports = exportedMethods;