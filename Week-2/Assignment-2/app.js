const heading = document.querySelector("h1");
const button = document.querySelector("#button");
const moreBox = document.querySelectorAll(".moreBox");
const hide = document.querySelector(".hide");
const downArrow = document.querySelector("#downArrow");
const upArrow = document.querySelector("#upArrow");

heading.addEventListener("click", () => {
  if (heading.textContent == "Have a Good Time!"){
    heading.textContent = "Welcome Message";
  } else {
    heading.textContent = "Have a Good Time!";
  }
})

button.addEventListener("click", () => {
  if (moreBox[0].style.display == 'inline-block') {
    for (var i = 0; i < moreBox.length; i++){
      moreBox[i].style.display='none';
    }
    upArrow.style.display = "none";
  } else {
    for (var i = 0; i < moreBox.length; i++){
      moreBox[i].style.display='inline-block';
    }
    downArrow.style.display = "none";
  }
})


// button.addEventListener("click", () => {
//   if (moreBox[0].style.display == 'none') {
//     for (var i = 0; i < moreBox.length; i++){
//       moreBox[i].style.display='inline-block';
//     }
//     button.textContent = " \u25b2 ";
//   } else {
//     for (var i = 0; i < moreBox.length; i++){
//       moreBox[i].style.display='none';
//     }
//     button.textContent = "Call to Action \u25bc";
//   }
// })

// use event instead of hover in CSS

button.addEventListener("mouseenter", () => {
  button.style.backgroundColor = "rgb(159, 198, 236)";
  button.style.color = "white";
  if (moreBox[0].style.display == 'inline-block') {
    upArrow.style.display = "inline";
    downArrow.style.display = "none";
  } else {
    downArrow.style.display = "inline";
    upArrow.style.display = "none";
  }
})

button.addEventListener("mouseleave", () => {
  button.style.backgroundColor = "rgb(204, 220, 236)";
  button.style.color = "black";
  if (moreBox[0].style.display == 'inline-block') {
    upArrow.style.display = "none";
  } else {
    downArrow.style.display = "none";
  }
})