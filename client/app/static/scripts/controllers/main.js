'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
  .controller('MainCtrl', function ($scope) {
    $scope.todos = [
      'Create Django models',
      'Expose them through a REST API',
      'Consume them with restangular'
    ];
  });
