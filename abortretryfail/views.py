from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/template.pt')
def my_view(request):
    return {'project': 'abortretryfail'}
