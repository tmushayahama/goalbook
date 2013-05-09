// ________________________________________________________________
// |-------------------------INITIALIZATIONS-----------------------|
// `````````````````````````````````````````````````````````````````

$(document).ready(function (e) {
    console.log("Loading rm.js...");
    $.ajaxSetup({traditional: true});
    populateGoals();
    populateFriends();
    populateRecentCommitments();
    populateSuggestedFriends();
    addEventHandlers();
});
function populateRecentCommitments() {
    for(var i=0; i<goals.length; i++) {
        addPost("#gb-recent-posts-home", true, goals[i]["task_name"], "Tremayne Mushayahama", "tmtrigga@gmail.com");
    }
}
function populateSuggestedFriends() {
    for(var i=0; i<suggestedFriends.length; i++) {
        addSuggestedFriend("#gb-suggested-friends", suggestedFriends[i]["username"], suggestedFriends[i]["first_name"], suggestedFriends[i]["last_name"]);
    }
}
function populateGoals () {
    for(var i=0; i<goals.length; i++) {
    $("#rm-goals-home")
        .append($("<li/>")
                .append($("<a/>")
                        .text(goals[i]["task_name"])));
    }
}
function populateFriends () {
    for(var i=0; i<friends.length; i++) {
        $("#rm-friends-selector-home")
            .append($("<label/>")
                    .addClass("checkbox")
                    .text(friends[i]["first_name"] + " " + friends[i]["last_name"])
                    .append($("<input/>")
                           
                            .attr("type", "checkbox")));
    }
}
function goalCommit(e) {
    e.preventDefault();
    $.post("commit/", $('#rm-commit-form').serialize(), function(data) {
        console.log(data);
        console.log(data["commitment"]);
        console.log(data["taskee_name"])
        addPost("#gb-recent-posts-home", false,  data["commitment"], data["taskee_name"], "tmtrigga@gmail.com");
        $("#rm-goals-home")
        .prepend($("<li/>")
                 .append($("<a/>")
                         .text(data["commitment"])));
    }, "json");
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
    $("#rm-commit-post-home").click(function(e) {
        goalCommit(e);
    });
}
