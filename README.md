# Graphics Card Prices

## Goals

The goal of this project was to investigate the relationship between a graphics card's price and it's specs; to gain insight into the dataset and to use machine learning to build a predictive model.
The could be useful information for consumers looking to buy a new card. They can decide what specs they need and see what price they can expect.

The data was scraped from www.newegg.com using web_scrape.py, which uses the BeatifulSoup package for html parsing. The project involves data cleaning, exploratory data analysis, data visualisation and predictive modelling. I am using Pandas, NumPy, Seaborn and Sci-kit Learn.

## Key Findings

Notebook.ipynb gives a more in depth exploratory data analysis, but some of the key findings are:

Alot of the variables are highly correlated. This is not surpising since a card is only as good as it's weakest part. When NVIDIA releases a new card all of the spec are improved, most of the specs are improved.

The most relevant features that affect price are number of CUDA Cores, the chip series and the memory size/interface. These are definitely features that are considered by consumers when looking for a card.

Surprisingly clock speed had a low correlation with price. Intuatively this seems like it would be important but must cards have a simialr speed around 1800 MHz. The data suggests that other features are more important.

There were a few outliers with lower specs but high price, I think that these are just older graphics cards that have retained their value. They were removed from the model as they are not in line with current cards.

## The model

I used a Random Forest Regressor and split the data into train/test data with a 80/20 split. The model had a root mean squared error of £30 on the test data, on a price range of £550.
I think this is quite good, but could be improved, the main limitation is that the sample size after removing outliers was 107, which is smaller than desired. 
