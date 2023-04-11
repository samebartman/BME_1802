from flask import render_template, flash, redirect, url_for, request
from cprwalkthrough import app, db
from cprwalkthrough.models import Video, Audio
from . import inject_data

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/', methods=['GET', 'POST'])
def redirect_to_primary():
    return redirect(url_for('primary_assessment'))

@app.route('/primary_assessment', methods=['GET', 'POST'])
def primary_assessment():
    audio_name = db.session.query(Audio)[0].audioname
    return render_template('primary_assessment.html', title='Primary Assessment', audio_name=audio_name)

@app.route('/compressions', methods=['GET', 'POST'])
def compressions():
    name = db.session.query(Video)[1].filename
    audio_name = db.session.query(Audio)[1].audioname
    return render_template('compressions.html', title='Compressions', name=name, audio_name=audio_name)

@app.route('/breaths', methods=['GET', 'POST'])
def breaths():
    name = db.session.query(Video)[2].filename
    audio_name = db.session.query(Audio)[2].audioname
    return render_template('breaths.html', title='Breaths', name=name, audio_name=audio_name)

@app.route('/recovery', methods=['GET', 'POST'])
def recovery():
    name = db.session.query(Video)[3].filename
    audio_name = db.session.query(Audio)[3].audioname
    return render_template('recovery.html', title='Recovery', name=name, audio_name=audio_name)
