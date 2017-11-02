// Choose the paper and stream
// Find time and day for a class
/*
function updateTimetable(){
for (papers_no  = 0; papers_no < 4; ++papers_no) {
    let timetablePaper = proposals[0][papers_no];
    console.log(timetablePaper);
    let timetableStream = proposals[1][papers_no];
    console.log(timetableStream);
    let paper = "";
    let stream = 0;

    for (index = 0, len = papers.length; index < len; ++index) {
        if(papers[index].paper_code == timetablePaper) {
            paper = papers[index];
            console.log(paper);
            break;
        }
    }

    for (index = 0, len = paper.streams.length; index < len; ++index) {
        if(paper.streams[index].stream_no == timetableStream){
            stream = paper.streams[index];
            console.log(stream);
            break;
        }
    }

    for (index = 0, len = stream.classes.length; index < len; ++index) {
        let time_slot = "";
        let lecture = stream.classes[index];
        time_slot = lecture.day.substring(0, 2).toLowerCase().concat("-");


        if (((lecture.end_time - lecture.end_time) % 100) == 0) {
            class_length = (lecture.end_time - lecture.start_time) / 100;
            for (hour = (lecture.start_time / 100); hour < (lecture.end_time / 100); ++hour) {
                let temp_time_slot = time_slot.concat(hour);
                document.getElementById(temp_time_slot).className = "time-slot-enrolled-" + (papers_no+1);
                if (hour == (lecture.start_time / 100)) {
                    document.getElementById(temp_time_slot).innerHTML = paper.paper_name;
                }
            }

        }

    }
}

}
*/
function clearTimetable() {
    let timeslotArray = document.getElementsByClassName("time-slot-enrolled");

    for(let i = (timeslotArray.length - 1); i >= 0; i--)
    {
        timestampArray[i].className = "time-slot";
    }
}

var listOfPapers = [];
var combinationOfStreams = [];



function addPaper() {
    let paper_added = document.getElementsByClassName("selectpicker").title;
    console.log(paper_added);
    document.getElementsById("class1").innerHTML = "";
    document.getElementsById("class1").innerHTML = paper_added;
}

async function getPaperInfo(paper_id, callback) {

    jsonData = JSON.stringify({
        request: 'info',
        paper_id: paper_id
    });

    console.log(jsonData);

    $.ajax({
        url: '/api/',
        type: 'POST',
        dataType: 'json',
        data: jsonData,
        success: callback,
        error: (response) => {
            console.log("Errors!");
            console.log(response);
        },

    })
}

async function getPaperCombos(papers_list, callback) {

    jsonData = JSON.stringify({
        request: 'algorithm',
        papers: papers_list
    });

    console.log(jsonData);

    $.ajax({
        url: '/api/',
        type: 'POST',
        dataType: 'json',
        data: jsonData,
        success: callback,
        error: (response) => {
            console.log("Errors!");
            console.log(response);
        },

    })
}



async function addPaper(paper_id, callback) {
    await getPaperInfo(paper_id, (response) => {
        console.log(response);
        listOfPapers.push(response);
        console.log(listOfPapers);
    });
}

async function getCombo(listOfPaperCodes, callback) {
    await getPaperCombos(listOfPaperCodes, (response) => {
        console.log(response);
        combinationOfStreams.push(response);
    })
}

async function start() {
    console.log("Calling the API");
    ajaxTest('COMP602');
}

$(function() {
    console.log("Ready for business");
});

$('.selectpicker').change(function () {
    console.log("A paper has been selected");
    if ($("#paperButtons > button").length >= 4) {
        console.log("4 papers are already selected");
        return;
    }
    var paperAlreadyExists = 0;
    $('#paperButtons > button').each(function () {
        console.log('Paper already in list: ' + $(this).text());
        console.log('Paper trying to be added: ' + $('.selectpicker').find("option:selected").text());
        if ($(this).text() == $('.selectpicker').find("option:selected").text()) {

            console.log("Paper already in listOfPapers");
            paperAlreadyExists = 1;
            return;
        }
    });

    if (paperAlreadyExists == 0) {
        var selectedPaperCode = $(this).find("option:selected").data("subtext");
        addPaper(selectedPaperCode);

        var selectedText = $(this).find("option:selected").text();
        var newButton = document.createElement("button");
        newButton.setAttribute('class','btn paper-btn');
        newButton.setAttribute('type','button');
        newButton.setAttribute('id',selectedPaperCode);
        newButton.setAttribute('text', selectedText);
        newButton.innerHTML = selectedText;

        document.getElementById("paperButtons").appendChild(newButton);
        console.log("New paper button has been created");
    }


});

function displayPaperInfo() {
    console.log("Display Paper Info");
};

function addButton() {


}

function paintTimetable() {
    console.log("Painting Streams to Timetable");




}

function updateTimetable() {
    console.log("Update timetable clicked");
    console.log("Requesting data from server");

    var listOfPaperCodes = [];

    listOfPapers.forEach(function (currentValue){
        listOfPaperCodes.push(currentValue.paper_id);
        console.log(listOfPaperCodes);
    })

    getCombo(listOfPaperCodes);

    paintTimetable();
}




