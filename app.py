from flask import Flask, render_template, request
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route('/')
def homepage():
    """Show list-of-stories form."""
    return render_template('create-story.html', stories=stories.values())

@app.route('/form')
def ask_questions():
    """Show the Madlibs form."""
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts
    return render_template('form.html', story_id=story_id,title=story.title,prompts=prompts)

@app.route('/story')
def show_story():
    """Generate and show the Madlibs story."""
    story_id = request.args["story_id"]
    story= stories[story_id]
    text = story.generate(request.args)

    return render_template("story.html", title=story.title,text=text)

if __name__ == '__main__':
    app.run(debug=True)