async function fetchCryptoPrices() {
    try {
        const response = await fetch("/crypto-prices");  // Fetch data from FastAPI
        const data = await response.json();

        let tickerContent = "";
        for (const [coin, price] of Object.entries(data)) {
            tickerContent += `<p>${coin.toUpperCase()}: $${price.usd}</p>`;
        }

        document.getElementById("crypto-ticker").innerHTML = tickerContent;
    } catch (error) {
        console.error("Error fetching crypto prices:", error);
        document.getElementById("crypto-ticker").innerHTML = "<p>Failed to load data</p>";
    }
}

// Fetch prices every 30 seconds
setInterval(fetchCryptoPrices, 30000);

// Initial fetch on page load
fetchCryptoPrices();
