$(document).ready(function (e) {
    addEventHandlers()
});

function addEventHandlers () {
    $('#rm-profile-tab a').click(function (e) {
        console.log("tab clicked");
        e.preventDefault();
        $(this).tab('show');
    });
}
function initProfile(authorization) {
    if (authorization=="owner") {
        
    } else if (authorization=="friend") {
    } else {
    }
}