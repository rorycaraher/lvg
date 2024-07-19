function generateRandomNumbers() {
    const numbers = Array.from({ length: 4 }, () => (Math.random() * 0.3 + 0.7).toFixed(2));
    alert("Generated numbers: " + numbers.join(", "));
}
