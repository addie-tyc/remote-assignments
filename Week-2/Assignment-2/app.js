const heading = document.querySelector("h1");
const button = document.querySelector("#button");
const moreBox = document.querySelectorAll(".moreBox");

heading.addEventListener("click", () => {
  heading.textContent = "Have a Good Time!";
})

button.addEventListener("click", () => {
  for (var i = 0; i < moreBox.length; i++){
    moreBox[i].style.display='inline-block';
  }
})

