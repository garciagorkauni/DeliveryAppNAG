function showLogin(){
    $.ajax({
        url: "http://localhost:8000/login/",
        type: 'GET',
        success: function (data) {
            document.getElementById("loginPopup").innerHTML = data;
            document.getElementById("loginPopup").style.display = "block";
        },
        error: function () {
            alert("Error with login");
        }
    });
}