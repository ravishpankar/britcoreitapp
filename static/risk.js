app = angular.module('risk',  []);
app.config(['$locationProvider', '$sceDelegateProvider', function AppConfig($locationProvider, $sceDelegateProvider) {
			$sceDelegateProvider.resourceUrlWhitelist([
			   // Allow same origin resource loads.
			   'self',
			   // Allow loading from our assets domain.  Notice the difference between * and **.
   				'https://bcit-static.s3.amazonaws.com/**']);
            $locationProvider.html5Mode({enabled: true, requireBase: false}).hashPrefix('*');
        }]);
app.controller('riskCtrl', function($scope) {
    $scope.v = -1
    $scope.rtname = '';
    $scope.hack = -1
    $scope.showRTC = function() {
        $scope.v = 0;
        $scope.hack = -1
    };

    $scope.showRC = function() {
        $scope.v = 1;
        $scope.hack = -1
    };

    $scope.showRTypes = function() {
        $scope.v = 2;
        $scope.hack = -1
    };

    $scope.setrtname = function(selrt){
        $scope.rtname = selrt;
        $scope.hack = ($scope.hack == 0 ? 1 : 0);
    }
});