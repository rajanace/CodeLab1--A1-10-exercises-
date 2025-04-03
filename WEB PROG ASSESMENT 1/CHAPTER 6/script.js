// Function to calculate the total cost
function calculateTotal() {
    // Get input values
    const costPerLiter = parseFloat(document.getElementById('petrolCost').value);
    const liters = parseFloat(document.getElementById('liters').value);

    // Calculate total cost
    const totalCost = costPerLiter * liters;

    // Display result with 2 decimal places
    document.getElementById('result').textContent = 
        `$${totalCost.toFixed(2)}`;
} 