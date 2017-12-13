function RTInputController($scope, $http, $element, $attrs) {
  var ctrl = this;
  ctrl.rtlist = [];

  ctrl.getrt = function() {
        $http({
            method : "GET",
            url : "risktypes",
            headers : {"Content-Type" : "application/json"}
            }).then(function successCallback(response) {
                    ctrl.rtlist = response.data
                }, function errorCallback(response) {
                if (response.status == 400) {
                    alert(response.data.message)
                } else {
                    alert("Error trying to get the risk types. Retry.")
                }
            });
  };

  ctrl.getrt();
}

angular.module('risk').component('risktypes',{
      templateUrl:'https://bcit-static.s3.amazonaws.com/risktypes.htm',
      bindings : {setrtname : '<'},
      controller: RTInputController
});