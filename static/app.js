function validateForm() {
    let inputs = document.querySelectorAll('input[type="text"]');
    
    for (let i = 0; i < inputs.length; i++) {
        let input = inputs[i];
        let value = input.value.trim();
        
        if (value.length < 3) {
            alert('Please provide answers with at least 3 characters.');
            return false;
        }

        if (value !== value.toLowerCase()) {
            alert('Please use lowercase letters only.');
            return false;
        }
    }

    return true;
}