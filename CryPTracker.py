import requests
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Solarized Dark color scheme
bg_color = "#002b36"  # Background color
fg_color = "#839496"  # Foreground color (base0)
accent_color = "#b58900"  # Accent color (yellow)pyi
text_color = "#93a1a1"  # Text color

# Function to retrieve cryptocurrency price
def get_price():
    crypto = crypto_entry.get()
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data[crypto]['usd']
    price_label.config(text=f"Price: ${price:.2f}")

# Function to retrieve historical data (e.g., past 7 days) and display it in a chart
def get_historical_data():
    crypto = crypto_entry.get()
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days=7"
    response = requests.get(url)
    data = response.json()
    prices = [point[1] for point in data['prices']]
    historical_data_label.config(text=f"Last 7 days prices: {', '.join(map(str, prices))}")

    # Create a price chart with Solarized Dark colors
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(prices, label=f'{crypto} Price', color=accent_color)
    ax.set_facecolor(bg_color)
    ax.set_title(f'{crypto} Price Chart', color=text_color)
    ax.set_xlabel('Days', color=text_color)
    ax.set_ylabel('Price (USD)', color=text_color)
    ax.tick_params(axis='x', colors=text_color)
    ax.tick_params(axis='y', colors=text_color)
    ax.legend(loc='best', fontsize=10, frameon=False, labelcolor=text_color)

    # Embed the chart in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

# Create a GUI window with Solarized Dark theme
app = tk.Tk()
app.title("CryPTracker")
app.geometry("600x400")  # Larger window size
app.config(bg=bg_color)

crypto_label = tk.Label(app, text="Enter Cryptocurrency:", fg=text_color, bg=bg_color, font=("Arial", 12))
crypto_label.pack()

crypto_entry = tk.Entry(app, font=("Arial", 12))
crypto_entry.pack()

price_button = tk.Button(app, text="Get Price", command=get_price, bg=accent_color, font=("Arial", 12))
price_button.pack()

price_label = tk.Label(app, text="", fg=text_color, bg=bg_color, font=("Arial", 12))
price_label.pack()

historical_data_button = tk.Button(app, text="Get Historical Data and Chart", command=get_historical_data, bg=accent_color, font=("Arial", 12))
historical_data_button.pack()

historical_data_label = tk.Label(app, text="", fg=text_color, bg=bg_color, font=("Arial", 12))
historical_data_label.pack()

app.mainloop()
