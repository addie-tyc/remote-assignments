const submit = document.querySelector("#submit");
const sum = document.querySelector("#sum");
const result = document.querySelector("#result");
const welcomeMsg = document.querySelector("#welcomeMsg");
const form = document.querySelector("#form");

function loadDoc() {
  var n = document.querySelector("#N").value;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        sum.innerHTML = this.responseText;
   }
  };
  xhttp.open("GET", "http://localhost:3000/data?number="+n, true);
  xhttp.send();
  history.replaceState("", "", "data?number=" + n); //change url without load
  document.querySelector("#N").value = ""; // clear input value
}

if (welcomeMsg.textContent != "Welcome, ") {
  form.style.display = "none";
  welcomeMsg.style.display = "block";
}