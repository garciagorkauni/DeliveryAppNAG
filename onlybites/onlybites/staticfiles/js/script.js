const selected_filters = {
    vegan: false,
    celiac: false,
    maxCalories: 0,
    allergies: []
}

$(document).ready(function () {
    // Listeners for login popup
    $(document).on("click", "#loginButton", function(){
        showLogin()
    })

    $(document).on("click", "#closeLoginPopup", function(){
        $('#loginPopup').empty();
    })


    // Listeners for addresses managemet
    $(document).on("click", ".editAddressButton", function(){
        showNewAddressForm($(this).attr('id'))
    })

    $(document).on("click", "#addAddressButton", function(){
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
    $(document).on("submit", ".filter-form", function(e){
        e.preventDefault()
    })

    $(document).on("click", "#dropdownbutton", function(){
        toggleFilters()
    })

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

    if (window.location.pathname === '/products/') { // This will be executed when the web is refreshed
        getFilters()
    }


    // Listener for payment simulation
    $(document).on("click", "#paymentButton", function(){
        showPaymentForm()
    })

    $(document).on("click", "#closePaymentFormButton", function(){
        $('#paymentForm').empty()
    })


    // Listener for valoration
    $(document).on("click", "#newValorationButton", function(){
        showNewValorationForm($('#productId').attr('value'))
    })

    $(document).on("click", "#closeRatingFormButton", function(){
        $('#newValorationForm').empty()
    })


    // Listeners for cart features
    $(document).on("click", ".reduceCartButton", function(){
        reduceCartQuantity($(this).attr('id'))
    })

    $(document).on("click", ".incrementCartButton", function(){
        incrementCartQuantity($(this).attr('id'))
    })

    $(document).on("click", ".deleteCartButton", function(){
        deleteCart($(this).attr('id'))
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

// AJAX function for reduce one cart quantity
function reduceCartQuantity(cart_id){
    let url = "/reduce-cart/" + cart_id
    $.ajax({
        type: 'GET',
        url: url,
        success: function (data) {
            document.getElementById("cartList").innerHTML = data
        },
        error: function (data) {
            alert("Error reducing the cart.")
        }
    })
}

// AJAX function for increment one cart quantity
function incrementCartQuantity(cart_id){
    let url = "/add-cart/" + cart_id
    $.ajax({
        type: 'GET',
        url: url,
        success: function (data) {
            if (window.location.pathname.split("/")[2] != 'cart') { 
                window.location.pathname = '/cart/'
            }
            document.getElementById("cartList").innerHTML = data
        },
        error: function (data) {
            alert("Error incrementing the cart.")
        }
    })
}

// AJAX function for delete cart quantity
function deleteCart(cart_id){
    let url = "/delete-cart/" + cart_id
    $.ajax({
        type: 'GET',
        url: url,
        success: function (data) {
            document.getElementById("cartList").innerHTML = data
        },
        error: function (data) {
            alert("Error deleting the cart.")
        }
    })
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

// Function to see which filters are checked
function getFilters() {
    selected_filters.vegan = $('#vegan')[0].checked
    selected_filters.celiac = $('#celiac')[0].checked
    selected_filters.maxCalories = $("#max-calories").val()
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
}