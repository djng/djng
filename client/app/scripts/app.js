'use strict';

angular
  .module('app', [
    'ngCookies',
    'ngSanitize',
    'ui.router',
    'restangular'
  ])
  .config(function ($locationProvider, $urlRouterProvider, $stateProvider, $httpProvider, $provide) {
    $locationProvider.html5Mode(true);
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';

    $urlRouterProvider.otherwise("/");

    $stateProvider
      .state('home', {
        url: "/",
        controller: 'MainCtrl',
        templateUrl: "static/views/main.html"
      });

    $provide.constant('tasks', angular.fromJson(angular.copy(window.tasks)).tasks);
  });
