from flask import Flask, render_template, request, redirect

app = Flask(__name__)

base = {}

@app.route('/')
def index():
    note = None

    if 'note' in base:
        note = base['note']
    edit_count = base.get('edit_count', 0)

    return render_template('index.html', note=note, edit_count=edit_count)


@app.route('/note', methods=['GET', 'POST'])
def notebook():
    if request.method == 'POST':
        base['note'] = request.form['note']
        base['edit_count'] = base.get('edit_count', 0) + 1

        return redirect('/')



    return render_template('note.html', note=base.get('note'))


if __name__ == '__main__':
    app.run()
