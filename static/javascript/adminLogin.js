$(document).ready(function(){
    $('#login').click(function(){
      var username = $('#username').val();
      var password = $('#password').val();
      if (username != 'admin' || password != 'admin'){
        alert('Wrong username or password! Please try again')
      }
    })
  })