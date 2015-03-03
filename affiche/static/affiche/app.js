define([
    'backbone',
    'app/controllers/events/list',
    'app/controllers/categories/list',
], function (Backbone, EventListController, CategoriesListController) {
    var AppRouter = Backbone.Router.extend({
        routes: {
            '!/:category': 'ListEvents',
            '*defaultAction': 'ListEvents'
        }
    });

    var app_router = new AppRouter;

    app_router.on('route:ListEvents', function (category) {
        var eventListView = new EventListController(category);
        $("#event-list").html(eventListView.render(category).el);

        var categoriesListView = new CategoriesListController();
        categoriesListView.render();
    });

    Backbone.history.start();
});