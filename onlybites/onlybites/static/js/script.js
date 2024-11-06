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

    $(document).on("click", "#closeAddressFormButton", function(){
        $('#newAddressForm').empty()
    });

    $(document).on("click", "#closeLoginPopup", function(){
        $('#loginPopup').empty();
    });

    $(document).on("submit", "#addAddressForm", function(){
        e.preventDefault()
        saveAddress()
    });

    $(document).on("submit", "#editAddressForm", function(){
        e.preventDefault()
        saveAddress($('#addressId').attr('value'))
    });
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
            alert("Error reading the address form");
        }
    });
}

function saveAddress(address_id){
    url = "/add-address/"
    if(address_id){
        url = "/edit-address/" + address_id + "/"
    }
    data = $(this).serialize()
    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        success: function (response) {
            alert("ondo gorde da address-a")
        },
        error: function (response) {
            alert("Error adding the address" + response);
        }
    })
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