package test;
// Update the marker title to use backticks for template literals:

// Add a marker to the user's location
const marker = new google.maps.Marker({
    position: pos,
    map: map,
    title: `Your current location: Latitude: ${pos.lat}, Longitude: ${pos.lng}, Altitude: ${pos.alt ? pos.alt : 'Not Available'}`
});

// Initialize infoWindow Globally:

let map;
let infoWindow; // Declare infoWindow globally

function initMap() {
    // Initialize infoWindow
    infoWindow = new google.maps.InfoWindow();
    // ... rest of the initMap function
}

// Properly Handle Errors in getCurrentPosition:

// Check if the Geolocation API is supported by the browser
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            // ... handle successful position retrieval
        },
        (error) => { // Use the error object
            handleLocationError(true, infoWindow, map.getCenter(), error);
        }
    );
} else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
}

// Improve handleLocationError Function:

function handleLocationError(browserHasGeolocation, infoWindow, pos, error = null) {
    infoWindow.setPosition(pos);
    let contentMessage = "Error: Your browser doesn't support geolocation.";
    if (browserHasGeolocation) {
        contentMessage = error ? `Error: ${error.message}` : "Error: The Geolocation service failed.";
    }
    infoWindow.setContent(contentMessage);
    infoWindow.open(map);
}

