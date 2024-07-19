function generateRandomNumbers() {
    const numbers = Array.from({ length: 4 }, () => (Math.random() * 0.4 + 0.6).toFixed(2));
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/save_numbers", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ numbers: numbers }));
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert("Generated numbers: " + numbers.join(", "));
        } else {
            alert("Failed to save numbers.");
        }
    };
}
