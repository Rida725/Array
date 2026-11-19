import sys

# Get scores from command-line arguments
scores = list(map(int, sys.argv[1:]))

total_score = sum(scores)
average = total_score / len(scores)

maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum of Scores:", total_score)
print("Average of Scores:", average)
print("Maximum Score:", maximum)
print("Minimum Score:", minimum)
          