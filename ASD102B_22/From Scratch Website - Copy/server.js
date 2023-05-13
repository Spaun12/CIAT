const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from the "public" directory
app.use(express.static('public'));

// Endpoint to get images
app.get('/images', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const imagesPerPage = 18; // 3 x 6 images per page
  const offset = (page - 1) * imagesPerPage;

  // Path to your images folder. The '__dirname' variable represents the current directory where the server.js file is located.
  // 'path.join' is used to create a filepath that works on any operating system. It joins all given path segments together 
  // and normalizes the resulting path.
  const folder = path.join(__dirname, 'Cyber Punk Images');
  
  // The 'fs.readdir' function reads the content of a directory. It takes two arguments: the path to the directory and a callback
  // function to be called when the directory has been read. The callback function takes two arguments: an error object and an 
  // array of filenames.
  fs.readdir(folder, (err, files) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error reading images directory');
      return;
    }

    // Filter out non-image files
    const images = files.filter(file => ['.jpg', '.jpeg', '.png', '.gif'].includes(path.extname(file).toLowerCase()));

    const totalImages = images.length;
    // Calculate the total pages
    const totalPages = Math.ceil(totalImages / imagesPerPage);

    // Get the images for the current page
    const pageImages = images.slice(offset, offset + imagesPerPage);

    // Send the images and pagination info as a JSON response
    res.json({
      images: pageImages,
      prevPage: page > 1 ? page - 1 : null,
      nextPage: page < totalPages ? page + 1 : null,
    });
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

