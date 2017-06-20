var signUp = angular.module("signUp", ["ngRoute"]);

signUp.config(function($routeProvider, $sceDelegateProvider) {
    $routeProvider
        .when('/', {
                templateUrl: 'sign_up.html',
                controller: 'mainController'
        })
        .otherwise({redirectTo: '/'});

    $sceDelegateProvider.resourceUrlWhitelist([
    // Allow same origin resource loads.
    'self'
  ]);
});

// Controller to Add User
signUp.controller("mainController",
    ["$scope", "$http",
    function ($scope, $http) {
       // click function to handle when user gives new user name
      $scope.click = function (phoneNumber) {
        $scope.number = api_key;
	url = 'http://http://34.210.213.199:8080/add_number/123451';
        $http.get(url).success(function (data) {
	    $scope.number = 'lol'
	})
      }
    }
]);

var api_key = process.env.auth_token;
