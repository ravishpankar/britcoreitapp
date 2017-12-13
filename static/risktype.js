function RTInputController($scope, $http, $element, $attrs) {
  var ctrl = this;
  ctrl.attrlist = [];
  ctrl.rtname = '';


  ctrl.getrt = function(rtname) {
        $http({
            method : "GET",
            url : "risktype/" + rtname,
            headers : {"Content-Type" : "application/json"}
            }).then(function successCallback(response) {
                    ctrl.attrlist = response.data.rtattributes
                }, function errorCallback(response) {
                    ctrl.attrlist = [];
                    if (response.status == 400) {
                        alert(response.data.message)
                    } else {
                        alert("Error trying to get the risk type. Retry.")
                    }
            });
  };

  if (ctrl.nosearch == 'T' && ctrl.passedname !='') {
    ctrl.getrt(ctrl.passedname);
  }
}

angular.module('risk').component('risktype',{
      bindings : {nosearch : '@', passedname : '<'},
      templateUrl: 'https://bcit-static.s3.amazonaws.com/risktype.htm',
      controller: RTInputController
});