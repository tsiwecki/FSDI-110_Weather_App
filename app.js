
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(locationSucceed, locationError);
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
        url: '/api/weather',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function (res) {
            console.log("Server says: ", res);
            
            console.log("current temp:  ", res.current.temp);
            console.log("current desc:  ", res.current.weather[0].description);

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
