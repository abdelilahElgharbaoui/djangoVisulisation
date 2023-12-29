# qcm/views.py
from django.shortcuts import render,redirect
from .models import Question
from .forms import AnswerForm

def display_questions(request):
    questions = Question.objects.all()
    form = AnswerForm()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        print(form)
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                # Get the selected choices from the form
                selected_choices_ids = form.cleaned_data['choices']

                # Retrieve the selected choices from the database
                selected_choices = Choice.objects.filter(id__in=selected_choices_ids)

                # Calculate the score
                score = 0
                for choice in selected_choices:
                    if choice.is_correct:
                        score += 1

                # Check if all questions are answered correctly
                all_correct = score == len(questions)

                # You can save the score in the user's session or database
                # For simplicity, let's just print the score and correctness for now
                print(f"Your score: {score}")
                print(f"All answers correct: {all_correct}")

                # You may want to redirect to a result page or display a message
                return redirect('result_page')
    return render(request, 'qst.html', {'questions': questions, 'form': form})
