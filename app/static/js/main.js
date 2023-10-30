// Update the label of the file input with the selected filename
$('.custom-file-input').on('change', function() {
    let fileName = $(this).val().split('\\').pop();
    $(this).next('.custom-file-label').addClass("selected").html(fileName);
});

document.querySelector("form").addEventListener("submit", function(event){
    event.preventDefault();

    // Show the modal
    document.getElementById("recognitionModal").style.display = "block";

    // Simulate the processing time
    setTimeout(function() {
        document.getElementById("recognitionModal").style.display = "none";

        // Redirect based on results if needed
    }, 5000); // e.g., after 5 seconds
});
