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