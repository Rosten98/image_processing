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

let imgElement = document.getElementById('imageSrc')
let inputElement = document.getElementById('fileInput')
let colorControls = document.getElementById('color-controls')
let modal = document.getElementById('modal')
let modalBtn = document.getElementById('open-modal')
let span = document.getElementsByClassName("close")[0];
let loader = document.getElementById('loader')
let page = document.getElementById('page')
let mat, matOriginal

// MODAL ----------------
modalBtn.onclick = function() {
  modal.style.display = "block";
  colorScale()
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// OpenCV ----------------
inputElement.addEventListener('change', (e) => {
  imgElement.src = URL.createObjectURL(e.target.files[0]);
}, false);

imgElement.onload = function() {
  mat = cv.imread(imgElement);
  matOriginal = mat
  cv.imshow('canvasOutput', mat);
  // mat.delete();
};

function editImage(colorType) {
  switch (colorType) {
    case "color-scale":
      console.log(colorType)
      colorScale();
      break;
    case "gray-scale":
      console.log(colorType)
      grayScale();
      break;
  }
}

function resetComponents() {
    let checkBlur = document.getElementById('check-blur')
    let checkOtsu = document.getElementById('check-otsu')
    let checkErode = document.getElementById('check-erode')

    let rangeBlur = document.getElementById('blur-range')
    let rangeOtsu = document.getElementById('otsu-range')
    let rangeErode = document.getElementById('erode-range')

    checkBlur.checked = false
    checkOtsu.checked = false
    checkErode.checked = false

    rangeBlur.value = 0
    rangeOtsu.value = 0
    rangeErode.value = 0

    rangeBlur.style.display = "none"
    rangeOtsu.style.display = "none"
    rangeErode.style.display = "none"
}

function grayScale() {
  // colorControls.style.display = "none"
  let dst = new cv.Mat()
  mat = cv.imread(imgElement)
  mat = cv.cvtColor(mat, dst, cv.COLOR_RGBA2GRAY, 0)
  cv.imshow('canvasOutput', dst)
  matOriginal = dst
  mat = dst
  resetComponents()
  // mat.delete();
  // dst.delete();
}

function colorScale() {
  // colorControls.style.display = "initial"
  mat = cv.imread(imgElement);
  matOriginal = mat
  cv.imshow('canvasOutput', mat);
  resetComponents()
  // mat.delete();
}

function resize() {
  let slider = document.getElementById('resize-range')
  let src = matOriginal
  let dst = new cv.Mat();
  let dsize = new cv.Size(matOriginal.cols*parseInt(slider.value)*.01, matOriginal.rows*parseInt(slider.value)*.01);
  // // You can try more different parameters
  cv.resize(src, dst, dsize, 0, 0, cv.INTER_AREA);
  cv.imshow('canvasOutput', dst);
  mat = dst
  resetComponents()
  // dst.delete();
}

function toggleBlur(){
  let blurRange = document.getElementById('blur-range')
  let checkBlur = document.getElementById('check-blur')
  if(checkBlur.checked){
    resetComponents()
    checkBlur.checked = true
    blurRange.style.display = "initial"
    matOriginal = mat
  }
  else{
    blurRange.style.display = "none"
    cv.imshow('canvasOutput', matOriginal)
  }
}


function blurCV() {
  let sliderBlur = document.getElementById('blur-range')
  console.log(sliderBlur.value);
  let src = matOriginal
  let dst = new cv.Mat();
  let ksize = new cv.Size(parseInt(sliderBlur.value), parseInt(sliderBlur.value));
  let anchor = new cv.Point(-1, -1);
  // You can try more different parameters
  cv.blur(src, dst, ksize, anchor, cv.BORDER_DEFAULT);
  // cv.boxFilter(src, dst, -1, ksize, anchor, true, cv.BORDER_DEFAULT)
  cv.imshow('canvasOutput', dst);
  // src.delete();
  dst.delete();
}

function toggleOtsu(){
  let checkOtsu = document.getElementById('check-otsu')
  let otsuRange = document.getElementById('otsu-range')
  if(checkOtsu.checked){
    resetComponents()
    checkOtsu.checked = true
    otsuRange.style.display = "initial"
    matOriginal = mat
  }
  else
    otsuRange.style.display = "none"
}

function otsu() {
  let sliderOtsu = document.getElementById('otsu-range')
  let src = matOriginal
  let dst = new cv.Mat();
  // You can try more different parameters
  cv.threshold(src, dst, parseInt(sliderOtsu.value), 200, cv.THRESH_BINARY);
  cv.imshow('canvasOutput', dst);
  // src.delete();
  dst.delete();
}

function toggleErode(){
  let checkErode = document.getElementById('check-erode')
  let erodeRange = document.getElementById('erode-range')
  if(checkErode.checked){
    resetComponents()
    checkErode.checked = true
    erodeRange.style.display = "initial"
    matOriginal = mat
  }
  else
    erodeRange.style.display = "none"
}

function erode() {
  let sliderErode = document.getElementById('erode-range')
  let src = matOriginal
  let dst = new cv.Mat();
  let M = cv.Mat.ones(parseInt(sliderErode.value), parseInt(sliderErode.value), cv.CV_8U);
  let anchor = new cv.Point(-1, -1);
  // You can try more different parameters
  cv.erode(src, dst, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
  cv.imshow('canvasOutput', dst);
  dst.delete();
}


// Check if opencv is already loaded
function onOpenCvReady() {
  document.getElementById('status').innerHTML = 'OpenCV.js is ready.';
  loader.style.display = "none";
  page.style.display = "initial";
}
