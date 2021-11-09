let global_couter = 0

function Function(qualifiedName, value) {
    if (global_couter < 10) {
        let objTo = document.getElementById('poll');
        let x = document.createElement("input");
        x.setAttribute("type", "text")
        x.setAttribute("name", "question" + global_couter)
        x.setAttribute("placeholder", "your question");
        objTo.appendChild(x);
        global_couter += 1
    }
    else {
        alert("maximum questions in poll is reached!")
    }
}