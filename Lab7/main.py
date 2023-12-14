from collections import defaultdict
import math as mt
import pandas as pd

def abs_major(votes):
    score = defaultdict(int)

    for vote in votes:
        first_choice = vote[0]
        score[first_choice] += vote[-1]

    winner = max(score, key=score.get)

    print(f"\nЗа правилом абсолютної більшості Переміг кандидат {winner} з {score[winner]} голосами\n")

def rel_major(votes):
    score = defaultdict(int)

    for vote in votes:
        first_choice = vote[0]
        score[first_choice] += vote[-1]

    half_candidates = mt.ceil(len(score) / 2)
    top_candidates = dict(sorted(score.items(), key=lambda x: x[1], reverse=True)[:half_candidates])

    if len(top_candidates) > 1:
        remaining_votes = []
        for vote in votes:
            remaining_vote = tuple(c for c in vote[:-1] if c in top_candidates)
            if remaining_vote:
                remaining_votes.append(remaining_vote + (vote[-1],))
        rel_major(remaining_votes)
    else:
        winner = list(top_candidates.keys())[0]
        print(f"За правилом відносної більшості Переміг кандидат {winner} з {score[winner]} голосами\n")


def borda_win(votes):
    candidate_scores = defaultdict(int)

    for vote in votes:
        for i, candidate in enumerate(vote[:-1]):
            candidate_scores[candidate] += vote[-1] * (3 - i)

    sort_candidates = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)

    winner, winning_score = sort_candidates[0]
    print(f"Керуючись методом Борда Переміг кандидат {winner} з {winning_score} балами.\n")

def condor_win(votes):
    candidates = set(candidate for vote in votes for candidate in vote[:-1])
    pair_win = {pair: 0 for pair in [(c1, c2) for c1 in candidates for c2 in candidates if c1 != c2]}

    for vote in votes:
        for i, candidate1 in enumerate(vote[:-1]):
            for j in range(i + 1, len(vote) - 1):
                candidate2 = vote[j]
                pair_win[(candidate1, candidate2)] += vote[-1]

    condorcet_winner = max(candidates, key=lambda candidate: sum(pair_win.get((candidate, other), 0) > pair_win.get((other, candidate), 0) for other in candidates))

    print(f"Переможець за правилом Кондорсе: {condorcet_winner}\n")

    for other in candidates:
        if condorcet_winner != other:
            wins = pair_win.get((condorcet_winner, other), 0)
            loses = pair_win.get((other, condorcet_winner), 0)
            print(f"{condorcet_winner} порівняно з {other} {wins} : {loses}")

    print()

def copeland_rule(votes):
    candidates = set()
    pair_score = {}

    for vote in votes:
        for candidate in vote[:-1]:
            candidates.add(candidate)

    for candidate1 in candidates:
        for candidate2 in candidates:
            if candidate1 != candidate2:
                pair_score[(candidate1, candidate2)] = 0

    for vote in votes:
        for i in range(len(vote) - 1):
            for j in range(i + 1, len(vote) - 1):
                candidate1 = vote[i]
                candidate2 = vote[j]
                if candidate1 != candidate2:
                    pair_score[(candidate1, candidate2)] += 1

    candidate_scores = {candidate: 0 for candidate in candidates}
    for pair, score in pair_score.items():
        candidate_scores[pair[0]] += score
        candidate_scores[pair[1]] -= score

    winner = max(candidate_scores, key=candidate_scores.get)

    print(f"Переможець за правилом Копленда {winner} з {candidate_scores[winner]} балами.\n")

def simpson_rule(votes):
    candidates = set()
    pair_sum = {}

    for vote in votes:
        for candidate in vote[:-1]:
            candidates.add(candidate)

    for candidate1 in candidates:
        for candidate2 in candidates:
            if candidate1 != candidate2:
                pair_sum[(candidate1, candidate2)] = 0

    for vote in votes:
        for i in range(len(vote) - 1):
            for j in range(i + 1, len(vote) - 1):
                candidate1 = vote[i]
                candidate2 = vote[j]
                if candidate1 != candidate2:
                    pair_sum[(candidate1, candidate2)] += vote[-1]

    cand_min_max_sum = {}
    for candidate in candidates:
        min_sum = min(pair_sum[(candidate, other)] for other in candidates if candidate != other)
        cand_min_max_sum[candidate] = min_sum

    winner = max(cand_min_max_sum, key=cand_min_max_sum.get)

    print(f"Переможець за правилом Сімпсона {winner} з {cand_min_max_sum[winner]} балами.\n")

def math_with_candidates(votes):
    print("Таблиця розподілу голосів між кандидатами: ")
    df = pd.DataFrame(votes, columns=["1st", "2nd", "3rd", "4th", "К-сть Голосів"])
    print(df.to_string(index=False))

    abs_major(votes)
    rel_major(votes)
    borda_win(votes)
    condor_win(votes)
    copeland_rule(votes)
    simpson_rule(votes)

votes = [
    ("A", "C", "D", "B", 5),
    ("C", "A", "B", "D", 8),
    ("B", "C", "A", "D", 3),
    ("B", "A", "C", "D", 4),
]
def main():
    math_with_candidates(votes)

if __name__ == '__main__':
    main()

