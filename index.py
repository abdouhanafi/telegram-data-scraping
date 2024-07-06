from flask import Flask, request, render_template, g, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'passwords.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def legal_notice():
    return render_template('legal_notice.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        return redirect(url_for('search', query=query, page=1))
    else:
        query = request.args.get('query', '')
        page = request.args.get('page', 1, type=int)
        results_per_page = 10

        results = search_data(query, page, results_per_page)
        total_results = count_results(query)
        total_pages = (total_results // results_per_page) + (1 if total_results % results_per_page > 0 else 0)

        return render_template('results.html', query=query, results=results, page=page, total_pages=total_pages, result_count=total_results)

def search_data(query, page, results_per_page):
    db = get_db()
    offset = (page - 1) * results_per_page
    cursor = db.execute(
        '''SELECT browser, profile, url, login, password 
           FROM passwords 
           WHERE browser LIKE ? OR profile LIKE ? OR url LIKE ? OR login LIKE ? OR password LIKE ? 
           LIMIT ? OFFSET ?''',
        ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%', results_per_page, offset)
    )
    results = cursor.fetchall()
    cursor.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]

def count_results(query):
    db = get_db()
    cursor = db.execute(
        '''SELECT COUNT(*) 
           FROM passwords 
           WHERE browser LIKE ? OR profile LIKE ? OR url LIKE ? OR login LIKE ? OR password LIKE ?''',
        ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%')
    )
    count = cursor.fetchone()[0]
    cursor.close()
    return count

if __name__ == '__main__':
    app.run(debug=True)
