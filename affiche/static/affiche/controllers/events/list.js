define([
    'jquery',
    'underscore',
    'backbone',
    'app/collections/events',
    'text!app/views/list.html',
], function ($, _, Backbone, EventsCollection, eventListTemplate) {
    var EventListController = Backbone.View.extend({
        // el: $("#event-list"),
        tagName: 'div',
        events: {
            'click #events li': 'selectEvent',
            'click #pagination li.previous': 'paginatePrev',
            'click #pagination li.next': 'paginateNext',
        },

        selected: null,

        initialize: function (category) {
            this.collection = new EventsCollection();
            if (category) {
                this.collection.setFilter({'category': category});
            }
            this.collection.bind('reset', this.render.bind(this));
            this.collection.fetchPage();
            this.compiledTemplate = _.template(eventListTemplate);
        },

        render: function () {
            this.$el.html(this.compiledTemplate({
                'pagination': this.collection.pagination,
                'events': this.collection.models,
                'selected': (!this.selected)? _.first(this.collection.models): this.selected,
            }));
            return this;
        },

        selectEvent: function () {
            this.render();
            this.selected = this.collection.get($(event.target).data('cid'));
        },

        paginateNext: function () {
            this.collection.fetchNext();
        },

        paginatePrev: function () {
            this.collection.fetchPrev();
        }
    });

    return EventListController;
})