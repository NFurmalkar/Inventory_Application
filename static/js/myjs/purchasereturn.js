console.log("purchasereturn working");

setTimeout(timer,10000)
function timer()
{
    var btn = document.getElementById("btn");
    try{
        btn.click();
    }
    catch(e){ console.log();}
   
}

try{
    var id = document.getElementById("inputProductName").value;
    document.getElementById("preturnDate").value = new Date().toISOString().slice(0,10);

    console.log("id is--->",id);
    if(Boolean(id)){
        void getdata();
    }
}
catch(e)
{ }

var dbQuantity = 0;
var totalAmt = 0;
function getdata()
{
    var id = document.getElementById("inputProductName").value;
    var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    //console.log(invoice,csrf);
    const xhr = new XMLHttpRequest();
    xhr.open("POST","/getProductById/",true);
    xhr.responseType = "json";
    xhr.onload = function(){
    if(xhr.status == 200)
    {
        console.log(xhr.response.productDataById);
        data = xhr.response.productDataById;
        document.getElementById("invoiceNo").value = data[0].invoice;
        //document.getElementById("rate").value = data[0].rate;
        document.getElementById("quantity").value = data[0].quantity;
        dbQuantity = data[0].quantity;
        //document.getElementById("discount").value = data[0].discount;
        //document.getElementById("CGST").value = data[0].CGST;
        //document.getElementById("IGST").value = data[0].IGST;
        //document.getElementById("taxableAmount").value = data[0].taxableAmount;
        //document.getElementById("totalAmount").value = data[0].totalAmount;
        totalAmt = data[0].totalAmount;

        if(dbQuantity == 0)
        {
            var setQty = document.getElementById("quantity");
            setQty.className += " " + "errors";

            var setUserQty = document.getElementById("returnQuantity");
            setUserQty.setAttribute('readonly',true);
           
            var btnVal = document.getElementById("submitId");
            btnVal.setAttribute('disabled',true);
        }
        else
        {
            var setQty = document.getElementById("quantity");
            setQty.classList.remove('errors');
            var setUserQty = document.getElementById("returnQuantity");
            setUserQty.removeAttribute('readonly');

            var btnVal = document.getElementById("submitId");
            btnVal.removeAttribute('disabled');
        }

    }
    else
    {
        console.log("error");
    }

    };
    myData = {'id':id}
    xhr.setRequestHeader("X-CSRFToken",csrf);
    xhr.setRequestHeader("Content-Type",'application/json;');
    xhr.send(JSON.stringify(myData));

}

isFormValids = false;
function calculate()
{
    console.log("dbQuantity--->",dbQuantity);
    //var discountVal = 0;
    //var afterDiscount = 0;
    //var finalAmt = 0;
    //var price =0;
    //var totalAmount =0
    var qty = +document.getElementById("returnQuantity").value;
    //var rate = +document.getElementById("rate").value;
    //var discount = +document.getElementById("discount").value;
    //console.log("qty is:",qty,typeof(qty),typeof(dbQuantity));
    var ErrorName = document.getElementById("errorquantity");
    getId = ErrorName.getAttribute('id');
    if(qty == 0 || qty == '' ||qty == null)
    {
        void setError("returnQuantity",getId,"Required Field");
        isFormValids = false;
        return false;
    }
    else
    {
        setSuccess("returnQuantity",getId);
        isFormValids = true;
    }

    if(qty > dbQuantity )
    {
        alert("Your Quantity is greater than Your actual Quantity");
        document.getElementById("returnQuantity").value = '';
        isFormValids = false;
        return false;
    }
    else
    {
        setSuccess("returnQuantity",getId);
        isFormValids = true;
    }
    // else
    // {
    //     price = rate*qty;
    //     discountVal = Math.ceil(discount/100*price);
    //     afterDiscount = price - discountVal;
    //     console.log(price,discountVal,afterDiscount,totalAmt);

    //     finalAmt = totalAmt - afterDiscount;
    //     document.getElementById("totalAmount").value = finalAmt;
    //     //console.log("price:",price ,"discountVal: ",discountVal,"afterDiscount:",afterDiscount ,"finalAmt:",finalAmt);
    // }
}

function saveform()
{
    var uQty = document.getElementById("returnQuantity").value;
    var ErrorName = document.getElementById("errorquantity");
    getId = ErrorName.getAttribute('id');
    if(uQty ==''||uQty== null)
    {
        void setError('returnQuantity',getId,'Required Field');
        isFormValids=false;
        return false;
    }
    else
    {
        setSuccess('returnQuantity',getId);
        isFormValids=true;
    }
    console.log("isFormValids",isFormValids);
    if(isFormValids)
    {
        var myForm = document.getElementById("myForm");
        myForm.submit();
    }           
}

function setError(input,getId,msg)
{
    addclass = document.getElementById(input);
    addclass.className += " " + "errors"
    document.getElementById(getId).innerText = msg; 
}

function setSuccess(input,getId)
{
    addclass = document.getElementById(input);
    addclass.classList.remove("errors");
    document.getElementById(getId).innerText = ''; 
}

