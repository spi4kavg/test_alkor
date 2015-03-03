define([
    'jquery',
    'backbone',
    'app/models/events'
], function ($, Backbone, EventModel) {
    var EventCollection = Backbone.Collection.extend({
        model: EventModel,
        url: function () {
            return '/api/events/' + "?" + $.param(this.filter);
        },

        filter: {
            'page': 1
        },

        pagination: {
            has_next: false,
            has_prev: false
        },

        parse: function (response) {
            if (response.pagination) {
                this.pagination.has_next = response.pagination.has_next_page;
                this.pagination.has_prev = response.pagination.has_prev_page;
            }
            return response.data;
        },

        setFilter: function (filter) {
            this.filter = $.extend(this.filter, filter);
        },

        fetchPage: function () {
            this.fetch({reset: true});
        },

        fetchNext: function () {
            this.filter['page'] += 1;
            this.fetchPage();
        },

        fetchPrev: function () {
            this.filter['page'] -= 1;
            this.fetchPage();
        }
    });

    return EventCollection;
});