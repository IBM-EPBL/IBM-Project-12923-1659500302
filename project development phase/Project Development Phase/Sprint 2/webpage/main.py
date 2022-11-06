{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "515d7a35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "D:\\Software\\python\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3465: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "#Imported Libraries\n",
    "from flask import Flask, app, request, render_template\n",
    "import os\n",
    "import flask\n",
    "import re\n",
    "import flask_login\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "app.secret_key = 'apple'\n",
    "login_manager = flask_login.LoginManager()\n",
    "\n",
    "login_manager.init_app(app)\n",
    "users = {'a@b.c': {'password': '123'}}\n",
    "class User(flask_login.UserMixin):\n",
    "    pass\n",
    "\n",
    "\n",
    "@login_manager.user_loader\n",
    "def user_loader(email):\n",
    "    if email not in users:\n",
    "        return\n",
    "\n",
    "    user = User()\n",
    "    user.id = email\n",
    "    return user\n",
    "\n",
    "\n",
    "@login_manager.request_loader\n",
    "def request_loader(request):\n",
    "    email = request.form.get('email')\n",
    "    if email not in users:\n",
    "        return\n",
    "\n",
    "    user = User()\n",
    "    user.id = email\n",
    "    return user\n",
    "@app.route('/')\n",
    "def index():\n",
    "    if(flask_login.current_user.is_authenticated):\n",
    "        return render_template('dashboard.html')\n",
    "    else:\n",
    "        return render_template('login.html')\n",
    "#Register function declared\n",
    "@app.route('/register',methods = ['GET','POST'])\n",
    "def register():\n",
    "    error = None\n",
    "    if(flask.request.method == 'GET'):\n",
    "        return render_template('register.html')\n",
    "    email = flask.request.form['email']\n",
    "    if(email in users):\n",
    "        return render_template('register.html',flash_message='True')\n",
    "    else:\n",
    "        users[email]={'password':flask.request.form['password']}\n",
    "        user  = User()\n",
    "        user.id = email\n",
    "        flask_login.login_user(user)\n",
    "        return render_template('dashboard.html',flash_message='True')\n",
    "\n",
    "\n",
    "#Login function declared\n",
    "@app.route('/login',methods =['GET','POST'])\n",
    "def login():\n",
    "    error = None\n",
    "    if(flask.request.method == 'GET'):\n",
    "        \n",
    "        return render_template('login.html',flash_message='False')\n",
    "    email = flask.request.form['email']\n",
    "    if(email in users and flask.request.form['password']==users[email]['password']):\n",
    "        user  = User()\n",
    "        user.id = email\n",
    "        flask_login.login_user(user)\n",
    "        return render_template('dashboard.html',flash_message='Fal')\n",
    "    #flask.flash('invalid credentials !!!')\n",
    "    return render_template('login.html',flash_message=\"True\")\n",
    "    #error = 'inavlid credentials')\n",
    "\n",
    "#Dashboard function declared\n",
    "@app.route('/dashboard',methods = ['GET','POST'])\n",
    "@flask_login.login_required\n",
    "def dashboard():\n",
    "    if(flask.request.method == 'GET'):\n",
    "        return render_template('dashboard.html',flash_message='False')\n",
    "    email = flask.request.form['email']\n",
    "    if(email in users and flask.request.form['password']==users[email]['password']):\n",
    "        user  = User()\n",
    "        user.id = email\n",
    "        flask_login.login_user(user)\n",
    "        return render_template('dashboard.html',flash_message=\"Fal\")\n",
    "    return render_template('dashboard.html',flash_message=\"Fals\")\n",
    "\n",
    "#Logout function declared\n",
    "@app.route('/logout')\n",
    "@flask_login.login_required\n",
    "def logout():\n",
    "    flask_login.logout_user()\n",
    "    return render_template('logout.html')\n",
    "\n",
    "\n",
    "@app.route('/prediction')\n",
    "@flask_login.login_required\n",
    "def prediction():\n",
    "    return render_template('prediction.html')\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True,port = 8000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "761c32a7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
