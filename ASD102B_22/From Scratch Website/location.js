// Your API Key
const API_KEY = "AIzaSyBEaz4eKf8OUbzsBGGR5v_rhjQeO9I2pRs";

// Check if Geolocation is supported
if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition((position) => {
        const { latitude, longitude, altitude } = position.coords;
        
        // Displaying the retrieved latitude, longitude, and altitude
        document.getElementById('latitude').textContent = latitude.toFixed(2);
        document.getElementById('longitude').textContent = longitude.toFixed(2);
        document.getElementById('altitude').textContent = altitude ? `${altitude.toFixed(2)} meters` : 'Unavailable';

        // Initialize Google Maps
        const myLatLng = new google.maps.LatLng(latitude, longitude);
        const mapOptions = {
            zoom: 15,
            center: myLatLng,
        };
        const map = new google.maps.Map(document.getElementById('map'), mapOptions);
        new google.maps.Marker({
            position: myLatLng,
            map,
            title: "You are here",
        });
    });
} else {
    alert("Geolocation is not supported by this browser.");
}

// Load the Google Maps API
const script = document.createElement('script');
script.src = `https://maps.googleapis.com/maps/api/js?key=${API_KEY}`;
document.getElementsByTagName('head')[0].appendChild(script);