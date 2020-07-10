
var form = document.getElementById("form");
 form.addEventListener( "submit", (e)=> userReg(e))



function userReg(e)
{  
var uname = document.getElementById("name");
var cnumber = document.getElementById("number");
var cnumberxx=document.getElementById("number").value;
var mail = document.getElementById("email");
mailxx =document.getElementById("email").value;
var mailx = /^([a-z 0-9\.-]+)@([a-z 0-9]+).([a-z]{2,8})(.[a-z]{2,8})?$/;
var cnumberx =/^[0][7]\d{8}$/;
var qury = document.getElementById("memo");

if (uname.value.trim() =="")
{
     e.preventDefault();
alert("Name cannot be blank");
uname.style.border="solid 3px red";
document.getElementById("lbluser1").style.visibility = "visible";
return false;  
}
// validating contact and displaying error message
else if(cnumber.value.trim() =="")
{ e.preventDefault();
alert("Contact number cannnot be blank");
cnumber.style.border = "solid 3px red ";
document.getElementById("lbluser3").style.visibility = "visible";
return false;
}
else if(cnumberx.test(cnumberxx) == false)
{ e.preventDefault();
    alert("Incorrect contact number format eg 079999999999");
    cnumber.style.border = "solid 3px red ";
    document.getElementById("lbluser3").style.visibility = "visible";
    return false;
}


// validating email textbox and displaying error msg
else if( email.value.trim() == "")
{ e.preventDefault();
alert("email cannot be blank");
mail.style.border="solid 3px red";
document.getElementById("lbluser2").style.visibility = "visible";
return false;
}
else if(mailx.test(mailxx) == false)
{ e.preventDefault();
  alert("Incorrect email format example tinashehove@gmail.com"); 
  mail.style.border="solid 3px red";
document.getElementById("lbluser2").style.visibility = "visible";
  return false;

}
else if(qury.value.trim() =="")
{ e.preventDefault();
alert("Please add your quiry");
qury.style.border="solid 3px red";
document.getElementById("lbluser4").style.visibility = "visible";
return false;
}

}