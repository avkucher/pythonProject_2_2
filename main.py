from flask import Flask, render_template, request

import utils

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:candidate_id>')
def get_candidate(candidate_id):
    candidate = utils.get_candidate(candidate_id)

    if not candidate:
        return 'Кандидат не найден'

    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def get_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)

    candidates_count = len(candidates)

    return render_template('search.html', candidates=candidates, candidates_count=candidates_count)


@app.route('/skill/<skill_name>')
def get_candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)

    candidates_count = len(candidates)
    return render_template('skill.html', candidates=candidates, candidates_count=candidates_count)


app.run()
