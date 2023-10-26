const dot = document.getElementById("dot");
const heart = document.getElementById("heart");
const time = document.getElementById("time");

const interval = setInterval(function() {
    const url = "http://127.0.0.1:5000/getItem"
    const currentDate = new Date();
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        dot.style = "--x: " +  json.device_data.yacc + "; --y:" + json.device_data.yacc + ";";
        heart.innerHTML = json.device_data.heartrate
        time.innerHTML = currentDate.toLocaleTimeString();
    })
  }, 500);
