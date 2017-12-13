function RTCreateController($scope, $http, $element, $attrs) {
  var ctrl = this;
  this.rtname = ''

  ctrl.attrlist = [{'rtaname' : '', 'rtatype' : ''}];

  ctrl.addattr = function() {
        ctrl.attrlist.push({'rtaname' : '', 'rtatype' : ''})
  };

  ctrl.creatert = function() {
        for (i=0; i < ctrl.attrlist.length; i++) {
           if (ctrl.attrlist[i].rtatype == 'enum') {
                ctrl.attrlist[i].enum ={};
                for (j=0; j < ctrl.attrlist[i].et.length; j++) {
                    if (ctrl.attrlist[i].et[j].een != '') {
                        ctrl.attrlist[i].enum[ctrl.attrlist[i].et[j].een] = ctrl.attrlist[i].et[j].eev;
                    }
                }
                delete Object.getPrototypeOf(ctrl.attrlist[i]).et;
           }
        }
        rt = {"rtname" : this.rtname, "rtattributes" : ctrl.attrlist}
        $http({
            method : "POST",
            url : "risktype",
            data : rt,
            headers : {"Content-Type" : "application/json"}
            }).then(function successCallback(response) {
                alert("Successfully created")
                ctrl.attrlist = [{'rtaname' : '', 'rtatype' : ''}]
                ctrl.rtname = ''
            }, function errorCallback(response) {
                if (response.status == 400) {
                    alert(response.data.message)
                } else {
                    alert("Error trying to create the risk type. Retry.")
                }
            });
  };
}

angular.module('risk').component('create',{
      templateUrl: 'https://bcit-static.s3.amazonaws.com/create.htm',
      controller: RTCreateController
});