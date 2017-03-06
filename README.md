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

Clone the repo:

https://github.com/jhole89/twitterAnalyser.git

### Prerequisites

Python 3.5+ (https://www.python.org/downloads/)

Twitter keys

### Installing

## Running the tests

pytest <individual test>

### Break down into end to end tests

pytest <all>

### And coding style tests

PEP8

## Built With

* [Tweepy]
* [Pandas]
* [Vincent]
* [d3]

## Contributing

As I consider this project to be closed (bar a few outstanding issues that I may revisit in the future) I will not be
looking to add any additional features into this project. However if you feel like contributing then feel free to issue
Pull Requests. Any further development or Fork of this project is bound by the sample license of its parent.

## Authors

* **Joel Lutman** - *Initial work* - [jhole89](https://github.com/jhole89)

## License

This project is licensed under the GNU GPL3 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Marco - inspired by blah
* Lexicon