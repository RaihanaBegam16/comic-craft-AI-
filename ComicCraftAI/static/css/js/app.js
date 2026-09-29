const form = document.getElementById("comicForm");

const button = document.getElementById("generateButton");

const loading = document.getElementById("loading");


if (form) {

    form.addEventListener("submit", function () {

        button.disabled = true;

        button.innerText = "⏳ Creating Comic...";

        if (loading) {
            loading.classList.remove("hidden");
        }

    });

}