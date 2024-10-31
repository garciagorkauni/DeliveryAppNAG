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

function showNewAddressFrom(address_id){
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

function minusCartQuantity(quantity, cart_id){
    quantity--
    if(quantity <= 0){
        window.location.replace("{% url 'delete_cart' cart_id=" + cart_id + " %}")
    } else {
        document.getElementById("cart-quantity").innerHTML = quantity;
        window.location.replace("{% url 'update_cart' cart_id=" + cart_id + " quantity=" + quantity + " %}")
    }
}

function plusCartQuantity(quantity, cart_id){
    quantity++
    document.getElementById("cart-quantity").innerHTML = quantity;
    window.location.replace("{% url 'update_cart' cart_id=" + cart_id + " quantity=" + quantity + " %}")
}

// El problema es que el {% url ...%} se tiene que cargar en el server antes de mandarselo al cliente, pero el js se carga directamente en el cliente