Khan Academy "Infection" Model
============

## Run me

1. If you do not already have `networkx`, please install using `pip install networkx`.
2. Run total infection with `python total_infection.py`. You will see a (fake) list of users and be prompted for the name of the first infection.
3. Run limited infection with `python limited_infection.py`

## EDA

Is the coaching network 'small-world' or 'scale free'? Given a dataset, I would first plot a histogram of node degree (number of links) across all the entire graph of users in the sample and determine whether the distribution was closer to a bell curve or a power law. This result would inform design choices for the limited infection procedure.

## Summary

I've described my approach to the infection problem below. During the process of writing my code and thinking through possible strategies, I compiled a "data wishlist" - salient user information for the problem at hand. My solutions are predicated on the existence and availability of this data!

## Part I: Infect

Users are represented by the User class in `user.py`. Users are the nodes / vertices of coaching graphs (Graph class in `user.py`). The graph can be constructed from an edge list (list of coach-student liaisons). For testing and demo purposes, I made a dummy edge list file and placed it in `edges.csv` For expediency I have assumed

## Part II: Limited Infection

The first way to limit spread is simply to choose not to infect users with many coaches, students or both, restricting release of the B version relatively isolated nodes.

However, if we were testing a new feature through A-B testing we might want equal proportions of users to see site A and site B, and limiting to isolated nodes is unrealistic (a tradeoff, however, is that infection-based sampling compromises the integrity of the A-B test because it is no longer truly random.) A slightly more nuanced approach with the tradeoff that mismatches may sometimes occur would be to stop the spread at "dead nodes"

Given that the objective in the limited infection scheme is to minimize the risk of a coach-student pair seeing different sites, I implemented "infection containment" using edge weighting. 

## Scalability & Questions

KA is estimated to have 6 million users a month - what proportion of these are classroom-based, lone users

## Extras

###Data wishlist:

1. Total number of minutes spent on KA within the last X days/weeks/months for any given student-coach pair (to gauge whether the pair is active - targeting inactive users as stopping points for the infection minimizes the risk of a site version mismatch). This activity window could be determined by the average length of an AB test.

2. Aggregate number of logins for a coach-student pair.

Logins * minutes spent on KA

(Many logins but short visits are not as strong of an indicator of engagement and volume of use.)

3. Interactions: weight edges by total hours spent *together* (affinity). That way, if two users are active independently but use the site together infrequently, it might be okay to stop the infection from spreading at that node. (Fraction of total time spent on site during which user is working on an assigned playlist.)

4. Should playlist length factor into edge weighting?

I've written a function to transform this hypothetical data into an edge list with weights.
