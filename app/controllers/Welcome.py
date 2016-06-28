from system.core.controller import *
class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def register(self):
        user_info = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'phone_number': request.form['phone_number'],
            'school_location': request.form['school_location'],
            'pw': request.form['pw'],
            'cpw': request.form['cpw']
        }
        create_status = self.models['WelcomeModel'].register_user(user_info)
        if create_status['status'] == True:
            session['user_id'] = create_status['user']['id']
            return redirect('/')
        else:
            for message in create_status['errors']:
                flash(message, 'register errors')
                return redirect('/')