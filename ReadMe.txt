First thing i did was to make the possible functions:-
1. A function that generate all possible combination for the next move
2. Made a checkwin function
3. Made a checkDraw function
4. Combined checkDraw and checkwin function into checkEndNode function that checks if the node is leafnode.
5. Then i was hit with the thought that :-

Moment of Realisation (naah i just recalled the recursive approach of merge sort and it did help me brainstorm):-

if we are the top most parent node and starting with max, then we should call it a max-min function.
i say so because we are using first max then inside min then min inside of it uses max.

and all the very next child nodes(of top most parent node) are using min-max function.
cause they each of the child node are calling using min-max 
(like they are just calling min then inside max and so on...)

6. i created two functions minOfDictionary and maxOfDictionary 
that returns min and max value and their index from dictionary.(i will use them later, that was the thought)

7. So i created maxFunction and minFunction that calls eachother alternately and recursive
8. after doing so my tic tac toe cpu was atleast playing by itself. but

it was trying to stop me pretty good and yet it never tried to win even though it had chance.

who knows.. maybe my minmax algorithm is wrong ?? (Not being sarcastic)
Later i just thought maybe the reason is that its getting same best-value from two nodes 
and it is priortising the first one of them.

two avoid it i added the functionality that also priortize the depth.

---> lower depth = higher priority

now the games seems to work fine.


