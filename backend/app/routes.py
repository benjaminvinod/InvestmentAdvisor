from flask import Blueprint, jsonify, render_template, send_file
from datetime import datetime
from .live_data import get_daily_stock_data, get_intraday_stock_data
from .portfolio_optimizer import generate_portfolio_recommendations
from .models import generate_shap_plot

main = Blueprint('main', __name__)

# Home route
@main.route('/')
def index():
    return render_template('index.html')

# Stock data route including both intraday and daily
@main.route('/stock_data/<symbol>', methods=['GET'])
def stock_data(symbol):
    daily = get_daily_stock_data(symbol)
    intraday = get_intraday_stock_data(symbol)

    if not daily or not daily.get("open") or not intraday or not intraday.get("open"):
        return jsonify({"error": "No data available for the given symbol"}), 404

    response = {
        "symbol": symbol.upper(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "daily": {
            "open": daily.get("open", []),
            "high": daily.get("high", []),
            "low": daily.get("low", []),
            "close": daily.get("close", []),
            "volume": daily.get("volume", [])
        },
        "intraday": {
            "open": intraday.get("open", []),
            "high": intraday.get("high", []),
            "low": intraday.get("low", []),
            "close": intraday.get("close", []),
            "volume": intraday.get("volume", [])
        }
    }

    return jsonify(response)

# Portfolio recommendation route
@main.route('/portfolio/<risk_profile>', methods=['GET'])
def portfolio(risk_profile):
    try:
        portfolio = generate_portfolio_recommendations(risk_profile)
        return jsonify(portfolio)
    except Exception as e:
        return jsonify({"error": f"An error occurred while generating portfolio recommendations: {str(e)}"}), 500

# SHAP explanation plot route
@main.route('/explain', methods=['GET'])
def explain():
    try:
        plot_path = generate_shap_plot()
        return send_file(plot_path, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": f"An error occurred while generating SHAP plot: {str(e)}"}), 500
