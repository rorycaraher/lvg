function generateRandomNumbers() {
    const numbers = Array.from({ length: 4 }, () => Math.random().toFixed(2));
    alert("Generated numbers: " + numbers.join(", "));
}
