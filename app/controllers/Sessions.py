from system.core.controller import *
from flask import Flask,flash

class Sessions(Controller):
    def __init__(self, action):
        super(Sessions, self).__init__(action)
        self.load_model("Student")

    def index(self):
        if "user_id" in session:
            result = self.models["Student"].get_user_info(session["user_id"])
            print result
            if len(result) > 0:
                return self.load_view("success.html")
        return self.load_view('index.html')

    def show_register_page(self):
        return self.load_view('register.html')

    def show_login_page(self):
        return self.load_view('index.html')

    def register(self):
        user_status = self.models['Student'].create_user(request.form)

        if user_status["status"] == False:
            return redirect("/register")

        session["user_id"] = user_status["user_id"]

        return self.load_view("success.html")

    def login(self):
        info = {
            "email": request.form["email"],
            "pwd": request.form["pwd"]
        }

        result = self.models["Student"].login_user(info)

        if result["status"] == False:
            return redirect("/")

        session["user_id"] = result["user"]["id"]

        return self.load_view("success.html")

    def logout(self):
        if "user_id" in session:
            session.pop("user_id")

        return redirect("/")