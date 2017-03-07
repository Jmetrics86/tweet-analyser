# PrepareToTry Tweet Analysis

## Background

As an avid gamer I spend a lot of my time reading gaming articles. One of the biggest gaming websites is IGN and last
year I found myself slightly addicted to their Dark Souls Let's Play comedy series [<b>Prepare To Try</b>](http://uk.ign.com/watch/prepare-to-try)
where <i>"3 idiot friends try to beat Dark Souls while slowly losing their minds"</i>.

Around the same time I started to become interested in Natural Language Processing with Twitter and thought Prepare To
Try would make an ideal candidate for some example tweet analysis.  With tweet-analyser complete(ish) we can now do this,
and while the final output may not be as pretty as I initial hoped for (screw it, I'm a Data Scientist not a JavaScript
developer) we can still get some interesting results.

## Tweet Analysis

### Usage

<b>Prepare To Try</b> uses a couple of key terms (<i>#PrepareToTry, @PrepareToTry, #PTT, #Finchy</i>) so we instantly have a
few choices about what we want to investigate. However if we weren't familiar with the source material it wouldn't be
unusual to start with the hashtag to see whats being said about it, in this case we'll search for the offical hashtag
<i>#PrepareToTry<i>.

From the command line:
```bash
$ python src/main.py
Would you like to analyse a user timeline(1) or search a hashtag(2): 2
Please enter the hashtag to search with: PrepareToTry
Report ready to view at http://localhost:8000/report/chart.html
Report will be available for the next 5 minutes
```

As above the application asks the user whether they would like to search a user's timeline, or search for a hashtag.
Since we are decided to search for the #PrepareToTry hashtag we choose option 2, and enter PrepareToTry as the hashtag
we want to search for (we could equally have included the # in the hashtag and it wouldn't make a difference). Our
results are made available at http://localhost:8000/report/chart.html using a WebServer we spin up in the background and
is available for viewing for number minutes (you can tweek this in main.py). If we want to save these results for later
we can also save this off as a PDF document.

### Results

So now that we've processed all tweets with the #PrepareToTry hashtag let's find out what those tweets are talking about.

As a note we should differentiate between searching for a hashtag such as #PrepareToTry and a user's timeline such as
@PrepareToTry.  Searching for the #PrepareToTry hashtag will return us any tweet from any user that has posted using that
hashtag, while scanning the @PrepareToTry user timeline will return that user's timeline which usually contains only that
user's tweets.  It's a subtle but significant difference between whats been said about that hashtag, and what that user
is saying.  What we're interested at here is what's being said about #PrepareToTry, so lets head over to the
[report.](http://localhost:8000/report/chart.html)

#### Tweet Timeline

The first think we can see is the recent trend of #PrepareToTry being mentioned. We can see that there was previously
some chatter, though not much recently. A quick google of PrepareToTry will shown us that this is because the last
episode of PrepareToTry aired on the 24th February 2017 (at least, the last till the next season - fingers crossed) so
we see lots of mentions on around the 24th and a die off since, basically people are forgetting and the boys need to get
back on the air.

#### Top Terms

While looking at the timeline tells us about the overall trend of the show and it's popularity over time, it doesn't
tell us much about the context of people are saying. Instead we can look at a simple aggregation of all the terms
(words/urls/emoji's/etc) to see what terms are appearing most frequently in tweets containing the #PrepareToTry tag. To
avoid this being dominated by useless information we remove most commonly appearing words that hold little interest, such
 as "a", "the", "is", "that", etc.

 \<GRAPH HERE>

 Here we see that the most commonly appearing terms are those we would probably expect for a Dark Souls Let's Play:
 "Dark", "Souls", etc. While this gives us some idea of the context of the tweets, it ...