'use strict';

/* Controllers */

function NavBarController($scope, $location) { 
    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
}

function IndexController($scope) {
	
}

function ScrapeController($scope) {
	
}

function SettingsController($scope, Post) {
    
}

function SummaryController($scope, $routeParams, Post) {
    
}

function RegistrationController($scope, $routeParams, Post) {
    
}