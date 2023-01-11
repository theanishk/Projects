Differences in effect of real and nominal exchange rate on economic growth: case study of India
===============================================================================================

**An HSN-201 Advanced Statistics Project**

Anish Kumar - 21322006 | Param Mahabare - 21322021

Abstract
--------

The following is a study to understand the differences in the variation of real and nominal exchange rates on the GDP growth of India over the period of 2004-2019. Even though it is generally assumed that both the nominal and real exchange rate are going to have similar impact on economic growth, in this particular case, as both the rates are converging and the economy is growing, suggesting that one of rates has an inverse effect.

Literature Review
-----------------

Exchange Rate (ER) is the price of one currency in relation to another. It expresses the national currency’s quotation in respect to foreign ones (Azid et al., 2005). Compared to nominal, Real Exchange Rate (RER) is often acknowledged as an important macroeconomic policy variable in the sense that it indicates a country’s international competitiveness. The RER is the Nominal Exchange Rate (NER) adjusted for price changes (inflation) in the domestic relative to those of trading partners. The NER management depends on the RER, and the RER is influenced, among others, by NER (Montiel, 1997; and Thapa, 2002). This is due to the close correlation between real and nominal exchange rates where NER often drives the RER.

International ERs are an important indicator of the overall state of an economy. Domestic ERs, for instance, provide information about the differences in economic activity between regions and are considered as important economic barometers (Phillips and Cutler, 1998) or indicators.

Data
----

We would be using the following datasets in order to commute our results:

1.  Exchange Rate: This consists of Real and Nominal Effective Exchange Rates.
2.  Economic Growth: This consists of annual real GDP figures.

**_Real Effective Exchange Rate (REER)_**

Conceptually, the REER, defined as a weighted average of nominal exchange rates adjusted for relative price differential between the domestic and foreign countries, relates to the purchasing power parity (PPP) hypothesis. The weights are determined by comparing the relative trade balance of a country’s currency against that of each country in the index.

An increase in a nation’s REER is an indication that its exports are becoming more expensive and its imports are becoming cheaper. It is losing its trade competitiveness.

The dataset that we have considered desribes the REER using stable 2015-16 rates as base. We have used the 36 currency index that considers India’s top 36 largest partners which consitute for over 80% of trade.

**_Nominal Effective Exchange Rate (NEER)_**

The nominal effective exchange rate (NEER) is an unadjusted weighted average rate at which one country’s currency exchanges for a basket of multiple foreign currencies. The nominal exchange rate is the amount of domestic currency needed to purchase foreign currency.

The NEER is adjusted with inflation in rorder to find the REER.

The dataset that we have considered desribes the NEER using stable 2015-16 rates as base. We have used the 36 currency index that considers India’s top 36 largest partners which consitute for over 80% of trade.

**_Real GDP_**

GDP at purchaser’s prices is the sum of gross value added by all resident producers in the economy plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources. Data are in constant 2015 prices, expressed in U.S. dollars. Dollar figures for GDP are converted from domestic currencies using 2015 official exchange rates.

Method
------

Among the various methods avaiable to check for stationarity, including but not limited to: Dickey-Fuller (DF) or Augmented Dickey-Fuller  
(ADF) (Dickey and Fuller, 1979), Phillips-Perron (PP) (Phillips and Perron, 1988), and DickeyFuller-Generalized Least Square (DF-GLS) (Elliott et al., 1996), we would be using the ADF methodology to find unit roots. The optimal lag length is chosen based on the lowest SIC value.

We need to do bivariate cointegration, for that we can use ARDL bounds testing approach proposed by Pesaran et al. (2001) in order to check for the long-run movement of the variables as well as to consider the robustness of the results.

But due to limitations in our knowledge we only performed unit root test.

![GDP_NEER](https://github.com/theanishk/stat-proj/blob/main/gdp_neer.png?raw=true)  
![GDP_REER](https://github.com/theanishk/stat-proj/blob/main/gdp_reer.png?raw=true)

#### Unit Root Test Result

| **Variable** | **ADF Statistic** | **p-value** | 1%     | 5%     | 10%    |
|:------------:|:-----------------:|-------------|--------|--------|--------|
|      GDP     |     -0.168922     |   0.942126  | -3.924 | -3.068 | -2.674 |
|     NEER     |     -2.137732     |   0.229616  | -4.069 | -3.127 | -2.702 |
|     REER     |      1.664325     |   0.998038  | -4.332 | -3.233 | -2.749 |

Empirical Results
-----------------

To avoid any problem related to spurious regression and biasedness of the results because of the uncertainty, instability and stationarity problems of the time series data, we conducted unit root tests by Augmented Dickey-Fuller (ADF) method.

Our computations suggest that the data is non-stationary. This thus adds additional layers of complexities to our study which are beyond the scope of our knowlegde and hence, unfortunately we can not continue further to present any concrete conclusions.

* * *