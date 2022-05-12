number_of_subjects = int(input())
subjects = list(map(int, input().split()))

max_score = max(subjects)

fake_score = sum(subjects) / max_score * 100

print(fake_score / number_of_subjects)