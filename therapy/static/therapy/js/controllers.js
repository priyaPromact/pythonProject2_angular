//var therapyControllers = angular.module('therapyControllers',[]);

therapyApp.controller('ScheduleDetailController',['$scope','$http','$state','$rootScope',
	function($scope, $http, $state,$rootScope) {
	    	$http.get("/therapy/api/schedule").success(function(dataSchedule){
			$http.get("/therapy/api/service/").success(function(dataService){
			$scope.schedules = [];
			for(var d in dataSchedule) {
			   	for(var s in dataService) {
				   if(dataService[s].id==dataSchedule[d].service) {
			   		$scope.schedules.push({'id':dataSchedule[d].id,'service':dataService[s],'date':dataSchedule[d].date});
				   }
				}			
			}
			});
		});
		$scope.editSchedule = function(scheduleId) { 
			$rootScope.scheduleId = scheduleId
			$state.transitionTo('edit');	
		}
		$scope.deleteSchedule = function(scheduleId) {
			$http.delete('/therapy/api/schedule/' + scheduleId).success(function (data, status) {
			    $http.get("/therapy/api/schedule").success(function(dataSchedule){
			    $http.get("/therapy/api/service/").success(function(dataService){
				$scope.schedules = [];
			        for(var d in dataSchedule) {
			       	    for(var s in dataService) {
				       if(dataService[s].id==dataSchedule[d].service) {
				   	 $scope.schedules.push({'id':dataSchedule[d].id,'service':dataService[s],'date':dataSchedule[d].date});
					   }
					}			
				     }
			    });
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
		$http.get("/therapy/api/schedule/" + $rootScope.scheduleId).success(function(data){
	     	    $scope.schedule = data;
		});
		$scope.saveSchedule = function(schedule) {
			$http.put("/therapy/api/schedule/" + schedule.id + "/", schedule).success(function(){});
		}
	}
]); 
