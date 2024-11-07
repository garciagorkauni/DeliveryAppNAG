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

    $(document).on("submit", "#addAddressForm", function(e){
        e.preventDefault()
        saveAddress()
    });

    $(document).on("submit", "#editAddressForm", function(e){
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

function saveAddress(address_id = null){
    let url = "/add-address/"
    if(address_id){
        url = "/edit-address/" + address_id + "/"
    }
    let data = $('#addAddressForm, #editAddressForm').serialize()

    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        success: function (response) {
            $('#newAddressForm').empty()
            updateAddressList();
        },
        error: function (response) {
            alert("Error adding the address.");
        }
    });
}

function updateAddressList() {
    $.ajax({
        url: "/update-address-list/", 
        type: 'GET',
        success: function (data) {
            document.getElementById("addressList").innerHTML = data
        },
        error: function () {
            alert("Error updating the address list.")
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

function toggleFilters() {
    const filterContainer = document.getElementById('filter-container');
    if (filterContainer.style.display === 'none' || filterContainer.style.display === '') {
        filterContainer.style.display = 'block';
    } else {
        filterContainer.style.display = 'none';
    }
}