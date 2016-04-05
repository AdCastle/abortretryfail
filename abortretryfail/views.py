from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/template.pt')
def my_view(request):
    return {'project': 'abortretryfail'}


@view_config(route_name='maps/amsterdam-ww2', renderer='templates/maps/ww2-amsterdam/template.pt')
def amsterdam_ww2(request):
    return {'project': 'abortretryfail'}


@view_config(route_name='isitfriday', renderer='templates/isitfriday.pt')
def isitfriday(request):
    return {'project': 'abortretryfail'}
