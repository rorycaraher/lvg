function generateRandomNumbers() {

    const numbers = Array.from({length: 8}, (_, i) => i + 1);
    
    // Shuffle the array to randomize the order
    for (let i = numbers.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
    }
    
    // Select the first 3 elements from the shuffled array
    const selectedNumbers = numbers.slice(0, 3);
    
    // Assign each selected number a random value between 0 and 1
    const lvg_values = selectedNumbers.map(num => ({
        number: num,
        value: Math.random()
    }));

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/save_numbers", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ lvg_values: lvg_values }));
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert("Generated values: " + lvg_values.join(", ") + " and pushed to Pub/Sub.");
        } else {
            alert("Failed to push lvg_values to Pub/Sub.");
        }
    };
}
