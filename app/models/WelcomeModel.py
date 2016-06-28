from system.core.model import Model
import re
from datetime import datetime
class WelcomeModel(Model):
        def __init__(self):
            super(WelcomeModel, self).__init__()
        def register_user(self, info):
            EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
            errors = []
            pw = info['pw']
            pw_hash = self.bcrypt.generate_password_hash(pw)
            if not info['first_name']:
                errors.append('First Name cannot be blank.')
            elif len(info['first_name']) < 2:
                errors.append('First Name must be at least two characters long')
            elif any(char.isdigit() for char in info['first_name']):
                errors.append('First Name can only be letters')
            if not info['last_name']:
                errors.append('Last Name cannt be blank.')
            elif len(info['last_name']) < 2:
                errors.append('Last Name must be at least two characters long')
            elif any(char.isdigit() for char in info['last_name']):
                errors.append('Last Name can only be letters')
            if not info['email']:
                errors.append('Email cannot be blank.')
            elif not EMAIL_REGEX.match(info['email']):
                errors.append('Email format is not valid.')
            if not info['phone_number']:
                errors.append('Phone number be blank.')
            elif len(info['phone_number']) < 10:
                errors.append('Phone number must be 9 digits long and include area code')
            if not['school_location']:
                errors.append('Your college location cannot be blank')
            if not info['pw']:
                errors.append('Password cannot be blank')
            elif len(info['pw']) < 8:
                errors.append('Password must be at least 8 characters long')
            elif info['pw'] != info['cpw']:
                errors.append('Password and confirmation must match.')
            if errors:
                return {"status": False, "errors": errors}
            else:
                query = "INSERT into students (first_name, last_name, email, phone_number, school_location, pw) VALUES(:first_name, :last_name, :email, :phone_number, :school_location, :pw)"
                data = {
                    'first_name': info['first_name'],
                    'last_name': info['last_name'],
                    'email': info['email'],
                    'phone_number': info['phone_number'],
                    'school_location': info['school_location'],
                    'pw': pw_hash
                }
                self.db.query_db(query, data)
                get_user_query = "SELECT * FROM users"
                users = self.db.query_db(get_user_query)
                return {"status": True, "user": users[0]}
