// ________________________________________________________________
// |-------------------------INITIALIZATIONS-----------------------|
// `````````````````````````````````````````````````````````````````

$(document).ready(function (e) {
    console.log("Loading rm.js...");
    $.ajaxSetup({traditional: true});
    populateGoals();
    addEventHandlers();
});
function populateGoals () {
    for(var i=0; i<goals.length; i++) {
    $("#rm-goals-home")
        .append($("<li/>")
                .append($("<a/>")
                        .text(goals[i]["task_name"])));
    }
}
function addEventHandlers() {
    $('#rm-post-tab a').click(function (e) {
        console.log("tab clicked");
        e.preventDefault();
        $(this).tab('show');
    });
     $('.rm-stop-propagation').click(function (e) {
        e.stopPropagation();
    });
     $( "#rm-post-start-dp" ).datepicker({
         changeMonth: true,
         changeYear: true
     });
     $( "#rm-post-end-dp" ).datepicker({
         changeMonth: true,
         changeYear: true
     });
}
