$(document).ready(function () {
    $(".rating-star").on("click", function () {
        var rating = $(this).data("value");
        $("#rating-input").val(rating);
        $(".rating-star").each(function (index) {
            if (index < rating) {
                $(this).addClass("selected");
            } else {
                $(this).removeClass("selected");
            }
        });
    });

    $("#review-form").on("submit", function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: $(this).serialize(),
            success: function (response) {
                if (response.success) {
                    // Перезагрузить страницу после успешной отправки отзыва
                    location.reload();
                } else {
                    alert("There was an error: " + response.errors);
                }
            },
            error: function (response) {
                alert("An error occurred. Please try again.");
            },
        });
    });
});
