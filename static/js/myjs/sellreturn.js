console.log("sellreturn.js working..");
var form = document.getElementById("myForm");
// function HoldSubmit(e)
// {
//     e.preventDefault();
// }
// form.addEventListener('submit',HoldSubmit);
setTimeout(timer,10000);
function timer()
{
    try
    {
        var btn = document.getElementById("btn");
        btn.click();
    }
    catch(e){console.log(e);}    
}

try
{
    document.getElementById("sellreturnDate").value = new Date().toISOString().slice(0,10);
}
catch(e){console.log(e);}

var isFormValid1 = false;
function validation()
{
    var quantity = +document.getElementById("quantity").value;
    var returnQuantity = +document.getElementById("returnQuantity").value;
    console.log("quantity is",quantity,'returnQuantity',returnQuantity);

    var ErrorName = document.getElementById("errorreturnQuantity");
    var getId = ErrorName.getAttribute('id');
    

}
var isFormValid2 = false;
function checkQty()
{
    var quantity = +document.getElementById("quantity").value;
    var returnQuantity = +document.getElementById("returnQuantity").value;
    console.log("checkQty is",quantity,'returnQuantity',returnQuantity);

    var ErrorName = document.getElementById("errorreturnQuantity");
    var getId = ErrorName.getAttribute('id');
    if(returnQuantity==""||returnQuantity==0||returnQuantity==null)
    {
        setError('returnQuantity',getId,'Required Field');
        isFormValid2=false;
        return false;
    }
    else 
    {
        setSuccess('returnQuantity',getId);
        isFormValid2=true;
    }

    if(returnQuantity>quantity)
    {
        setError('returnQuantity',getId,'Invalid Field');
        isFormValid2=false;
        return false;
    }
    else 
    {
        setSuccess('returnQuantity',getId);
        isFormValid2=true;
    }
}
function saveform()
{
    void checkQty();
    console.log("isFormValid2-->",isFormValid2)
    if(isFormValid2)
    {
        myForm.submit();
    }

}

function setError(input,getId,msg)
{
    var addclass = document.getElementById(input);
    addclass.className +=" " + "errors";
    document.getElementById(getId).innerText = msg;
}
function setSuccess(input,getId)
{
    addclass = document.getElementById(input);
    addclass.classList.remove("errors");
    document.getElementById(getId).innerText = ''; 
}
