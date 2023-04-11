from cprwalkthrough import app
from cprwalkthrough.models import Video

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Video': Video}