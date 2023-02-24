from django.shortcuts import render


def main(request):
    data = {
        'title': 'Главная страница!!',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/about.html')
