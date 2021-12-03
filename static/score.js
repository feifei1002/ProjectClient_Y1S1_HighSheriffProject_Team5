function checkAnswer(){
  var ques1 = document.getElementsByName('1');
  var len1 = ques1.length;
  var score = 0;

  if(ques1[1].checked==true){
    score++;
  }
  var ques2 = document.getElementsByName('2');
  var len2 = ques2.length;

  if(ques2[0].checked==true){
    score++;
  }
  var ques3 = document.getElementsByName('3');
  var len3 = ques3.length;

  if(ques3[0].checked==true){
    score++;
  }
  var ques4 = document.getElementsByName('4');
  var len4 = ques4.length;

  if(ques4[1].checked==true){
    score++;
  }
  $('#score').attr("value", score)
}
