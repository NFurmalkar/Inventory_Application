console.log("customer");
var myForm = document.getElementById("form");
function holdsubmit(e)
{
    e.preventDefault();
    validation();
}

myForm.addEventListener('submit',holdsubmit);

function validation()
{
     isValidForm = false;
     customerName = document.getElementById("customerName").value;
     address = document.getElementById("address").value;
     mobileNumber = document.getElementById("mobileNumber").value;
     gstno = document.getElementById("gstno").value;
     console.log(customerName.length,address,mobileNumber,gstno);

     var ErrorName = document.getElementById("errorCustomerName");
     var getId = ErrorName.getAttribute('id'); 
     if(customerName.length <= 2 || customerName == null)
     {
        isValidForm = false;
         setError("customerName",getId,'Name Required 3 char');
         return false;
     }
     else
     {
        isValidForm = true;
        setSuccess("customerName",getId);
     }

     ErrorName = document.getElementById("errorMobileNumber");
     getId = ErrorName.getAttribute('id');
     
     if(mobileNumber.length > 0)
     {
         list=["0","1","2","3","4","5"]
         firstDigit = mobileNumber.charAt(0);
         isvalid = list.includes(firstDigit);
         if(isvalid)
         {
            isValidForm = false;
            setError("mobileNumber",getId,'Invalid Customer');
            return false;
         }
         else
         {
            isValidForm = true;
             setSuccess("mobileNumber",getId);
         }
     }
     if(mobileNumber.length == 0)
     {
        setSuccess("mobileNumber",getId);
     }

     //alert(isValidForm);
     //console.log(isValidForm);
     if(isValidForm)
     {
         myForm.submit();
     }
}

function setError(input,getId,msg)
{
    var addClass = document.getElementById(input);
    addClass.className += " " + 'errors';
    document.getElementById(getId).innerText = msg;
}
function setSuccess(input,getId)
{
    var addClass = document.getElementById(input);
    addClass.classList.remove('errors');
    document.getElementById(getId).innerText =''
}


function onsave()
{
    validation();
    alert(isValidForm);
}



