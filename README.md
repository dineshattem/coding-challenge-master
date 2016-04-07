Insight Data Engineering - Coding Challenge
===========================================================
Used Python: 3.4.3 for programming. Source file averge_degree.py is located in ./src. result is created in the output file inside ./tweet_output.
[Graph Creation]
If we have a pair of hash tags like #A and #B. I create a graph by dictionary adding both A and B as keys and A <-> B , B<->A as edges as graph = { 'A':'B', 'B':'A' }.
If there are more than two hashtags then we create edges by combination of the hashtags without replacement. For example: we have hashtags #C, #D, #E in the new tweet. Now combinations are (#C,#D), (#D,#E), (#C, #E) and each of these pairs are added to the graph as explained above.
