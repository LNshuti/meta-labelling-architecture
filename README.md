## Meta Labeling

Deploy a full stack application that automatically downloads live Bitcoin prices from an exchange such as CoinmarketCap. Use Advanced ML forecasting methods to build a trading strategy based on ensemble modeling. Backtest strategy. 

Disclaimer: This is for Educational Purposes Only. 

**Models taken into consideration:**
------------------------------------

* Moving Average Crossover Strategy: When the short-term moving average crosses above the long-term moving average, that indicates a positive trend and hence a buy. If it crosses from the top down, it is a short signal.

* Minervini Trend Filter

* Hedgefundie's Ultimate Adventure

* Antonacci Dual Momentum

* Radge ADX Day Trade

* Radge BBO

* Radge Weekend Trend Trader

* Bensdorp books

* Connors' 7 day high/low

**Figure 1. Meta Labeling Architecture.**

![image](https://user-images.githubusercontent.com/13305262/230697422-bf530fdd-dacf-455a-a63c-d8fa573abede.png)

# How to create architecture diagram using Drawio in VSCode
[here](https://www.loom.com/share/f96d2241e6b54d81a529ea2527c776ae)



# How to use the code  

```python
# Step 1: Clone the repo
https://github.com/LNshuti/meta-labelling-architecture.git

# Step 2: Create an isolated environment to manage dependencies
conda env create --file=environment.yaml

# Step 3: install required python packages

pip install -r requirements.txt
```

**References**

1. Marcos Lopez de Prado. Advances in Financial Machine Learning. Lopez de Prado, M. (2018). Advances in Financial Machine Learning. United Kingdom: Wiley.
2. Chip Huyen. Designing Machine Learning Systems. An Iteative Process for Production Ready Application. 
