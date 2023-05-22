const API_KEY = 'wAx5frf51MSlP7Ta9EAqecBuTjPp1GpLLqbUIQBI'; // replace with your API key
const API_URL = `https://api.nasa.gov/planetary/apod?api_key=${API_KEY}`;

fetch(API_URL)
  .then(response => response.json())
  .then(data => {
    const image = data.url;
    const explanation = data.explanation;
    const title = data.title;

    // Assuming you have img and p HTML elements in your HTML file
    document.getElementById('apod-image').src = image;
    document.getElementById('apod-title').textContent = title;
    document.getElementById('apod-explanation').textContent = explanation;
  })
  .catch(error => console.error(error));
