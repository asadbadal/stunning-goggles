from notejam import app


@app.route('/welcome')
def welcome_page():
    return "Welcome page!"

@app.route('/func1')
def func1_page():
    return "func1!"

if __name__ == '__main__':
    welcome_page()
    func1_page()
    
    app.run()
