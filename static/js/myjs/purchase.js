console.log("purchase working js");
try
{
var x = document.getElementById("purchaseDate").value = new Date().toISOString().slice(0,10);
document.getElementById("quantity").value = 1;
}
catch(ex)
{
    console.log(ex);
}
var form = document.getElementById('myform');
function HoldSubmit(e)
{
    e.preventDefault();
    //validation();
}
form.addEventListener('submit',HoldSubmit);
//-----------------calculation on page load--------------------------

var newRate = Number(form.rate.value);
var newquantity = Number(form.quantity.value);
var newdiscount = Number(form.discount.value);
var newCGST = Number(form.CGST.value);
var newIGST = Number(form.IGST.value);
if(Boolean(newRate)&&Boolean(newquantity))
{
    void calculateTotalAmount();
    /*
    totalAmt = newRate*newquantity;
    if(Boolean(newdiscount))
    {
        newDiscount = totalAmt*newdiscount/100;
        totalAmt = totalAmt-newDiscount;
    }
    if(Boolean(newCGST))
    {
        totalAmt = totalAmt + newCGST;
    }
    if(Boolean(newIGST))
    {
        totalAmt = totalAmt + newIGST;
    }

    document.getElementById("totalAmount").value = totalAmt;
    */
}
//console.log("onload Rate is:",newRate,typeof(newRate));


//----------------------------validation function()-----------------------

var formvalid = false;

function validation()
{
    //console.log("from value valid is :",Boolean(form.rate.value));
    var noSelect = document.getElementById("inputCustomerName").value;
    var invoice = document.getElementById('invoice').value;
    var rate = document.getElementById('rate').value;
    var customerDataId = document.getElementById("customerDataId").value;
    totalAmount = document.getElementById('totalAmount').value;
    console.log(typeof(noSelect),totalAmount,customerDataId);

    var ErrorName = document.getElementById("errorSelectName");
    var getId = ErrorName.getAttribute('id');
    if(noSelect == "noSelect")
    {
        formvalid = false;
        setError("inputCustomerName",getId,"This field is required");
        return false;
    }
    else
    {
        setSuccess("inputCustomerName",getId);
    }

    var ErrorName = document.getElementById("errorCustomerdata");
    getId = ErrorName.getAttribute('id');
    if(customerDataId == 'noSelect')
    {
        formvalid = false;
        setError('customerDataId',getId,'select customer.');
        return false;
    }
    else
    {
        setSuccess('customerDataId',getId);
    }

    var ErrorName = document.getElementById("errorInvoice");
    var getId = ErrorName.getAttribute('id');
    if(invoice.length <= 2 || invoice == null)
    {
        formvalid = false;
        setError("invoice",getId,"Enter Invoice NO");
        return false;
    }
    else
    {
        formvalid = true;
        setSuccess("invoice",getId);   
    }

    ErrorName = document.getElementById("errorRate");
    getId = ErrorName.getAttribute('id');
    if(rate <= 0 || rate == null)
    {
        isvalid = false;
        setError("rate",getId,"Enter valid Rate");
        //document.getElementById("quantity").value = '';
        document.getElementById("totalAmount").value = '';
        return false;
    }
    else
    {
        setSuccess("rate",getId);
    }

    //isRate = Boolean(form.rate.value);
    //isquantity = Boolean(form.quantity.value);

    

}

var isvalid = false;

function calculateTotalAmount()
{
    var totalAmount;
    var finalAmount = 0;
    var totalTax = 0;
    rate = document.getElementById('rate').value;
    quantity = document.getElementById('quantity').value;
    discount = document.getElementById("discount").value;
    taxableAmount = document.getElementById('taxableAmount').value;
    CGST = document.getElementById("CGST").value;
    IGST = document.getElementById("IGST").value;
    //console.log("discount is:",typeof(discount),discount,"taxableAmount",typeof(taxableAmount),taxableAmount);
    
    ErrorName = document.getElementById("errorRate");
    getId = ErrorName.getAttribute('id');
    if(rate <= 0 || rate == null)
    {
        isvalid = false;
        setError("rate",getId,"Enter valid Rate");
        //document.getElementById("quantity").value = '';
        document.getElementById("totalAmount").value = '';
        return false;
    }
    else
    {
        setSuccess("rate",getId);
    }

    ErrorName = document.getElementById("errorquantity");
    getId = ErrorName.getAttribute('id');
    if(quantity <= 0 || quantity == null)
    {
        isvalid = false;
        setError("quantity",getId,"Enter valid Rate");
        document.getElementById("totalAmount").value = '';
        return false;
    }
    else
    {
        setSuccess("quantity",getId);
    }

    if((rate && quantity))
    {
        total = rate * quantity
        totalAmount = Math.ceil(total)
        document.getElementById("totalAmount").value = totalAmount;
        isvalid = true;
    }
    else
    {
        isvalid = false;
        return false;
    }

    if(discount.length>0)
    {
        discountPrice = 0
        var discountPrice = totalAmount*discount/100;
        var afterDiscount = totalAmount - discountPrice;
        finalAmount = afterDiscount;
        document.getElementById("totalAmount").value = afterDiscount;
    }

    if(CGST.length>0)
    {
        var afterCGST = 0;
        cgst = Number(CGST);
        if(finalAmount>0)
        {
            afterCGST = finalAmount + cgst;
            finalAmount = afterCGST
            document.getElementById("totalAmount").value = afterCGST;    
        }
        else
        {
            //cgst = Number(CGST);
            afterCGST = totalAmount + cgst;
            totalAmount = afterCGST;
            document.getElementById("totalAmount").value = afterCGST;
        }

    }

    if(IGST.length>0)
    {
        var afterIGST = 0
        igst = Number(IGST);
        if(finalAmount>0)
        {
            afterIGST = finalAmount + igst;
            finalAmount = afterCGST
            document.getElementById("totalAmount").value = afterIGST;    
        }
        else
        {
            //igst = Number(IGST);
            afterIGST = totalAmount + igst;
            totalAmount = afterIGST;
            document.getElementById("totalAmount").value = afterIGST;  
        }

    }

    if(CGST.length>=0 || IGST.length>=0)
    {
        cgst = Number(CGST);
        igst = Number(IGST);
        totalTax = igst + cgst;
        document.getElementById("taxableAmount").value = totalTax;
        console.log(totalTax);
    }

}

function setError(input,getId,msg)
{
    var addClassName = document.getElementById(input);
    addClassName.className += " " + 'errors';
    document.getElementById(getId).innerText = msg;
}

function setSuccess(input,getId)
{
    var addClass = document.getElementById(input);
    addClass.classList.remove('errors');
    document.getElementById(getId).innerText = '';
}


function saveform()
{
    void validation();
    void calculateTotalAmount();
    //isRate = Boolean(form.rate.value);
    //isquantity = Boolean(form.quantity.value);
    //console.log(isRate,isquantity);

    console.log("isvalid is:",isvalid,"formvalid is:",formvalid);
    if(isvalid && formvalid) //(totalAmount >0 || totalAmount != null)
    {
        form.submit();
    }

    
}