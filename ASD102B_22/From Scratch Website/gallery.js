// gallery.js

let captions = new Array(14);
captions[0]="Cool Cyber Punk Image 1";
captions[1]="Cool Cyber Punk Image 2";
captions[2]="Cool Cyber Punk Image 3";
captions[3]="Cool Cyber Punk Image 4";
captions[4]="Cool Cyber Punk Image 5";
captions[5]="Cool Cyber Punk Image 6";
captions[6]="Cool Cyber Punk Image 7";
captions[7]="Cool Cyber Punk Image 8";
captions[8]="Cool Cyber Punk Image 9";
captions[9]="Cool Cyber Punk Image 10";
captions[10]="Cool Cyber Punk Image 11";
captions[11]="Cool Cyber Punk Image 12";
captions[12]="Cool Cyber Punk Image 13";
captions[13]="Cool Cyber Punk Image 14";


let htmlCode = "";

for (let i = 0; i < captions.length; i++) {
   // Add 1 to i for the image number (to match your file names) and pad start with 0 to always have two digits
   let imageNumber = (i + 1).toString().padStart(2, '0');
   htmlCode += `<figure>
   <img alt='' src='Cyber Punk ${imageNumber}.png' />
   <figcaption>${captions[i]}</figcaption>
</figure>`;
}

document.getElementById("gallery").innerHTML = htmlCode;