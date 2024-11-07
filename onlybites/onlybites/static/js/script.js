$(document).ready(function () {
    // Listeners for login popup
    $('#loginButton').on("click", function(){
        showLogin()
    })

    $(document).on("click", "#closeLoginPopup", function(){
        $('#loginPopup').empty();
    })


    // Listeners for addresses managemet
    $('.editAddressButton').on("click", function(){
        showNewAddressForm($(this).attr('id'))
    })

    $('#addAddressButton').on("click", function(){
        showNewAddressForm()
    })

    $(document).on("click", "#closeAddressFormButton", function(){
        $('#newAddressForm').empty()
    })

    $(document).on("submit", "#addAddressForm", function(e){
        e.preventDefault()
        saveAddress()
    })

    $(document).on("submit", "#editAddressForm", function(e){
        e.preventDefault()
        saveAddress($('#addressId').attr('value'))
    })


    // Listeners for product filters
    const selected_filters = {
        vegan: false,
        celiac: false,
        maxCalories: 0,
        allergies: []
    }

    $(document).on("change", "#vegan", function(e){
        selected_filters.vegan = $('#vegan')[0].checked

        updateProductList(selected_filters.vegan, 
            selected_filters.celiac, 
            selected_filters.maxCalories, 
            selected_filters.allergies)
    })

    $(document).on("change", "#celiac", function(e){
        selected_filters.celiac = $('#celiac')[0].checked

        updateProductList(selected_filters.vegan, 
            selected_filters.celiac, 
            selected_filters.maxCalories, 
            selected_filters.allergies)
    })

    $(document).on("change", "#max-calories", function(e){
        selected_filters.maxCalories = $("#max-calories").val()

        updateProductList(selected_filters.vegan, 
            selected_filters.celiac, 
            selected_filters.maxCalories, 
            selected_filters.allergies)
    })

    $(document).on("change", "#allergiesList", function(e){
        selected_filters.allergies = []
        $(".allergies").each(function() {
            if ($(this).is(":checked")) {
                selected_filters.allergies.push($(this).attr("name"));
            }
        })
        
        updateProductList(selected_filters.vegan, 
            selected_filters.celiac, 
            selected_filters.maxCalories, 
            selected_filters.allergies)
    })
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

// AJAX function for get updated and filtered product list html
function updateProductList(vegan, celiac, max_calories, allergies) {
    allergiesStr = ''
    for (let index = 0; index < allergies.length; index++) {
        allergiesStr += allergies[index] + '-'
    }
    $.ajax({
        url: "/update-product-list/",
        type: 'GET',
        data: {
            vegan: vegan,
            celiac: celiac,
            max_calories: max_calories,
            allergies: allergiesStr
        },
        success: function (data) {
            document.getElementById("productList").innerHTML = data;
        },
        error: function () {
            alert("Error updating the product list.");
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