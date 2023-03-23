let mouse_pos = document.querySelector(".mouse_pos")


window.addEventListener("mousemove", function (ev) {
    mouse_pos.textContent = `x=${ev.x} y=${ev.y}`
})


alert("Окно с информацией")
age = prompt("Укажите возраст: ")
let is_ = confirm("Вам больше 18?")

if (is_ && age < 18) {
    setInterval(function (e) {
        document.body.style.backgroundColor = "red";
    }, 1000)
    setTimeout(function (e) {
        setInterval(function (e) {
            document.body.style.backgroundColor = "white";
        }, 1000)
    }, 500)
}
