from django.shortcuts import render
from .models import Menu


def index(request):
    return render(
        request,
        'menu/index.html',
        {'menus': Menu.objects.all()}
    )


def draw_menu(request, path):
    splitted_path = path.split('/')
    if len(splitted_path) <= 0:
        return render(
            request,
            'menu/index.html',
            {'error_message': f'Invalid path size: "/{path}"'},
        )
    else:
        return render(
            request,
            'menu/index.html',
            {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]}
        )
