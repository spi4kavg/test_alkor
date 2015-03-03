define([
    'jquery',
    'backbone',
    'app/models/categories'
], function ($, Backbone, CategoriesModel) {
    var CategoriesCollection = Backbone.Collection.extend({
        model: CategoriesModel,
        url: '/api/categories/',
    });

    return CategoriesCollection;
});