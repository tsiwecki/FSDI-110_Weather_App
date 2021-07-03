
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(locationSucceed);
    }
    else {
        alert("Your browser does not support location")
    }    
}

function locationSucceed(position) {
    console.log("Current location", position);

    let data = {
        lat: position.coords.latitude,
        lon: position.coords.longitude,        
    };

    $.ajax({
        url: '/',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(res) {
            console.log("Server says: ", res);
            
            document.write("Current Temperature:  ", res.current.temp, "  F");
            document.write("<br>");
            document.write("<br>");
            document.write("Feels Like Temperature:  ", res.current.feels_like, "  F");
            document.write("<br>");
            document.write("<br>");
            document.write("Current Description:  ", res.current.weather[0].description);
            document.write("<br>");
            document.write("<br>");
            document.write("Humidity:  ", res.current.humidity);
            document.write("<br>");
            document.write("<br>");
            document.write("Wind Speed:  ", res.current.wind_speed);
            document.write("<br>");
            document.write("<br>");
            document.write("Current Alerts:   ", res.alerts[0].description)
            
        },
        error: function (err) {
            console.error("Error getting location", err);
        },
        error: function (err) {
            console.error("Error getting weather", err);
        }
    });
}



function init() {
    console.log("Weather page!")

    getLocation();
}




window.onload = init;
