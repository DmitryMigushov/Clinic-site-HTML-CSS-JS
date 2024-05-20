function subscribe() {
    alert("Нажата кнопка подписаться (через on_click), меняем цвет текста на красный");
    document.querySelector(".black-but").style.color = "red";
}

function fun2() {
    alert("Нажата кнопка запись (через addEventListener), меняем цвет фона одного из абзацев и текст");
    text2 = document.querySelector("#text2")
    text2.innerHTML = 'Изменный текст'
    text2.style.backgroundColor ='aqua';
}

but2 = document.querySelector("#b2")
but2.addEventListener('click', fun2)

document.addEventListener('DOMContentLoaded', () => {
    const fetchButton = document.getElementById('fetchButton');
    const dogImage = document.getElementById('dogImage');

    fetchButton.addEventListener('click', () => {
        fetch('https://dog.ceo/api/breeds/image/random')
            .then(response => response.json())
            .then(data => {
                dogImage.src = data.message;
            })
            .catch(error => {
                console.error('Error fetching the dog image:', error);
            });
    });
});