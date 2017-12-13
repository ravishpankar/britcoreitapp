angular.module('risk').component('enum',{
      templateUrl: 'https://bcit-static.s3.amazonaws.com/enum.htm',
      bindings : {et : '='},
      controller: function(){
        var ctrl = this
        ctrl.et.push({een : '', eev : ''})

        ctrl.addenumentry = function () {
            ctrl.et.push({een : '', eev : ''})
        };
      }
  });