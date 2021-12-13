$(document).ready(function(){
    // the add question form will not appear unless the moderator clicked the button
    $('#list').show();
    $('#addForm').hide();
    $('#btnAdd').click(function(){
      $('#addForm').toggle()
    });
    // the delete question form will not appear unless the moderator clicked the button
    $('#deleteForm').hide();
    $('#btnDelete').click(function(){
      $('#deleteForm').toggle()
    });
  })