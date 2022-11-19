"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template('form.html')

@app.route('/results')
def show_results():
    """Show resulting message."""
    cheery = request.args.get('cheery')
    honest =  request.args.get('honest')
    dreary =  request.args.get('dreary')
    if cheery and honest and dreary:
        msg = "Not possible"
    elif cheery and honest and not dreary:
        msg = "Here's' a cheery and honest message: you are pretty awesome!"
    elif cheery and dreary and not honest:
        msg = "You are the greatest, but not for long!"
    elif dreary and honest:
        msg = "You won't live forever"
    elif not dreary and not honest and cheery:
        msg = " Santa is real and getting you everything you asked for!"
    elif not honest and not cheery:
        msg = "You will likely have to do homework over Thanksgiving break."
    else:
        msg = "God loves you."
    return render_template('results.html', msg=msg)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
