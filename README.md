## Meta Labeling

Deploy a full stack application that automatically downloads live Bitcoin prices from an exchange such as CoinmarketCap. Use Advanced ML forecasting methods to build a trading strategy based on ensemble modeling. Backtest strategy. 

### Null Hypothesis
------------------------------------
There exists alpha in developing and deploying a custom trading bot using an ensemble model and experimenting with proprietary datasets. 

This collaborative project aims to examine this hypothesis. We will build a full-stack application following software engineering and MLOPS best practices with **the goal of disproving our null hypothesis**.  

**Team:** 
------------------------------------
* Leonce 
* Indrit 
* Dipta
* You?

**Disclaimer: This is for Educational Purposes Only.** 

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

# How to access BTC data 
We use **OpenBB Terminal**, an incredible open-source [library](https://my.openbb.co/app/sdk) that provides APIs for accessing prices, news, data, and models. A comparable commercial tool is the Bloomberg Terminal.  

Follow Installation instructions from OpenBB's [website](https://my.openbb.co/app/sdk/installation)

# How to use the code  

```python
# Step 1: Clone the repo
https://github.com/LNshuti/meta-labelling-architecture.git

# Step 2: Create an isolated environment to manage dependencies
conda env create --file=environment.yaml

# Step 3: install required Python packages

pip install -r requirements.txt

## Install the OpenBB python package from PIP
pip install openbb

# Step 4: Open openbb using the terminal command
$ openbb

# Get Historical Bitcoin Prices
$ historical --ticker BTC
```
**Commonly used Ticker mapping**
```python
| Ticker | Name         |
|--------|--------------|
| BTC    | Bitcoin      |
| ETH    | Ether        |
```

**References**

1. Marcos Lopez de Prado. Advances in Financial Machine Learning. Lopez de Prado, M. (2018). Advances in Financial Machine Learning. United Kingdom: Wiley.
2. Chip Huyen. Designing Machine Learning Systems. An Iteative Process for Production Ready Application. 
