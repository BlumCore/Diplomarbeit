
const interval = setInterval(function() {
    const url = "http://127.0.0.1:5000/getItem"
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
    })
  }, 500);
