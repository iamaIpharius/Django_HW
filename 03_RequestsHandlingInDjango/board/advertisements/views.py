from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


class Contacts(TemplateView):
    template_name = "contacts/contacts_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adress'] = 'Adress'
        context['phone'] = 'Phone'
        context['email'] = 'Email'
        return context


class About(TemplateView):
    template_name = "contacts/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "SUPER-COMPANY"
        context['text'] = """


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse elementum turpis ut justo ultrices finibus. Quisque metus mauris, malesuada vel suscipit quis, facilisis id nunc. Sed felis massa, tincidunt at dui eleifend, bibendum imperdiet erat. Ut sed odio volutpat, scelerisque quam nec, pellentesque mauris. Sed feugiat lectus non lorem mattis, non fermentum metus euismod. Phasellus sed enim purus. Phasellus at elit eu dui porttitor consectetur id id urna. Integer eget ullamcorper lectus. Quisque at egestas magna, ut suscipit elit. Sed porta porta ligula id commodo. Phasellus laoreet dolor velit, varius dapibus metus eleifend et. Suspendisse risus turpis, cursus sit amet sollicitudin eget, maximus sed purus. Integer consequat nunc vel leo tempus, id gravida lectus accumsan.

Mauris lobortis ipsum ligula, sit amet iaculis odio auctor non. Pellentesque condimentum eros tellus, vestibulum viverra odio feugiat ut. Mauris non tempus purus, non molestie lectus. Ut non vestibulum mi. Fusce sit amet auctor libero. Quisque blandit faucibus ante at semper. Vivamus sit amet nunc quis neque tempor ornare sit amet quis purus. Morbi tristique pharetra viverra. Sed eu tristique risus, id tempor neque. Ut in quam sapien. Nunc rhoncus, libero sit amet pellentesque dapibus, erat metus feugiat elit, a posuere nulla ligula at nunc. Etiam vitae mi ornare, sollicitudin lorem et, lobortis diam. Nam scelerisque odio urna, sed pellentesque tellus convallis eu. Nam ornare dictum mi in scelerisque. Pellentesque mollis turpis luctus fermentum imperdiet. Phasellus posuere diam vel urna varius, eu bibendum dolor dictum.

Sed imperdiet erat quis tempor convallis. Nulla eu sapien tempor, tincidunt ante ac, porttitor sapien. Nunc scelerisque nec lorem rutrum consectetur. Aenean consectetur nisi id eros vehicula dignissim. Nunc porta nisi ut purus laoreet, id interdum velit auctor. Quisque tincidunt sem arcu, et sagittis massa auctor at. Phasellus volutpat porttitor augue. Praesent rhoncus ex sed pretium interdum. Sed in turpis id tellus suscipit dictum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Pellentesque sagittis ante vitae sodales egestas. Fusce vitae sem arcu. Praesent lacus neque, hendrerit sit amet dictum sit amet, fermentum sit amet erat.

Praesent id erat id arcu elementum tincidunt sit amet sit amet felis. Duis non lacus sit amet augue vehicula pellentesque semper pretium erat. In hac habitasse platea dictumst. Etiam quis suscipit ipsum. Praesent ultrices erat tortor, ut pharetra sapien scelerisque sit amet. Pellentesque ullamcorper ornare auctor. Nulla sit amet iaculis nulla. Cras cursus, eros vitae vulputate convallis, nibh arcu pretium diam, at tincidunt ipsum velit eu leo. Pellentesque ac tellus in quam tincidunt dapibus et a tellus. Maecenas laoreet porta leo vitae euismod. Donec at blandit risus. Proin et venenatis ante, ut euismod arcu. Nulla in sollicitudin metus. Nullam placerat elementum ex, et malesuada massa venenatis non.

Nunc auctor lectus in nisi venenatis, id dictum est volutpat. Phasellus suscipit elementum finibus. Mauris at mollis tellus, id pretium nisl. Nulla tempor mattis urna id varius. Morbi pellentesque tincidunt risus. Quisque eu quam a tortor laoreet suscipit. Proin est erat, euismod at massa non, varius interdum nulla. Fusce augue nisl, volutpat sed felis sed, lobortis tempus purus. Cras quis enim mi. Donec scelerisque arcu enim, ac luctus justo placerat et. Praesent at lorem lorem. Mauris ultrices, lacus et lacinia tempus, est mauris tempor nibh, sed pulvinar justo sem congue elit. Nam ullamcorper at lorem in pulvinar. 

        """
        return context


class Advertisements(TemplateView):
    template_name = "advertisements/advertisement_list.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['advertisements'] = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Best practices for begginers',
            'You have won 1000 dollars!'
        ]
        context['count'] = 0
        return context

    def post(self, request):
        req_new = 'запрос на создание новой записи успешно выполнен.'

        return render(request, 'advertisements/success.html', {'req_new': req_new})


class Main(View):

    def get(self, request):
        cathegory = ['work', 'study', 'trade', 'home', 'games']
        regions = ['moscow', 'st.petersburg',
                   'pskov', 'novgorod', 'kaluga', 'ryazan']
        field = 'Here you can search ads!'
        button = 'Search'

        return render(request, 'mainpage/main.html',
                      {'cathegory': cathegory, 'regions': regions, 'button': button, 'field': field})
