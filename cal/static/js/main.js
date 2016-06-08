$(document).ready(function(){
	console.log("Hi there!")
    $('.parallax').parallax();

  $('.button-collapse').sideNav({
      edge: 'left', 
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    });

///// User Register /////
    $('#nav').on('click', "#user_register", function(event){
    	event.preventDefault();
        var template = $('#user_register-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#user_register_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "user_register",
        data: query_string,
    }).done(function(data, status){

		if (data.success){
			////// if they registered then display the Login ////////
                var template = $('#user_login-template').html();
		        var renderM = Mustache.render(template);
		        $('#answer_div').html(renderM);
            }
        });
    });


///// Org Register /////
    $('#nav').on('click', "#org_register", function(event){
        event.preventDefault();
        var template = $('#org_register-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#org_register_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "org_register",
        data: query_string,
    }).done(function(data, status){

        if (data.success){
            ////// if they registered then display the Login ////////
                var template = $('#org_login-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);
            }
        });
    });



///// User Login /////
    $('#nav').on('click', "#user_login", function(event){
    	event.preventDefault();
        var template = $('#user_login-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#user_login_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "user_login",
        data: query_string,
    }).done(function(data, status){

          if (data.success){
          ////// if they login correctly ////////
            console.log("HERE")
            document.location.href="/";
            window.scrollTo(0, 0);
        	} 
    	});
    });


///// Org Login /////
    $('#nav').on('click', "#org_login", function(event){
        event.preventDefault();
        var template = $('#org_login-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#org_login_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "org_login",
        data: query_string,
    }).done(function(data, status){

          if (data.success){
          ////// if they login correctly ////////
            console.log("HERE")
            document.location.href="/";
            window.scrollTo(0, 0);
            } 
        });
    });


///// Logout /////
    $('#nav').on('click', "#logout", function(event){
    event.preventDefault();

    $.ajax({
        method: "POST",
        url: "logout",
        // data: query_string,
    }).done(function(data, status){

	location.reload();
    });
});

///// About /////
    $('#nav').on('click', "#about", function(event){
        event.preventDefault();
        var template = $('#about-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });







});