$(function(){
    alert("Hello");
    $("#student").text("waiting for results");
    setInterval(refreshQueue,5000);
});

functionrefreshQueue(){
    $.getJSON('/allStudents', function(d){
            $('#student').empty();
            $('#debug').empty();
            for (var i=0; i < d.length; i++){
                $('<div/>')
                    .append($("<span/>", {text:d[i][0]+ " " + d[i][1]}))
                    .append($('<br/>'))
                    .append('#student');
            }
    });
};