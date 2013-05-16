$(document).ready(function (e) {
    console.log("Loading rm_profile.js...");
    $.ajaxSetup({traditional: true});
 /*   if (authorization=="owner") {
        populateRecentCommitments(); 
        populateSuggestedFriends();
    }*/
    addEventHandlers();
});
function populateRecentCommitments() {
    for(var i=0; i<goals.length; i++) {
        addPost("#gb-recent-posts-profile", true, goals[i]["task_name"], "Tremayne Mushayahama", "tmtrigga@gmail.com");
    }
}
function populateSuggestedFriends() {
    for(var i=0; i<suggestedFriends.length; i++) {
        addSuggestedFriend("#gb-suggested-friends", suggestedFriends[i]["username"], suggestedFriends[i]["first_name"], suggestedFriends[i]["last_name"]);
    }
}
function goalCommit(e) {
    e.preventDefault();
    $.post("commit/", $('#rm-commit-form').serialize(), function(data) {
        console.log(data);
        console.log(data["commitment"]);
        console.log(data["taskee_name"])
        addPost("#gb-recent-posts-profile", false,  data["commitment"], data["taskee_name"], "tmtrigga@gmail.com");
        $("#rm-goals-home")
        .prepend($("<li/>")
                 .append($("<a/>")
                         .text(data["commitment"])));
    }, "json");
}
function sendRequest(e, url) {
    alert(url);
    e.preventDefault();
    $.post(url, function(data) {
        console.log(data);
      //  console.log(data["request"]);
       // console.log(data["taskee_name"])
       
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
    $(".gb-send-request").click(function(e) {
        sendRequest(e, $(this).attr('send-request-url'));
    });
    $('#rm-profile-tab a').click(function (e) {
        console.log("tab clicked");
        e.preventDefault();
        $(this).tab('show');
    });
}
