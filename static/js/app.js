'use strict';

var myApp = angular.module('myApp', [
 'ngRoute',
]);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/index.html',
             }).
             when('/scrape', {
                 templateUrl: '../static/partials/scrape.html',
             }).
             when('/settings', {
                 templateUrl: '../static/partials/settings.html',
             }).
             when('/summary', {
                 templateUrl: '../static/partials/summary.html',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);