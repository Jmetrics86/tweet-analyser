# Tweet Analyser

Tweet Analyser is a Python3 implementation of NLP (Natural Language Processing) on Twitter data.
It is a Proof of Concept aimed to discover hidden facts about Tweets using simple counting, aggregations,
and semantic orientation.

Data is sourced from Twitter using their own API interfaced with the Tweepy python package.
At a tweet level we can look at frequency of tweets to discover trend patterns of a user or hashtag, however what we
are really interested in is whats inside those Tweets.  We process the data to reduce tweets down to each term
(we use term instead of word as a term can also be a hashtag, numeric, or emoji) whereby from this point we can easily
uncover some interesting insights.  By simply counting and aggregating we can find out the top terms, hashtags, and
pairs of terms that are being used, giving us an indication of what the Tweets are talking about.  Finally we take this
one step further and use semantic orientation and pointwise-mutual-information to ascertain how positive, negative or
neutral each term is.

## Getting Started

### Prerequisites

* [Python 3.5+](https://www.python.org/downloads/)

* [Twitter OAuth access tokens](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)

### Installing

1. Install Python3 on your Operating System as per the Python Docs. Continuum's Anaconda distribution is recommended.

2. Clone the repo: `git clone https://github.com/jhole89/tweet-analyser.git`

3. Create a credentials.properties file based on the template in src/resources with your Twitter OAuth consumer and
access tokens as per the prerequisites

4. Set the environment: `pip install -r requirements.txt`

5. From tweet-analyser/src run the application: `python main.py`

## Running the tests

We use PyTest as our test framework

### Test Coverage

pytest <all>

### Coding style

Tweet Analyser is PEP8 complaint but uses a max-line-length=100.  This can be checked from the command line with:
```unix
pep8 --statistics --max-line-length=100 twitterAnalyser
```

## Built With

* [Python3](https://www.python.org/downloads/) [(Anaconda)](https://www.continuum.io/downloads)
* [Tweepy](https://github.com/tweepy/tweepy)
* [Pandas](http://pandas.pydata.org/)
* [PyTest](http://doc.pytest.org/en/latest/)
* [Vincent](https://vincent.readthedocs.io/en/latest/)
* [d3.js](https://d3js.org/)

## Contributing

As I consider this project to be closed (bar a few outstanding issues that I may revisit in the future) I will not be
looking to add any additional features into this project. However if you feel like contributing then feel free to issue
Pull Requests. Any further development or Fork of this project is bound by the sample license of its parent.

## Authors

* **Joel Lutman**

## License

This project is licensed under the GNU GPL3 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* We make use of the excellent [Opinion Lexicon](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon) by Minqing Hu and Bing Liu - <i>Mining and Summarizing Customer Reviews (KDD-2004)</i>
* This piece of work was inspired by the work of Marco Bonzanini's <i>[Mining Twitter Data with Python](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)</i>
