from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question
# Create your views here.
class IndexView(generic.ListView):
    model = Question
    template_name = 'words/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('id')[:5]

class DetailView(generic.DetailView):
    model = Question
    slug_field = 'question_key'
    template_name = 'words/detail.html'
    def get_object(self):
        object = get_object_or_404(Question,question_key=self.kwargs['question_key'])
        return object

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'words/results.html'

def submit(request, question_key):
    question = get_object_or_404(Question, pk=question_key)
    try:
        answer_from_post = (request.POST['answerSubmit'])
        if answer_from_post == '':
            raise TypeError
        elif answer_from_post != question.answer_text:    
            return render(request, 'words/detail.html', {
                'question': question,
                'error_message': "Sorry bud, wrong answer...",
            })
    except (TypeError):
        #Redisplay the question voting form.
        return render(request, 'words/detail.html', {
                'question': question,
                'error_message': "At least try something... Ugh...",
            })
        #return HttpResponseRedirect(reverse('words:detail', args=(question.question_key,)))
    else:
        # print(question.id)
        next_question_id = question.id + 1
        next_question = get_object_or_404(Question, pk=next_question_id)
        if question.answer_text == answer_from_post:
            return HttpResponseRedirect(reverse('words:detail', args=(next_question.question_key,)))
            # return render(request, 'words/detail.html', {
            # 'question': question,
            # 'congrats_message': "Correct!",
            # })  
        # question.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.        
