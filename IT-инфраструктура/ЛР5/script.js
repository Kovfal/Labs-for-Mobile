document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = event.target;
    let isFormFilled = true;

    for (let element of form.elements) {
        if (element.required && !element.value.trim()) {
            isFormFilled = false;
            break;
        }
    }

    if (!isFormFilled) {
        alert('Перепроверьте правильность заполнения полей.');
    } else {
        form.reset();
        const successMessage = document.getElementById('successMessage');
        successMessage.style.display = "block";
        setTimeout(function() {
            successMessage.style.display = "none";
        }, 3000);
    }
});

document.getElementById('clearButton').addEventListener('click', function() {
    document.getElementById('registrationForm').reset();
});

