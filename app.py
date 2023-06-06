from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
db = SQLAlchemy(app)


class Blog(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.no} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        blog = Blog(title=title, desc=desc)
        db.session.add(blog)
        db.session.commit()
    allblog = Blog.query.all()
    return render_template('index.html', allBlog=allblog)


@app.route('/postblog/', methods=['GET', 'POST'])
def post():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        blog = Blog(title=title, desc=desc)
        db.session.add(blog)
        db.session.commit()
    allblog = Blog.query.all()
    return render_template('postblog.html', blog=allblog)


@app.route('/blog/<int:no>')
def blog(no):
    blogquery = Blog.query.filter_by(no=no).first()
    return render_template('blog.html', blog=blogquery)


@app.route('/updateblog/<int:no>', methods=['GET', 'POST'])
def update(no):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        blogquery = Blog.query.filter_by(no=no).first()
        blogquery.title = title
        blogquery.desc = desc
        db.session.add(blogquery)
        db.session.commit()
        return redirect("/")
    updateblog = Blog.query.filter_by(no=no).first()
    return render_template('updateblog.html', blog=updateblog)


@app.route('/deleteblog/<int:no>')
def delete(no):
    deleteblog = Blog.query.filter_by(no=no).first()
    db.session.delete(deleteblog)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=False, port=8000)
