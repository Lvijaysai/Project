'// QuizScores/myapp/views.py'
from django.shortcuts import render
import csv
import statistics

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def upload_and_analyze_index(request):
    context = {}
    if request.method == 'POST' and 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']
        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            scores = []
            students = []
            for row in reader:
                try:
                    name = row['Name'].strip()
                    score = int(row['Score'])
                    scores.append(score)
                    students.append({
                        'name': name,
                        'score': score,
                        'grade': get_grade(score),
                    })
                except (ValueError, KeyError):
                    continue

            if not scores:
                context['error'] = "No valid scores found in the file."
            else:
                avg = statistics.mean(scores)
                med = statistics.median(scores)
                highest = max(scores)
                lowest = min(scores)

                grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
                for score in scores:
                    grade = get_grade(score)
                    grade_dist[grade] += 1

                context['stats'] = {
                    'avg': f"{avg:.2f}",
                    'med': med,
                    'highest': highest,
                    'lowest': lowest,
                    'grade_dist': grade_dist,
                }
                context['students'] = students

        except Exception as e:
            context['error'] = f"Error processing file: {str(e)}"

    return render(request, 'QuizScores/upload.html', context)
