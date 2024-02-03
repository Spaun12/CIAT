// Declare global variables for map and infoWindow
let map;
let infoWindow;

// Initialize the map and add geolocation functionality
function initMap() {
    // Create a new map and set its initial zoom level
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 6,
    });

    // Initialize the infoWindow
    infoWindow = new google.maps.InfoWindow();

    // Check if the Geolocation API is supported by the browser
    if (navigator.geolocation) {
        // Try to get the current position of the user
        navigator.geolocation.getCurrentPosition(
            (position) => {
                // Create a position object with the latitude and longitude
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                    // Use altitude if available or indicate it's not available
                    alt: position.coords.altitude || 'Not Available'
                };

                // Set the center of the map to the user's current position
                map.setCenter(pos);

                // Add a marker to the map at the user's current position
                const marker = new google.maps.Marker({
                    position: pos,
                    map: map,
                    // Use a template literal with backticks to include variables
                    title: `Your current location: Latitude: ${pos.lat}, Longitude: ${pos.lng}, Altitude: ${pos.alt}`
                });
            },
            (error) => {
                // Call handleLocationError with the error object if geolocation fails
                handleLocationError(true, infoWindow, map.getCenter(), error);
            }
        );
    } else {
        // Handle the case where the browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
}

// Define the handleLocationError function
function handleLocationError(browserHasGeolocation, infoWindow, pos, error = null) {
    // Set the position of the infoWindow to the provided position
    infoWindow.setPosition(pos);

    // Determine the content message based on whether the browser supports geolocation
    // and whether an error message is provided
    let contentMessage = browserHasGeolocation
        ? (error ? `Error: ${error.message}` : "Error: The Geolocation service failed.")
        : "Error: Your browser doesn't support geolocation.";

    // Set the content of the infoWindow and open it on the map
    infoWindow.setContent(contentMessage);
    infoWindow.open(map);
}
