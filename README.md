# **Portfolio Optimisation**

## Table of Contents

- [Introduction](#introduction)
- [Why have I made this?](#why-have-i-made-this)
- [Optimisations/Features](#optimisationsfeatures)
- [What have I learnt from this?](#what-have-i-learnt-from-this)
- [Improvements to be made](#improvements-to-be-made)
- - [File Structure](#file-structure)
- [How to use this?](#how-to-use-this)

## Introduction
This repository contains a detailed look into the key concepts and ideas behind the infamous Modern Portfolio Theory by Harry Markowitz. Here we will:
1) Explain the fundamental idea of balancing risk and reward when it comes to optimising a portfolio.
2) Provide various ways of calculating expected return and covariances between assets.
3) Construct a detailed Efficient Frontier plot.
4) Derive and implement various strategies to find a set of weights that optimise a portfolio, such as minimising risk and maximising sharpe ratio.
5) Having found a set of weights, we will derive and implement a way to translate this into finding the optimal allocation of shares for each asset.
6) Provide code to produce a full set of results for different strategies and respective plots.

## Why have I made this?
This project was made in order to be a helping hand in order to better understand the derivations of Markowitz's ideas. I found myself in a position where I needed to find the best way to spread an investment across various assets in order to build my own unsupervised learning trading algorithm, and upon researching this topic I found that many resources online simply stated the optimisation problem without detailed reasoning. Moreover, many simply leave the problem as such, simply finding a set of optimal weights for a given strategy. I wanted to take this a step further and translate this to the real world by finding an optimal set of allocated shares for a given investment amount.

## Optimisations/Features

I have implemented the following features:
- Various ways to calculate expected returns such as with a CAPM
- Various ways to calculate covariances between assets such as via Ledoit-Wolf Shrinkage Estimator
- 3 main strategies that one could optimise a portfolio for
- A way to translate a set of weights into a set of allocated shares to invest in
- Plots for covariances and correlations between assets, detailed full Efficient Frontier, weights and allocations
- A full set of results of multiple strategies, its returns, volatilities, sharpe ratios, weights and allocations

I have also optimised this by allowing for shorting of assets and custom constraints.

## What have I learnt from this?

From researching and writing this myself, I have learnt the importance of optimising a portfolio as to manage the trade-off between risk and reward, the notion of diversification, and optimisation techniques whether it be numerical or analytical. Moreover, this has allowed me to hone my technical skills using Python, and libraries such as NumPy, Pandas and CvxPy. 

This also makes me confident in my ability to transfer this into my unsupvervised learning trading algorithm, to allocate an investment amount across various assets.

## Improvements to be made

- I could aim to implement and develop a custom optimiser using gradient-based methods, without relying on cvxpy
- I could also implement a strategy to maximise the Treynor ratio

## File Structure
This repository is split into 2 folders, one containing all notebooks pertinent to acting as an educational tool and to learn in detail about Portfolio Optimisation. The second contains all the code necessary to run the full optimisation process for any given price data.

Notebooks:
- *Analytic Derivation of Efficient Frontier* explains how instead of relying on numerical optimisation techniques through the CvxPy library, we can analytically solve the optimisation problem through some matrix manipulation
- *Introduction to Modern Portfolio Theory* provides an introduction to the theory in its entirety, how to derive the optimistaion problem for various strategies and how we can translate this into finding optimal allocations of shares for each asset
- *MPT Code Implementation* shows how one could implement these ideas into code and gives a step by step explanation for how to do so
- *MPT Full Example* gives a firsthand example of how to use the code provided to fully optimise a portfolio

Code:
- *Price Data .csv Files* are historical price datasets for DJIA and S&P500
- *Individiual_Functions* contains all functions outside of classes for clarity
- *allocations* translates a set of weights into a set of allocated shares to invest in
- *mpt_full_example* provides a template as to how to run all the code on a sample price dataset
- *plotting* contains all the plotting functions for Efficient Frontier, covariances, weights and etc
- *portfolio_optimisers* has all the code for optimising for a particular strategy
- *portfolio_params* contains various ways to calculate expected returns and covariances between assets
- *results* has a function which returns a full set of results for various strategies

## How to use this?

Firstly, I advise going through the Jupyter Notebooks to understand the derivation and reasoning behind this theory and also how I have gone about implementing the code for it. Then, one could use the *mpt_full_example* file to see how to use the code provided on any price dataset.

Please ensure the necessary libraries have been imported, the full list can either be seen at the start of the Python file or the top of the notebooks.

