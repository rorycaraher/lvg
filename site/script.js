function generateRandomNumbers() {
    const numbers = Array.from({ length: 4 }, () => (Math.random() * 0.4 + 0.6).toFixed(2));
    alert("Generated numbers: " + numbers.join(", "));
}
