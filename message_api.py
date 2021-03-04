from message_models import app, db, Admin, Tag, User, Message

@app.route('/index')
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run()