$(document).ready(function () {
    $('#loginButton').on("click", function(){
        showLogin()
    })

    $('.editAddressButton').on("click", function(){
        showNewAddressForm($(this).attr('id'))
    })

    $('#addAddressButton').on("click", function(){
        showNewAddressForm()
    })
})


function showLogin(){
    $.ajax({
        url: "/login/",
        type: 'GET',
        success: function (data) {
            document.getElementById("loginPopup").innerHTML = data;
        },
        error: function () {
            alert("Error with login");
        }
    });
}

function showNewAddressForm(address_id){
    url = "/add-address/"
    if(address_id){
        url = "/edit-address/" + address_id + "/"
    }
    $.ajax({
        url: url,
        type: 'GET',
        success: function (data) {
            document.getElementById("newAddressForm").innerHTML = data;
        },
        error: function () {
            alert("Error adding the address");
        }
    });
}
function showNewValorationForm(valoration_id){
    url = "/add-rating/" + valoration_id + "/"
    $.ajax({
        url: url,
        type: 'GET',
        success: function (data) {
            document.getElementById("newValorationForm").innerHTML = data;
        },
        error: function () {
            alert("Error adding the valoration");
        }
    });
}

function showPaymentForm() {
    $.ajax({
        url: "/payment/",
        type: 'GET',
        success: function (data) {
            document.getElementById("paymentForm").innerHTML = data;
        },
        error: function () {
            alert("Error loading payment form");
        }
    });
}