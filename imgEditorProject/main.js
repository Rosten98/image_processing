// let editBtn, imgUpload, imgEdit
//
// window.addEventListener('DOMContentLoaded', (event) => {
//     console.log('DOM fully loaded and parsed')
//
//     editBtn = document.getElementById('edit-img')
//     imgUpload = document.getElementById('img-upload')
//     imgEdit = document.getElementById('img-to-edit')
//
//     editBtn.disabled = true
//
//     imgUpload.addEventListener('change', function() {
//       if (this.files && this.files[0]) {
//           var img = document.querySelector('img');  // $('img')[0]
//           img.src = URL.createObjectURL(this.files[0]); // set src to blob url
//           img.onload = imageIsLoaded;
//       }
//     });
// });
//
//
// function imageIsLoaded() {
//   console.log(this.src);  // blob url
//   // update width and height ...
// }

let imgElement = document.getElementById('imageSrc');
let inputElement = document.getElementById('fileInput');
let mat
inputElement.addEventListener('change', (e) => {
  imgElement.src = URL.createObjectURL(e.target.files[0]);
}, false);

imgElement.onload = function() {
  mat = cv.imread(imgElement);
  cv.imshow('canvasOutput', mat);
  mat.delete();
};

function editImage(colorType) {
  console.log(colorType)
  let dst = new cv.Mat()
  mat = cv.imread(imgElement);
  mat = cv.cvtColor(mat, dst, cv.COLOR_RGBA2GRAY, 0);
  cv.imshow('canvasOutput', dst)
  mat.delete();
  dst.delete();
}

// Check if opencv is already loaded
function onOpenCvReady() {
  document.getElementById('status').innerHTML = 'OpenCV.js is ready.';
}
