# **Portfolio-Optimisation**

## Table of Contents

- [Introduction](#introduction)
- [Why have I made this?](#why-have-i-made-this)
- [File Structure](#file-structure)
- [Optimisations/Features](#optimisationsfeatures)
- [What have I learnt from this?](#what-have-i-learnt-from-this)
- [Improvements to be made](#improvements-to-be-made)
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
- *allocations* 

## Optimisations/Features
I have implemented the following features:
- 


- I have managed to implement a K-Means++ approach to initialising the first $k$ centroids. This is where the first centroid is chosen uniformly at random from the data points that are being clustered, after which each subsequent centroid is chosen from the remaining data points with probability proportional to its squared distance from the point's closest existing centroid.<br> Although this takes greater time to initialise, it significantly reduces the time to run the actual K-Means Clustering Algorithm. Hence overall, this is a optimisation in the long run.
- An issue with the Voronoi Diagram implementation through the SciPy library is that each regions does not necessarily correspond to its respective centroids and clusters and thus, the colours will be different. I have managed to amend this, allowing for greater visualisation since we can easily colour the regions and data points within a cluster the same.

## What have I learnt from this?


Instead of simply importing libraries and running pre-existing functions, I have thorougly understood how this algorithm works and I feel I am able to incorporate this way of thinking into other machine learning methods.

I have also learnt the importance and use cases of clustering stocks for portfolio management.

Moreover, I have learnt about the existence of Voronoi Diagrams and how useful they can be in visualising data. To further this, I have come across a very interesting problem surrounding these diagrams: "In a Voronoi Diagram with $n$ uniformly chosen sites, what is the average perimeter of a random region in terms of $n$?".

## Improvements to be made


- I could store all iterations of centroids, such that I can plot a Voronoi Diagram for each iteration and iteratively see the change each time. For now, I have only plotted the start and end iterations. However, with the K-Means++ implementation, only a few iterations are required for most datasets.
- I have stored my distances in a dataframe when implementing K-Means++, in order to tabulate and display distances, however this is not necessary. So to save time and computation, I should instead store them in simple numpy arrays.
- I would like to implement other clustering methods that can deal with non-spherical data better and also avoid clustering spherically.

## How to use this?


Firstly, I advise going through the Jupyter Notebooks to understand how the algorithm works and for a step by step methodology. Then, one could use the Python file provided on the .csv datasets provided or alternatively use any 2 dimensional data. I have only included the code for the actual clustering of data points and not the visualisation since this is not necessary, it is simply a visual aid to see how the algorithm works.

Please ensure the necessary libraries have been imported, the full list can either be seen at the start of the Python file or the top of the notebooks.

