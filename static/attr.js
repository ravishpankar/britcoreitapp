angular.module('risk').component('attr',{
      templateUrl: 'https://bcit-static.s3.amazonaws.com/attr.htm',
      bindings : {attr : '='},
      controller: function(){
            var ctrl = this
            ctrl.attr.et = [];
      }
  });