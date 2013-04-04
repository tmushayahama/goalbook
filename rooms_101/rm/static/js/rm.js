// ________________________________________________________________
// |-------------------------INITIALIZATIONS-----------------------|
// `````````````````````````````````````````````````````````````````

$(document).ready(function (e) {
    console.log("Loading rm.js...");
    $.ajaxSetup({traditional: true});
    populateGoals();
});
function populateGoals () {
    for(var i=0; i<goals.length; i++) {
    $("#rm-goals-home")
        .append($("<li/>")
                .append($("<a/>")
                        .text(goals[i]["task_name"])));
    }
}
