let stockChartInstance = null;

// Fetch live stock stats
function getStockData() {
    const symbol = document.getElementById('stockSymbol').value.trim();
    if (!symbol) {
        alert('Please enter a stock symbol!');
        return;
    }

    fetch(`/stock_data/${symbol}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('stockData').innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                const format = (arr, prefix = '') => Array.isArray(arr) ? arr.join(', ') : `${prefix}${arr}`;

                const stockInfo = `
                    <h3>${data.symbol} - ${data.timestamp}</h3>
                    <p><strong>Open:</strong> $${format(data.open)}</p>
                    <p><strong>High:</strong> $${format(data.high)}</p>
                    <p><strong>Low:</strong> $${format(data.low)}</p>
                    <p><strong>Close:</strong> $${format(data.close)}</p>
                    <p><strong>Volume:</strong> ${format(data.volume)}</p>
                `;
                document.getElementById('stockData').innerHTML = stockInfo;
            }
        })
        .catch(error => {
            document.getElementById('stockData').innerHTML = `<p>Error fetching data: ${error}</p>`;
        });
}

// Fetch portfolio recommendation
function getPortfolioRecommendation() {
    const riskProfile = document.getElementById('riskProfile').value;

    fetch(`/portfolio/${riskProfile}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('portfolioRecommendation').innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                document.getElementById('portfolioRecommendation').innerHTML = `<h3>Recommendation: ${data.recommendation}</h3>`;
            }
        })
        .catch(error => {
            document.getElementById('portfolioRecommendation').innerHTML = `<p>Error fetching data: ${error}</p>`;
        });
}

// SHAP visualization
function getSHAPExplanation() {
    fetch('/explain')
        .then(response => {
            if (response.ok) {
                document.getElementById('shapImage').src = '/static/shap_plot.png?' + new Date().getTime();
                document.getElementById('shapImage').style.display = 'block';
            } else {
                alert("Failed to fetch SHAP explanation.");
            }
        })
        .catch(error => {
            alert("Error: " + error);
        });
}
