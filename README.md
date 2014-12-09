Khan Academy Infection Model
============

## Instructions

1. Dependencies: If you do not already have `networkx` and the latest `matplotlib`, please install with `pip install networkx` and `pip install --upgrade matplotlib`.

2. Run total and limited infection with `python total_infection.py` and `python limited_infection.py`, respectively. You will see a (fake) list of users and be prompted for the name of the first infection. Outputs a list of infected users and an image `network_infection.png`.

3. Modify or append coaching relations in `edges.csv` and `weighted_edges.csv` and rerun for fun, *ad infinitum*.


## EDA 

KA is estimated to have 6 million users a month - what proportion of these are classroom-based vs. individual (uncoached) users?

Is the coaching network 'small-world' or 'scale free'?

Given data on coaching relations, I would plot a histogram of node degree (number of links) across all users in the sample and determine whether it more closely follows a Poisson / power law / other distribution. This result would inform design choices for the limited infection model.


## Part I: Infect

Users are represented by the User class in `user.py`. Users are the nodes / vertices of coaching graph (Graph class in `user.py`). The graph can be constructed from an edge list (list of coach-student liaisons). For testing and demo purposes, I have made a dummy edge list `edges.csv`. 

## Part II: Limited Infection

The first way to limit spread is simply to choose not to infect users with many coaches, students or both, restricting release of the B version relatively isolated nodes (the threshold for this is subjective.)

However, if we were testing a new feature through A/B testing we might want equal proportions of users to see site A and site B, and limiting to isolated nodes is unrealistic (a tradeoff, however, is that infection-based sampling compromises the integrity of the A/B test because it is no longer truly random.)

A slightly more nuanced approach would be to stop the spread at "dead nodes" (with the tradeoff that mismatches may sometimes occur):

Given that the objective in the limited infection scheme is to minimize (but perhaps not eliminate) the risk of a coach-student pair seeing different sites, I implemented "infection containment" in `limited_infection.py` using edge weighting, with dummy data in `weighted_edges.csv`.


#### Edge weighting scheme:

Several of these weighting schemes are predicated on the availability of salient user information for the problem at hand.

__Time weighting__: Total number of minutes spent on KA within the last X days/weeks/months for any given student-coach pair (to gauge whether the pair is active - targeting inactive users as stopping points for the infection minimizes the risk of a site version mismatch). This activity window should be scaled to the average length of an A/B test.

__Aggregate number of logins__ for a coach-student pair.

Logins * minutes spent on KA

(Many logins but short visits are not as strong of an indicator of engagement and volume of use.)

__Affinity__: weight edges by total hours spent *together*. That way, if two users are active independently but use the site together infrequently, it might be okay to stop the infection from spreading across that edge. (Fraction of total time spent on site during which user is working on an assigned playlist from a given coach.)

## Ideas for extensions

Create an interactive visualization dashboard with D3.js that would allow you to click on a node and see the spread of the infection for different threshold values of metrics discussed above. One could "tune" parameters by use-case. 