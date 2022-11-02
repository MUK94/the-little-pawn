// BAR SLIDE

let slideTextIndex = 0;
showSlidesText();

function showSlidesText() {
  let j;
  let textSlides = document.getElementsByClassName("text-Slides");
  
  for(j = 0; j < textSlides.length; j++) {
    textSlides[j].style.display = "none"
  }
  slideTextIndex++

  if (slideTextIndex > textSlides.length){slideTextIndex = 1}
  textSlides[slideTextIndex-1].style.display = "block"

  setTimeout(showSlidesText, 5000); 
}