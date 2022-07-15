console.log("newsale isworking..");
try
{
    document.getElementById("salesDate").value = new Date().toISOString().slice(0,10);
    document.getElementById("quantity").value = 1;
}
catch(e)
{
    console.log(e);
}


var form = document.getElementById("myForm");
function HoldSubmit(e)
{
    e.preventDefault();
    //validation();
}
form.addEventListener('submit',HoldSubmit);

/* -------------------AJAX CALL  HERE------------------------*/  
var dbQuantity=0;
function getsalesdata()
{
    var id = document.getElementById("inputCustomerName").value;
    var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    console.log(id);
    const xhr = new XMLHttpRequest();
    xhr.open("POST","/getProductById/",true);
    xhr.responseType = 'json';
    xhr.onload = function(){
        if(xhr.status == 200)
        {
            //console.log("success");
            data = xhr.response.productDataById;
            //console.log(data);
            document.getElementById("rate").value = data[0].rate;
            document.getElementById("discount").value = data[0].discount;
            document.getElementById("CGST").value = data[0].CGST;
            document.getElementById("IGST").value = data[0].IGST;
            console.log("quantity is:",data[0].quantity);
            dbQuantity = data[0].quantity;
            console.log("dbQuantity is:",dbQuantity);
            void calculateTotal();

        }
        else
        {
            console.log("error");
        }
    };
    mydata = {'id':id}
    //console.log(mydata);
    xhr.setRequestHeader("X-CSRFToken",csrf);
    xhr.setRequestHeader("Content-Type",'application/json;');
    xhr.send(JSON.stringify(mydata));
}



isFormvalid = false;
function validation()
{
    var form = document.getElementById("myForm");
    selectname = form.inputCustomerName.value;
    selectCustName = form.selectCustomerData.value;
    invoice = form.invoice.value;
    rate = form.rate.value;
    quantity = form.quantity.value;
    //total = form.total.value;
    console.log(selectname,invoice,rate,quantity,typeof(quantity),selectCustName);

    var ErrorName = document.getElementById('errorSelectName')
    getId = ErrorName.getAttribute('id');
    if(selectname == "noSelect" || selectname == null)
    {
        setError("inputCustomerName",getId,"select Product Name");
        isFormvalid = false;
        return false;
    }
    else
    {
        setsuccess("inputCustomerName",getId);
    }

    var ErrorName = document.getElementById("errorCustomerdata");
    getId = ErrorName.getAttribute('id');
    if(selectCustName == 'selectCustomerValue')
    {
        setError("selectCustomerData",getId,"Field Required");
        isFormvalid = false;
        return false;
    }
    else
    {
        setsuccess("selectCustomerData",getId);
    }

    var ErrorName = document.getElementById("errorInvoice");
    getId = ErrorName.getAttribute('id');
    if(invoice.length <= 0 || invoice == '')
    {
        setError("invoice",getId,"Required Field");
        isFormvalid = false;
        return false;
    }
    else
    {
        setsuccess("invoice",getId);
    }

    var ErrorName = document.getElementById('errorquantity')
    getId = ErrorName.getAttribute('id');
    if(quantity.length <=0 || quantity == '')
    {
        setError("quantity",getId,"Invalid Rate");
        isFormvalid=false;
        document.getElementById('totalAmount').value = '';
        return false;
    }
    else
    {
        setsuccess("quantity",getId);
        isFormvalid = true;
    }
    

    

}

var isvalid = false;

function calculateTotal()
{
    var totalAmount = 0;
    var finalAmount = 0;
    var totalTax = 0;
    var rate = +document.getElementById('rate').value;
    var quantity = +document.getElementById('quantity').value;
    var discount = +document.getElementById("discount").value;
    var CGST = +document.getElementById("CGST").value;
    var IGST = +document.getElementById("IGST").value;
    //console.log(rate,quantity);

    var ErrorName = document.getElementById('errorquantity')
    getId = ErrorName.getAttribute('id');
    //console.log("in cal funL",quantity,typeof(quantity));
    if(quantity <= 0)
    {
        setError("quantity",getId,"Field Required");
        isFormvalid=false;
        return false;
    }
    console.log("dbQuantity:",dbQuantity)
    if(quantity > dbQuantity)
    {
        setError("quantity",getId,"Out of stock");
        isFormvalid=false;
        return false;
    }
    else
    {
        setsuccess("quantity",getId);
    }

    if((rate>0 && quantity>0))
    {
        totalAmount = Math.ceil(quantity*rate);
        document.getElementById('totalAmount').value = totalAmount;
        isvalid = true;
    }
    else
    {
        //document.getElementById('totalAmount').value = '';
        isvalid = false;
        return false;
    }

    if(discount>0)
    {
       //console.log(discount,typeof(discount))
       discountPrice = 0
       var discountPrice = totalAmount*discount/100;
       var afterDiscount = totalAmount - discountPrice;
       finalAmount = afterDiscount;
       document.getElementById("totalAmount").value = afterDiscount;
    }
    if(CGST>0)
    {
        var afterCGST = 0;
        if(finalAmount>0)
        {
            afterCGST = finalAmount + CGST;
            finalAmount = afterCGST
            document.getElementById("totalAmount").value = afterCGST;  
        }
        else
        {
            afterCGST = totalAmount + CGST;
            totalAmount = afterCGST;
            document.getElementById("totalAmount").value = afterCGST;
        }
    }
    
    if(IGST>0)
    {
        var afterIGST = 0;
        if(finalAmount>0)
        {
            afterIGST = finalAmount + IGST;
            finalAmount = afterIGST;
            document.getElementById("totalAmount").value = afterIGST;  
        }
        else
        {
            afterIGST = totalAmount + IGST;
            totalAmount = afterIGST;
            document.getElementById("totalAmount").value = afterIGST;
        }
    }
    if(CGST>=0 || IGST>=0)
    {
        totalTax = CGST + IGST;
        //console.log(CGST,IGST,totalTax);
        document.getElementById("taxableAmount").value = totalTax;
    }

    
}

function getAvailableQty()
{
    console.log("getAvailableQty....");
    void getsalesdata();

}

function formsubmit()
{
    validation();
    calculateTotal();
    console.log(isvalid,isFormvalid);
    if(isvalid && isFormvalid)
    {
        form.submit();
    }
}

function setError(input,getId,msg)
{
    addclass = document.getElementById(input);
    addclass.className += " " + "errors"
    document.getElementById(getId).innerText = msg; 
}
function setsuccess(input,getId)
{
    addclass = document.getElementById(input);
    addclass.classList.remove("errors");
    document.getElementById(getId).innerText = ''; 
}