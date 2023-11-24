odoo.define('airplane.iframe_dashboard_airplane', function (require) {
    'use strict';
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var QWeb = core.qweb;
    var iframe_dashboard = AbstractAction.extend({
        template: 'iFrameAirplane',
        events: {},
        init: function(parent, action) {
           this._super(parent, action);
        },
        start: function() {
           var self = this;
           this.set("title", 'Dashboard');
           //self.load_data();
        },
        load_data: function () {
            //self.$('.table_view').html(QWeb.render('iFrameDashboard'));
            },
    });
    core.action_registry.add("iframe_dashboard_airplane", iframe_dashboard);
    return iframe_dashboard;
});