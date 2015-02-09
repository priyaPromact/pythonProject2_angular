var therapyApp = angular.module('therapyApp',['ui.router']);

therapyApp.config(function($stateProvider ) {
    $stateProvider
	.state('home', {
	     url: '/',
	     templateUrl :'/static/therapy/js/partials/schedule_detail.html',
	     controller: 'ScheduleDetailController'
	});
    $stateProvider
	.state('edit', {
	     url: '/edit_schedule/',
	     templateUrl :'/static/therapy/js/partials/add_schedule.html',
	     controller: 'ScheduleEditController'
	});
		
});

therapyApp.config(['$httpProvider',
     function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
     }
]);
