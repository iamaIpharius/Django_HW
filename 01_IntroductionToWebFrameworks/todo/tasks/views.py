from django.http import HttpResponse

from django.views import View

import random

class ToDoView(View):

    def get(self, request, *args, **kwargs):

        elements = ['Установить python', 'Установить django', 'Запустить сервер', 'Порадоваться результату', 'Выпить чаю']
        random.shuffle(elements)


        return HttpResponse('<ul>'
                            f'<li>{elements[0]}</li>'
                            f'<li>{elements[1]}</li>'
                            f'<li>{elements[2]}</li>'
                            f'<li>{elements[3]}</li>'
                            f'<li>{elements[4]}</li>'
                            '</ul>')
