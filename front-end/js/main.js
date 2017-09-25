var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        document.getElementById("demo").innerHTML = myArr[0];
        }
    };
}

xmlhttp.open("GET", "json_demo_aray.txt", true);
xmlhttp.send();


var papers = {
    paper1: {
        paper_code: "COMP602",
        paper_name: "Software Development Practice",
        streams: {
            stream1: {
                stream_no: 50,
                classes: {
                    class1: {
                        day: "Mon",
                        start_time: 1300,
                        end_time: 1500,
                        room: "WS114"
                    },
                    class2: {
                        day: "Tue",
                        start_time: 800,
                        end_time: 1000,
                        room: "WT206"
                    }
                }
            },
            stream2: {
                stream_no: 51,
                classes: {
                    class1: {
                        day: "Mon",
                        start_time: 1300,
                        end_time: 1500,
                        room: "WS114"
                    },
                    class2: {
                        day: "Thu",
                        start_time: 1400,
                        end_time: 1600,
                        room: "WT206"
                    }
                }
            },
            stream3: {
                stream_no: 52,
                classes: {
                    class1: {
                        day: "Mon",
                        start_time: 1300,
                        end_time: 1500,
                        room: "WS114"
                    },
                    class2: {
                        day: "Tue",
                        start_time:1000,
                        end_time: 1200,
                        room: "WT204"
                    }
                }
            },
            stream4: {
                stream_no: 53,
                classes: {
                    class1: {
                        day: "Mon",
                        start_time: 1300,
                        end_time: 1500,
                        room: "WS114"
                    },
                    class2: {
                        day: "Thu",
                        start_time: 1600,
                        end_time: 1800,
                        room: "WT203"
                    }
                }
            }
        }},
    paper2: {paper_code: "ECON601",
        paper_name: "Microeconomics",
        streams: {
            stream1: {
                stream_no: 50,
                classes: {
                    class1: {
                        day: "Wed",
                        start_time: 1300,
                        end_time: 1430,
                        room: "WG126"
                    },
                    class2: {
                        day: "Fri",
                        start_time: 15300,
                        end_time: 1700,
                        room: "WG126"
                    }
                }
            }
        }},
    paper3: {paper_code: "COMP603",
        paper_name: "Program Design and Constrution",
        streams: {
            stream1: {
                stream_no: 50,
                classes: {
                    class1: {
                        day: "Tue",
                        start_time: 1100,
                        end_time: 1300,
                        room: "WE230"
                    },
                    class2: {
                        day: "Wed",
                        start_time: 1800,
                        end_time: 2000,
                        room: "WS220"
                    },
                    class3: {
                        day: "Thu",
                        start_time: 1000,
                        end_time: 1200,
                        room: "WT407"
                    }
                }
            },
            stream2: {
                stream_no: 51,
                classes: {
                    class1: {
                        day: "Tue",
                        start_time: 1100,
                        end_time: 1300,
                        room: "WE230"
                    },
                    class2: {
                        day: "Wed",
                        start_time: 1800,
                        end_time: 2000,
                        room: "WS220"
                    },
                    class3: {
                        day: "Wed",
                        start_time: 1600,
                        end_time: 1800,
                        room: "WT301"
                    }
                }
            },
            stream3: {
                stream_no: 52,
                classes: {
                    class1: {
                        day: "Tue",
                        start_time: 1100,
                        end_time: 1300,
                        room: "WE230"
                    },
                    class2: {
                        day: "Wed",
                        start_time: 1800,
                        end_time: 2000,
                        room: "WS220"
                    },
                    class3: {
                        day: "Thu",
                        start_time: 1400,
                        end_time: 1600,
                        room: "WT301"
                    }
                }
            },
            stream4: {
                stream_no: 54,
                classes: {
                    class1: {
                        day: "Tue",
                        start_time: 1100,
                        end_time: 1300,
                        room: "WE230"
                    },
                    class2: {
                        day: "Wed",
                        start_time: 1800,
                        end_time: 2000,
                        room: "WS220"
                    },
                    class3: {
                        day: "Thu",
                        start_time: 1200,
                        end_time: 1400,
                        room: "WT301"
                    }
                }

            }
        }},
    paper4: {paper_code: "INFS601",
        paper_name: "Data and Process Modelling",
        streams: {
            stream1: {
                stream_no: 50,
                classes: {
                    class1: {
                        day: "Wed",
                        start_time: 800,
                        end_time: 1000,
                        room: "WE230"
                    },
                    class2: {
                        day: "Thu",
                        start_time: 1000,
                        end_time: 1200,
                        room: "WT203"
                    }
                }
            },
            stream2: {
                stream_no: 51,
                classes: {
                    class1: {
                        day: "Wed",
                        start_time: 800,
                        end_time: 1000,
                        room: "WE230"
                    },
                    class2: {
                        day: "Thu",
                        start_time: 1200,
                        end_time: 1400,
                        room: "WT203"
                    }
                }
            },
            stream3: {
                stream_no: 52,
                classes: {
                    class1: {
                        day: "Wed",
                        start_time: 800,
                        end_time: 1000,
                        room: "WE230"
                    },
                    class2: {
                        day: "Wed",
                        start_time: 1200,
                        end_time: 1400,
                        room: "WT204"
                    }
                }
            },
            stream4: {
                stream_no: 54,
                classes: {
                    class1: {
                        day: "Wed",
                        start_time: 800,
                        end_time: 1000,
                        room: "WE230"
                    },
                    class2: {
                        day: "Thu",
                        start_time: 1400,
                        end_time: 1600,
                        room: "WT203"
                    }
                }
            },
            stream5: {
                stream_no: 55,
                classes: {
                    class1: {
                        day: "Wed",
                        start_time: 800,
                        end_time: 1000,
                        room: "WE230"
                    },
                    class2: {
                        day: "Thu",
                        start_time: 1600,
                        end_time: 1800,
                        room: "WT203"
                    }
                }
            }
        }}
};

var proposals = {
    paper_codes: {
        paper1: "COMP602",
        paper2: "ECON601",
        paper3: "COMP603",
        paper4: "INFS601"
    },
    stream_numbers: {
        stream1: 53,
        stream2: 50,
        stream3: 50,
        stream4: 51
    }
};

//time-slot-enrolled-1

// Choose the paper and stream
// Find time and day for a class

var timetablePaper = proposals.paper_codes[1];
var timetableStream = proposals.stream_numbers[1];
var paper;
var stream;


for (index = 0, len = papers.length; index < len; ++index) {
    if(papers[index] == timetablePaper) {
        paper = papers[index];
    }
}

for (index = 0, len = paper.streams.length; index < len; ++index) {
    if(paper.streams[index] == timetableStream){
        stream = index;
    }
}

for (index = 0, len = stream.classes.length; index < len; ++index) {
    time_slot = "";
    class_ = stream.classes[index];
    time_slot = class_.day.substring(0,1);

    if ((class_.end_time - class_.end_time % 100) == 0) {
        class_length = (class_.end_time - class_.end_time)/100;
        for (hour = 0; hour < class_length; ++hour) {
            time_slot.concat( "-" + ((class_.start_time/100) + hour));
            document.getElementById(time_slot).className = "time-slot-enrolled-" + index;
        }

    }


}

$.each( papers, function( key, value ) {
    // console.log( key + ": " + value );

    $.each(value.streams, function ( subKey, subValue) {
        // body...
        // console.log( subKey + ": " + subValue );

        $.each(subValue.classes, function ( classNum, classValue) {
            // body...
            console.log( ": " , classValue);

            var id = classValue.day.toLowerCase().substring(0,2);

            classValue.start_time = '' + classValue.start_time;
            classValue.end_time = '' + classValue.end_time;


            var startId = classValue.start_time.slice(0, -2);

            var duration = classValue.end_time.slice(0, -2) - classValue.start_time.slice(0, -2);

            console.log( "startId ==> " , startId);
            console.log( "duration ==> " , duration);

            for (var i = 0; i  < duration; i++){

                var selector = id + '-' +  (parseInt(startId) + i);

                console.log( "selector ==> " , selector);


                // thsi is the js code to update each course
                $('#'+selector).html(value.paper_code + ' ' + value.paper_name);

            }

        })
    })
});




