document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll(".rating-star");
    stars.forEach((star) => {
        star.addEventListener("click", function () {
            stars.forEach((s) => s.classList.remove("selected"));
            this.classList.add("selected");
            let value = this.getAttribute("data-value");
            // Создаем скрытое поле для передачи рейтинга в форме
            let ratingInput = document.createElement("input");
            ratingInput.type = "hidden";
            ratingInput.name = "rating";
            ratingInput.value = value;
            let form = this.closest("form");
            let existingInput = form.querySelector('input[name="rating"]');
            if (existingInput) {
                existingInput.value = value;
            } else {
                form.appendChild(ratingInput);
            }
        });
    });
});
