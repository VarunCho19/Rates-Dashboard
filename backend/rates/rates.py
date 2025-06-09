from fredapi import Fred
import os
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from fastapi import FastAPI

# Load environment variables from .env file
#load_dotenv()
api_key = "f1578e7f7117865b1306f5c8a89d2e4e"
#print(f"Using FRED API key: {api_key}")

def get_yields():
    fred = Fred(api_key=api_key)
    terms = {
        "1M": "DGS1MO",
        "3M": "DGS3MO",
        "1Y": "GS1",
        "5Y": "GS5",
        "10Y": "GS10",
        "30Y": "GS30"
    }
    print("Fetching yields from FRED...")
    yield_curve = {k: fred.get_series(v).iloc[-1] for k, v in terms.items()}
    print("Yields fetched successfully.")
    return yield_curve
    

def plot_yield_curve(yield_curve):
    current_date = datetime.today().strftime('%Y-%m-%d')
    plt.style.use('seaborn-darkgrid')
    colors = plt.get_cmap('tab10')
    terms = list(yield_curve.keys())
    yields = list(yield_curve.values())

    plt.figure(figsize=(10, 6))
    plt.plot(terms, yields, marker='o')
    plt.title('US Treasury Yield Curve')
    plt.xlabel('Maturity')
    plt.ylabel('Yield (%)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


app = FastAPI()

@app.get("/yields")
def read_yields():
    return get_yields()


