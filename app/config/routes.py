from system.core.router import routes

routes['default_controller'] = 'Sessions'

routes['/register'] = 'Sessions#show_register_page'

routes['/login'] = 'Sessions#show_login_page'

routes['POST']['/login'] = 'Sessions#login'

routes['POST']['/register'] = 'Sessions#register'

routes["/logout"] = "Sessions#logout"

