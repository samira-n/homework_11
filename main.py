from flask import Flask, render_template
import utils

app = Flask(__name__)

data = utils.load_candidates_from_json('candidates.json')


@app.route('/')
def index():
    return render_template('list.html', candidates=data)


@app.route('/candidate/<int:uid>')
def profile(uid):
    candidate = utils.get_candidate(uid)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<name>')
def search(name):
    candidates = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route('/skill/<skill_name>')
def skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, candidates_len=len(candidates),  skill= skill_name)



if __name__ == '__main__':
    app.run(debug=True)