## Meta Labeling

**Models taken into consideration:**
------------------------------------

A. Moving Average Crossover Stragegy: When the short term moving average crosses above the long term moving average, that indicates a positive trend, and hence a buy. If it crosses from the top down, it is a short signal.

B. Minervini Trend Filter

C. Hedgefundie's Ultimate Adventure

D. Antonacci Dual Momentum

E. Radge ADX Day Trade

F. Radge BBO

G. Radge Weekend Trend Trader

H. Bensdorp books

I. Connors' 7 day high/low

**Figure 1. Meta Labeling Architecture See third reference for additional details.**




## openbb-terminal-cron
-----------------------

schedule cron job to download plots from openbb, upload to static s3 website

```{python}
install openbb

opeb openbb
```

run daily

**Futures** 
-----------

```{python}
historical --ticker BTC
```

![bitcoin](https://user-images.githubusercontent.com/13305262/222621891-d4bd69b0-1963-4534-8ddd-7dce0730427b.png)

```{python}
historical --ticker ETH
```

![ether](https://user-images.githubusercontent.com/13305262/222621907-f0187ff1-4c54-4796-bd28-f9d1dc95327b.png)

**Ice us dollar index**
![us_dollar](https://user-images.githubusercontent.com/13305262/222622195-c6d82111-b793-471a-a27c-cd09d9a11442.png)

**Yen**

![yen](https://user-images.githubusercontent.com/13305262/222622265-7bd7ff07-b7fb-4e44-a0b6-561d6271a0ee.png)



save plots

upload to s3

email completion message

```{python}

```
