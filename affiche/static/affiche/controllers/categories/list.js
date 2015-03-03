define([
    'jquery',
    'underscore',
    'backbone',
    'app/collections/categories',
    'text!app/views/categories.html',
], function ($, _, Backbone, CategoriesCollection, categoriesListTemplate) {
    var EventListController = Backbone.View.extend({
        el: $("#categories"),

        selected: null,

        initialize: function () {
            this.collection = new CategoriesCollection();
            this.collection.fetch({reset: true});
            this.collection.on('reset', this.render.bind(this));
            this.compiledTemplate = _.template(categoriesListTemplate);
        },

        render: function () {
            this.$el.html(this.compiledTemplate({
                'categories': this.collection.models,
            }));
        }
    });

    return EventListController;
})