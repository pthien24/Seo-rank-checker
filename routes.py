from flask import render_template , request, redirect, url_for
from googlesearch import search
from models import Person
from models import User
import math

def register_route(app,db):
    @app.route('/')
    def index():
        rows = User.query.order_by(User.date_submitted.desc()).all()
        no_data = len(rows) == 0
        return render_template('index.html', rows=rows, no_data=no_data)


    @app.route('/', methods=['POST'])
    def check_rank():
        domain = request.form['domain']
        keywords = request.form['keywords'].split(',')  # Split keywords by comma
        region = request.form['region']

        # Determine top-level domain based on region
        if region == "1":
            domain_tld = "vn"
            region_name = "Vietnam"
            print('The search is in Vietnam - Google')
        elif region == "2":
            domain_tld = "vn"
            region_name = "Vietnam"
            print('The search is in Vietnam - Google')

        results = []

    # Function to search for keyword ranks
        def searchfunc(my_website):
            print(f"Searching for {my_website} with keywords: {keywords}...")
            for keyword in keywords:
                # Google search does not require 'tld' parameter in the latest version
                urls = search(keyword)

                found = False
                for index, url in enumerate(urls):
                    if my_website in url:
                        page = math.ceil((index + 1) / 10)
                        rank = index + 1
                        results.append({"keyword": keyword, "rank": rank, "page": page, "url": url})
                        print(f"Searching for {my_website} with keywords: {keywords}... {rank} and {page}...")
                        found = True
                        break

                if not found:
                    results.append({"keyword": keyword, "rank": "Not Found", "page": "Not Found"})
        # Call the search function
        searchfunc(domain)

        for result in results:
            user = User(domain=domain, keywords=result["keyword"], rank=result["rank"], page=result["page"], region=region_name)
            db.session.add(user)
        db.session.commit()
    
        return redirect(url_for('index'))

    # Route to handle entry deletion
    @app.route('/delete/<int:sno>', methods=['POST'])
    def delete_entry(sno):
        entry = User.query.get_or_404(sno)
        db.session.delete(entry)
        db.session.commit()
        return redirect(url_for('index'))
