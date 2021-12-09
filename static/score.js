function checkAnswer(){
  var ques1 = document.getElementsByName('1');
  var score = 0;

  if(ques1[1].checked==true){
    score++;
  }
  var ques2 = document.getElementsByName('2');

  if(ques2[0].checked==true){
    score++;
  }
  var ques3 = document.getElementsByName('3');

  if(ques3[0].checked==true){
    score++;
  }
  var ques4 = document.getElementsByName('4');

  if(ques4[1].checked==true){
    score++;
  }
  $('#score').attr("value", score)
}
