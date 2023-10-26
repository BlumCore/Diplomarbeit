const rows = document.querySelectorAll(".clickable-row")
const dot = document.getElementById("dot")
const heart = document.getElementById("heart_label")
let active = ""
rows.forEach((row) => {
    row.addEventListener("click", function(){
        if(active != ""){
            active.classList.remove("active")
        }
        row.classList.add("active")
        active = row
        dot.style = "--x: " +row.children[0].innerHTML + "; --y: " +row.children[1].innerHTML + ";"
        heart.innerHTML = row.children[2].innerHTML;
    })
});
