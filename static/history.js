const rows = document.querySelectorAll(".clickable-row")
const dot = document.getElementById("dot")

console.log(rows)
rows.forEach((row) => {
    row.addEventListener("click", function(){
        console.log(row.children[0])
        dot.style = "--x: " +row.children[0].innerHTML + "; --y: " +row.children[1].innerHTML + ";"
    })
});
