// gallery.js

// Get the gallery element
const gallery = document.getElementById('image-gallery');

// Get the pagination buttons
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

// Initialize the current page
let currentPage = 1;

// Fetch images from the server
function fetchImages(page) {
  fetch(`/images?page=${page}`)
    .then(response => response.json())
    .then(data => {
      // Clear the gallery
      gallery.innerHTML = '';

// Add images to the gallery
for (const image of data.images) {
    const img = document.createElement('img');
    img.src = `Cyber Punk Images/${image}`; // Modify this line
    gallery.appendChild(img);
  }
  

      // Enable or disable pagination buttons
      prevBtn.disabled = data.prevPage === null;
      nextBtn.disabled = data.nextPage === null;

      // Update the current page
      currentPage = page;
    });
}

// Fetch images for the first page when the page loads
fetchImages(currentPage);

// Add event listeners for the pagination buttons
prevBtn.addEventListener('click', () => fetchImages(currentPage - 1));
nextBtn.addEventListener('click', () => fetchImages(currentPage + 1));
