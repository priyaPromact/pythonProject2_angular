//var therapyControllers = angular.module('therapyControllers',[]);

therapyApp.controller('ScheduleDetailController',['$scope','$http','$state','$rootScope',
	function($scope, $http, $state, $rootScope) {
	    	$http.get("/therapy/api/schedule").success(function(data){
			$scope.schedules = data;
		});
		$scope.editSchedule = function(schedule) {
			$rootScope.schedule=schedule;
			$state.transitionTo('edit');	
		}
		$scope.deleteSchedule = function(schedule) {
			$http.delete('/therapy/api/schedule/' + schedule.id).success(function (data, status) {
			    $http.get("/therapy/api/schedule").success(function(data){
				$scope.schedules = data;
			    });
			});		
		}
	}
]);

therapyApp.controller('ScheduleEditController',['$scope','$http','$stateParams','$rootScope',
	function($scope,$http,$stateParams,$rootScope) {
		$http.get("/therapy/api/service/").success(function(data){
	     	    $scope.services = data;
		});
	  	$scope.schedule = $rootScope.schedule;
		$scope.saveSchedule = function(schedule) {
			$http.get("/therapy/api/service/" + schedule.service.id).success(function(data){ console.log(data);
		     	    $scope.service = data;
			    $scope.scheduleData = [];
			    $scope.scheduleData.push({'id' : schedule.id, 'service' : $scope.service, 'date': schedule.date});
			    $http.put("/therapy/api/schedule/" + schedule.id + "/", schedule).success(function(){});
			});
			
		}
	}
]); 
