// script.js

function getRecommendation() {
    const userId = document.getElementById('userIdInput').value;
    const resultDiv = document.getElementById('recommendationResult');

    if (!userId) {
        resultDiv.innerHTML = "Please enter a valid User ID.";
        return;
    }

    // Simulated response from Python backend
    const recommendations = {
        1: "Recommended Products: Smartwatch, Wireless Earbuds, Fitness Tracker",
        2: "Recommended Products: Gaming Laptop, Noise Cancelling Headphones, RGB Keyboard",
    };

    resultDiv.innerHTML = recommendations[userId] || "No preferences found for this User ID.";
}