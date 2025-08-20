from sklearn.cluster import KMeans
import numpy as np

# Example: Dummy user risk profiles for clustering (age, income)
user_data = np.array([
    [30, 50000],  # User 1: age 30, income 50k
    [25, 45000],  # User 2: age 25, income 45k
    [40, 70000],  # User 3: age 40, income 70k
    [35, 60000],  # User 4: age 35, income 60k
    [60, 80000],  # User 5: age 60, income 80k
    [50, 65000]   # User 6: age 50, income 65k
])

# Create and fit KMeans model for clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(user_data)

# Map cluster labels to detailed risk categories
cluster_to_risk = {
    0: 'Low Risk - Bonds & Stable Stocks',
    1: 'Moderate Risk - Balanced Portfolio',
    2: 'High Risk - Stocks & Crypto'
}

def generate_portfolio_recommendations(risk_profile):
    risk_profile = risk_profile.strip().lower()

    if risk_profile == 'low':
        return {
            'recommendation': cluster_to_risk[0],
            'allocation': {
                'Government Bonds': '40%',
                'Corporate Bonds': '20%',
                'Index Funds': '25%',
                'Blue-Chip Stocks': '15%'
            }
        }
    elif risk_profile == 'moderate':
        return {
            'recommendation': cluster_to_risk[1],
            'allocation': {
                'Index Funds': '40%',
                'Blue-Chip Stocks': '30%',
                'ETFs': '20%',
                'Gold': '10%'
            }
        }
    elif risk_profile == 'high':
        return {
            'recommendation': cluster_to_risk[2],
            'allocation': {
                'Growth Stocks': '50%',
                'Emerging Market ETFs': '30%',
                'Cryptocurrency': '15%',
                'Cash Reserve': '5%'
            }
        }
    else:
        return {
            'error': 'Invalid risk profile. Please choose from "low", "moderate", or "high".'
        }

# Example usage
if __name__ == '__main__':
    print(generate_portfolio_recommendations('low'))
    print(generate_portfolio_recommendations('moderate'))
    print(generate_portfolio_recommendations('high'))
