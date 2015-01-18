/**
 * Created by nonex_000 on 1/13/2015.
 */
function get_element(a) {
    return document.getElementById(a);
}

function load_data() {
    alert("starting data load");
    $("#data_holder").load("/api/something/test_worked!", function (responseTxt, statusTxt, xhr) {
        if (statusTxt == "success")
            alert("External content loaded successfully!");
        if (statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
    });

}

function post_data(message) {
    //message = get_element("data_holder").elements.length;
    message = document.getElementById("form1").elements["message_box"].value;
    console.log(message)
    $.post("/api/submit", {
        message: message
    })
}

function subscribe() {
    
}

function async_load(name, item) {
    $("name").innerHTML += item;
}