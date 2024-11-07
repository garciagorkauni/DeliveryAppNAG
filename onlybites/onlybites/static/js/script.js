$(document).ready(function () {
    // Listeners for login popup
    $('#loginButton').on("click", function(){
        showLogin()
    })

    $(document).on("click", "#closeLoginPopup", function(){
        $('#loginPopup').empty();
    });


    // Listeners for addresses managemet
    $('.editAddressButton').on("click", function(){
        showNewAddressForm($(this).attr('id'))
    })

    $('#addAddressButton').on("click", function(){
        showNewAddressForm()
    })

    $(document).on("click", "#closeAddressFormButton", function(){
        $('#newAddressForm').empty()
    });

    $(document).on("submit", "#addAddressForm", function(e){
        e.preventDefault()
        saveAddress()
    });

    $(document).on("submit", "#editAddressForm", function(e){
        e.preventDefault()
        saveAddress($('#addressId').attr('value'))
    });


    // Listeners for product filters
    $(document).on("change", "#vegan", function(e){
        alert("Vegan filter changed")
    });

    $(document).on("change", "#celiac", function(e){
        alert("Celiac filter changed")
    });

    $(document).on("change", "#max-calories", function(e){
        alert("Max calories filter changed")
    });

    $(document).on("change", "#allergiesList", function(e){
        alert("Allergies selector filter changed")
    });
})

// AJAX function for get login popup html
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

// AJAX function for get address form html
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

// AJAX function for saving new or edited address
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

// AJAX function for get updated addresses list html
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

// AJAX function for get valoration form html
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

// AJAX function for get payment form html
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

// Function for show and hide product filters in menu
function toggleFilters() {
    const filterContainer = document.getElementById('filter-container');
    if (filterContainer.style.display === 'none' || filterContainer.style.display === '') {
        filterContainer.style.display = 'block';
    } else {
        filterContainer.style.display = 'none';
    }
}