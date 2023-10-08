const dot = document.getElementById("dot");
const heart = document.getElementById("heart");

const interval = setInterval(function() {
    const url = "http://127.0.0.1:5000/getItem"
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
        dot.style = "--x: " +  json.device_data.yacc + "; --y:" + json.device_data.yacc + ";";
        heart.innerHTML = json.device_data.heartrate

    })
  }, 500);
