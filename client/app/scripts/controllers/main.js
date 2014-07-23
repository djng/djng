'use strict';

angular.module('app')
  .controller('MainCtrl', function ($scope, tasks) {
    $scope.mytasks = tasks;
  });
