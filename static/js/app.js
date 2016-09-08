'use strict';

angular.module('ScrapeIt', ['angularFlaskServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
            .when('/', {
                templateUrl: '/static/partials/index.html',
                controller: IndexController
            })
            .when('/scrape', {
                templateUrl: '../static/partials/scrape.html',
                controller: ScrapeController
            })
            .when('/settings', {
                templateUrl: '../static/partials/settings.html',
                controller: SettingsController
            })
            .when('/summary', {
                templateUrl: '../static/partials/summary.html',
                controller: SummaryController
            })
            .otherwise({
                redirectTo: '/'
            });
            
            $locationProvider.html5Mode(true);
		}]);