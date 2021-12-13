var numberOnlyAmout = (id) => {
    var element = document.getElementById(id);
    element.value = element.value.replace(/[^0-9]/gi, "");
  }


 var numberOnly = (id) => {
   var element = document.getElementById(id);
   element.value = element.value.replace(/[^0-9]/gi, "");
 }