# Given the participants' score sheet for your University 
# Sports Day, you are required to find the runner-up score.
#  Store them in a list and find theYou are given  scores. 
#  score of the runner-up.

# Content - list  of score, runner-up finding, condition,



n = int(input("Enter the number of participants: "))


scores = list(map(int, input("Enter the scores: ").split()))


unique_scores = sorted(set(scores), reverse=True)


if len(unique_scores) > 1:
    runner_up_score = unique_scores[1]
    print("Runner-up score:", runner_up_score)
else:
    print("No runner-up exists")
