
/* init Jarallax */
        jarallax(document.querySelectorAll('.jarallax'));


//----------- Login-----------
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

  //****************** Input Date ********** 
  $( function() {
    $( ".datepicker" ).datepicker();
  } );

 
          // ************* Function close Page **************
      
      function ClosePage(){
        document.getElementById('idstyleDvDetail').style.display='none';
        document.getElementById('dvslider').style.display='none';
         document.getElementById('dvgrid1').style.visibility='visible';
         document.getElementById('dvgrid2').style.visibility='visible';
     }

  // ************* Function Show Detail **************
  function showDetailPlan(id){
         document.getElementById('idstyleDvDetail').style.display='block';
         document.getElementById('dvslider').style.display='block';
         var val1=document.getElementById(id);
         var y = val1.getElementsByTagName("span");
         document.getElementById('NameAct').innerHTML=y[0].innerText;
         document.getElementById('dvgrid1').style.visibility='hidden';
       }
       function showDetailActivitie2(id){
         document.getElementById('idstyleDvDetail').style.display='block';
         document.getElementById('dvslider').style.display='block';
         var val2=document.getElementById(id);
         document.getElementById('NameAct').innerHTML=val2.innerText;
         document.getElementById('dvgrid2').style.visibility='hidden';
       }

//  ******************* Function Add Prix **********
function addPrix(id) {
 x= document.getElementById(id).innerText;
 y= document.getElementById("prix").innerText;
 z=parseInt(y);

 
   if(x =="+"){
  document.getElementById(id).innerHTML="-";
  document.getElementById("prix").innerHTML=z+100;
   }else{
     document.getElementById(id).innerHTML="+";
  document.getElementById("prix").innerHTML=z-100;
   }

}
            
function showBag() {
  var idBag=document.getElementById("IdFormShop");
   if(idBag.style.display==="none"){
    idBag.style.display = "block";
    }else{
    idBag.style.display = "none";
  }
  }




// *************** Form Login *************** 
        function showModale(){  
         document.getElementById("IdFormShop").style.display = "none";
          var valueUser = document.getElementById("ltr1");
          if(valueUser.innerText=="Login"){
         document.getElementById("id01").style.display="block";
          }else{
            showProfiel();
          }
        }
//****** Function button Login **********

document.getElementById("IdLogin").addEventListener("click", function() {
  var valInpt1 = document.getElementById("inptTxtUser").value;
  var valInpt2 = document.getElementById("inptPwUser").value;
  if (valInpt1!="" && valInpt2!=""){
    myFctBtnLog();
  }else{
    document.getElementById("SpanErreur1").style.visibility = "visible";
    document.getElementById("SpanErreur2").style.visibility = "visible";
  }
});

//******** Function Form Profiel Custemer ************
function myFctBtnLog() {
  document.getElementById("id01").style.display="none";
  document.getElementById("iconuser").style.display="inline";
  var str1 = document.getElementById("inptTxtUser").value;
  var res1 = str1.slice(0,4);  
  document.getElementById("ltr1").innerHTML = res1; 
}
//*************** Form Button  Profile *********** 
function showProfiel() {
var idall=document.getElementById("idAllsContent");
 if(idall.style.display==="none"){
  idall.style.display = "block";
  }else{
  idall.style.display = "none";
}
}



//*************** Function Form Login ************

          //********** Button Login **************
      function showFrmReg(){
        document.getElementById("tab1").style.display="none";
        document.getElementById("tab2").style.display="none";
        document.getElementById("tab3").style.display="block";
      }
      function FncBtnLogin(){
        document.getElementById("tab1").style.display="block";
        document.getElementById("tab2").style.display="none";
        document.getElementById("tab3").style.display="none";
      }
      document.getElementById("btnLog").addEventListener("click",FncBtnLogin);
      document.getElementById("BtnBack").addEventListener("click",FncBtnLogin);

      document.getElementById("btnReg").addEventListener("click",function(){
        document.getElementById("tab1").style.display="none";
        document.getElementById("tab2").style.display="block";
        document.getElementById("tab3").style.display="none";
      });
//**********End Button Login **************
         
          

//******** Evente Enter In inputs *******
var idcon= document.getElementById("contform1");
var myInputs = idcon.getElementsByTagName("input");
    var p;
    for (p = 0; p < myInputs.length; p++) {
      
      myInputs[p].addEventListener("keyup", function(event) {
    event.preventDefault()
    if (event.keyCode === 13){
      document.getElementById("btn1").click();         
      }
});
}
                 
          //******** Function scroll *******
              if (window.matchMedia("(max-width: 600px)").matches) {
    window.onscroll = function() {myFunction()};

  function myFunction() {
     if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
      document.getElementById("contform1").style.display = "none";
     $(".menu2 > li a").css("color", "#f4f4f4");
   }
  }
    }




    
//********** Button Like **********/
function BtnLike(elmnt) {
  if(elmnt.style.background == "white")
  {
    elmnt.style.background="red";
    elmnt.style.color="white";
  }else{
    elmnt.style.background="white";
    elmnt.style.color="red"; 
  }
  }


$(document).ready(function(){
      $(".menu1 > li:not(.lien6,.lien5) a").click(function(){
      $(".menu1 > li:not(.lien6,.lien5) a").css("color", "black");
        $(this).css("color", "#f8d001"); 
      });
      });
      $(document).ready(function(){
        $(".menu2 > li a").click(function(){
        $(".menu2 > li a").css("color", "#f4f4f4");
          $(this).css("color", "#f8d001"); 
        });
        });


//    Lien 1 
$(document).ready(function(){
    $("#l1").click(function(event){
      event.preventDefault();
      document.getElementById("idFormInputQui").style.display="none";
      $(".container").css("width", "67%");
      $(".divtable").css("display", "none");
      $("#lblerreur").css("display", "none");
        $("#contform1").css("display", "flex");
        $("#input1").css("display", "flex");
        $("#input2").css("display", "flex");
        $("#input3").css("display", "flex");
        $("#input4").css("display", "flex");
        $("#input2").css("border-right", "1px solid #a8a383");
        $(".flex-container").css("flex", "100%");
    });
  });
  $(document).ready(function(){
    $("#l2").click(function(event){
      event.preventDefault();
      document.getElementById("idFormInputQui").style.display="none";
      $(".container").css("width", "67%");
      $(".divtable").css("display", "none");
      $(".flex-container3").css("display", "none");
      $("#frmTrip").css("display", "block");
      $("#lblerreur").css("display", "none");
        $("#contform1").css("display", "flex");
        $("#input1").css("display", "flex");
        $("#input3").css("display", "flex");
        $("#input4").css("display", "flex");
        $("#input2").css("display", "none");
        $(".flex-container").css("flex", "100%");
    });
  });
//    Lien 2 
  $(document).ready(function(){
    $("#l3,#l4").click(function(event){
      event.preventDefault();
      document.getElementById("idFormInputQui").style.display="none";
      $("#lblerreur").css("display", "none");
      $(".container").css("width", "35%");
      $(".divtable").css("display", "none");
      $("#contform1").css("display", "flex");
        $("#input1").css("display", "none");
        $("#input3").css("display", "none");
        $("#input4").css("display", "none");
        $("#input2").css("display", "flex");
        $("#input2").css("border-right", "none");
    });
  });

  function reset() {
    var myCollection = document.getElementsByTagName("input");
    var i;
    for (i = 0; i < myCollection.length; i++) {
      myCollection[i].value = "";
    }
  }

  // //********/  Function paege index Button serach in input 
  function myshow(id){
    var txt1=document.getElementById("input1").value;
    var txt2=document.getElementById("input2").value;
    var txt3=document.getElementById("input3").value;
    var txt4=document.getElementById("input4").value;
          
    var idFrm =document.getElementById("frm");
    var idfrmauto =document.getElementById("frmauto");
    var idFfrmTrip =document.getElementById("frmTrip");
    var idlblerreur=document.getElementById("lblerreur");
    var idinput=document.getElementById("idFormInputQui");
    if(idinput.style.display=="block"){
      idinput.style.display="none";
    }

    if(id=="btn1" && document.getElementById("input1").style.display!="none"&& document.getElementById("input2").style.display!="none"){
      if(txt1!='' && txt2!='' && txt3!='' && txt4!=''){
        if (window.matchMedia("(max-width: 601px)").matches){
          document.getElementById("contform1").style.display="none";
        }
        idFrm.style.display="block";
        idfrmauto.style.display="block";
        idFfrmTrip.style.display="none";
        idlblerreur.style.display="none";
      }else
        {
        idlblerreur.style.display="block";
      }
    }else if(document.getElementById("link2").style.color=="rgb(248, 208, 1)" || document.getElementById("l2").style.color=="rgb(248, 208, 1)"){
      if(txt1!=''&& txt3!='' && txt4!=''){
        if (window.matchMedia("(max-width: 601px)").matches){
          document.getElementById("contform1").style.display="none";
        }
        idFrm.style.display="block";
        idfrmauto.style.display="none";
        idFfrmTrip.style.display="block";
        idlblerreur.style.display="none";
      }else
        {
        idlblerreur.style.display="block";
      }

    }else if(document.getElementById("link3").style.color=="rgb(248, 208, 1)" || document.getElementById("l3").style.color=="rgb(248, 208, 1)"){
      if(txt2!=''){
        idlblerreur.style.display="none";
        window.location="pageThree.html?text2="+document.getElementById("input2").value;
      }else
        {
        idlblerreur.style.display="block";
      }
    }else if(document.getElementById("link4").style.color=="rgb(248, 208, 1)" || document.getElementById("l4").style.color=="rgb(248, 208, 1)"){
      if(txt2!=''){
       idlblerreur.style.display="none";
        window.location="pageThree.html?text2="+document.getElementById("input2").value;
      }else
        {
        idlblerreur.style.display="block";
      }
    }else{
      return;
    }
  }

  


  $(document).ready(function(){
    $("#link1").click(function(){
      $("#input1").show();
      $("#input2").show();
      $("#input3").show();
      $("#input4").show();
      $("#contform1").toggle();
      $("#frm").hide();
      $("#idFormInputQui").hide();
    });
  });
  $(document).ready(function(){
    $("#link2").click(function(){
      $("#input1").show();
      $("#input3").show();
      $("#input2").hide();
      $("#input4").show();
      $("#contform1").toggle();
      $("#frm").hide();
      $("#idFormInputQui").hide();
    });
  });
  $(document).ready(function(){
    $("#link3").click(function(){
      $("#contform1").toggle();
      $("#frm").hide();
      $("#idFormInputQui").hide();
      $("#input1").hide();
      $("#input3").hide();
      $("#input4").hide();
      $("#input2").show();
    });
  });
  $(document).ready(function(){
    $("#link4").click(function(){
      $("#contform1").toggle();
      $("#frm").hide();
      $("#idFormInputQui").hide();
      $("#input1").hide();
      $("#input3").hide();
      $("#input4").hide();
      $("#input2").show();
    });
  });

  //***************** Function input qui ***********
document.getElementById("input4").addEventListener("click",function(){
  var idinput=document.getElementById("idFormInputQui");
  var idRest=document.getElementById("frm");
  if(idinput.style.display==="none"||idRest.style.display=="none"){
    if (window.matchMedia("(max-width: 601px)").matches){
    document.getElementById("contform1").style.display = "none";
    }
    idRest.style.display = "none";
    idinput.style.display = "block";
   }else{
    idinput.style.display = "none";
 }
});
$(document).ready(function(){
  $("#input1").click(function(){
    $("#idFormInputQui").hide();
  });
  $("#input2").click(function(){
    $("#idFormInputQui").hide();
  });
  $("#input3").click(function(){
    $("#idFormInputQui").hide();
  });
});

$(document).ready(function(){
  $("#iconDown").click(function(){
    $("#idFormInputQui").css("display", "none");
    $("#contform1").css("display", "flex");
  });

});

//************* Function Button Plus Minus Input Qui   */

var valinput1 =document.getElementById('demoInput1');
var valinput2 =document.getElementById('demoInput2');
var valinput3 =document.getElementById('demoInput3');
var valinput4 =document.getElementById('demoInput4');


function increment1(num) {
  var value1=parseInt(valinput1.value);
  var value2=parseInt(valinput2.value);
  var value3=parseInt(valinput3.value);
  var value4=parseInt(valinput4.value);
  var total=value1+value2+value3+value4+1;
  document.getElementById('demoInput1').stepUp();
  if(num===1){
    document.getElementById('input4').value =total+"Voyageurs";
  }else{
    document.getElementById('inputCmd4').value =total+"Voyageurs";
  }
}
function decrement1(num) {
  var value1=parseInt(valinput1.value);
  var value2=parseInt(valinput2.value);
  var value3=parseInt(valinput3.value);
  var value4=parseInt(valinput4.value);
  var total=value1+value2+value3+value4-1;
  document.getElementById('demoInput1').stepDown();
  if(num===1){
    if(total>0){
      document.getElementById('input4').value =total+"Voyageurs";
    }else{
      document.getElementById('input4').value =""; 
    }
  }else{
    if(total>0){
    document.getElementById('inputCmd4').value =total+"Voyageurs";      
    }else{
      document.getElementById('inputCmd4').value =""; 
    }
   }
}
  function increment2(num) {
    var value1=parseInt(valinput1.value);
    var value2=parseInt(valinput2.value);
    var value3=parseInt(valinput3.value);
    var value4=parseInt(valinput4.value);
    var total=value1+value2+value3+value4+1;
  document.getElementById('demoInput2').stepUp();
  if(num===1){
    document.getElementById('input4').value =total+"Voyageurs";
  }else{
    document.getElementById('inputCmd4').value =total+"Voyageurs";
  }
}
function decrement2(num) {
  var value1=parseInt(valinput1.value);
  var value2=parseInt(valinput2.value);
  var value3=parseInt(valinput3.value);
  var value4=parseInt(valinput4.value);
  var total=value1+value2+value3+value4-1;
  document.getElementById('demoInput2').stepDown();
  if(num===1){
    if(total>0){
      document.getElementById('input4').value =total+"Voyageurs";
    }else{
      document.getElementById('input4').value =""; 
    }
  }else{
    if(total>0){
    document.getElementById('inputCmd4').value =total+"Voyageurs";      
    }else{
      document.getElementById('inputCmd4').value =""; 
    }
   }
}
  function increment3(num) {
    var value1=parseInt(valinput1.value);
    var value2=parseInt(valinput2.value);
    var value3=parseInt(valinput3.value);
    var value4=parseInt(valinput4.value);
    var total=value1+value2+value3+value4+1;
  document.getElementById('demoInput3').stepUp();
  if(num===1){
    document.getElementById('input4').value =total+"Voyageurs";
  }else{
    document.getElementById('inputCmd4').value =total+"Voyageurs";
  }
}
function decrement3(num){
  var value1=parseInt(valinput1.value);
  var value2=parseInt(valinput2.value);
  var value3=parseInt(valinput3.value);
  var value4=parseInt(valinput4.value);
  var total=value1+value2+value3+value4-1;
  document.getElementById('demoInput3').stepDown();
  if(num===1){
    if(total>0){
      document.getElementById('input4').value =total+"Voyageurs";
    }else{
      document.getElementById('input4').value =""; 
    }
  }else{
    if(total>0){
    document.getElementById('inputCmd4').value =total+"Voyageurs";      
    }else{
      document.getElementById('inputCmd4').value =""; 
    }
   }
}
  function increment4(num) {
    var value1=parseInt(valinput1.value);
    var value2=parseInt(valinput2.value);
    var value3=parseInt(valinput3.value);
    var value4=parseInt(valinput4.value);
    var total=value1+value2+value3+value4+1;
  document.getElementById('demoInput4').stepUp();
  if(num===1){
    document.getElementById('input4').value =total+"Voyageurs";
  }else{
    document.getElementById('inputCmd4').value =total+"Voyageurs";
  }
}
function decrement4(num){
  var value1=parseInt(valinput1.value);
  var value2=parseInt(valinput2.value);
  var value3=parseInt(valinput3.value);
  var value4=parseInt(valinput4.value);
  var total=value1+value2+value3+value4-1;
  document.getElementById('demoInput4').stepDown();
  if(num===1){
    if(total>0){
      document.getElementById('input4').value =total+"Voyageurs";
    }else{
      document.getElementById('input4').value =""; 
    }
  }else{
    if(total>0){
    document.getElementById('inputCmd4').value =total+"Voyageurs";
    }else{
      document.getElementById('inputCmd4').value =""; 
    }
   }
}

// *********** Function Input Quand DateTRangePicker*******

$(function() {

  $('input[name="datefilter"]').daterangepicker({
      autoUpdateInput: false,
      opens:"left",
      autoApply:true
  });

  $('input[name="datefilter"]').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('MM/DD/YYYY') + ' - ' + picker.endDate.format('MM/DD/YYYY'));
  });
});



