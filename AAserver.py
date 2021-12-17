import os

import speech_recognition as sr
import pymysql

os.environ.setdefault('PATH', '')
from flask import Flask, render_template, request, redirect, url_for

con = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      db='ActorAesthetic')
cursor = con.cursor()
app = Flask(__name__)
r = sr.Recognizer()


# home
@app.route('/')
def index():
    cursor.execute("SELECT * from Blog ORDER BY `postDate` DESC LIMIT 4")
    favorites = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'lifestyle' ORDER BY `postDate` DESC LIMIT 3")
    lifestyle = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'auditioning' ORDER BY `postDate` DESC LIMIT 3")
    audition = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'equity' ORDER BY `postDate` DESC LIMIT 3")
    equity = cursor.fetchall()
    return render_template('index.html', favorites=favorites, lifestyle=lifestyle, audition=audition, equity=equity)


# about
@app.route('/about')
def about():
    return render_template('about.html')


# register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form.get('userSubmit'):
            fullname = request.form['fullName']
            email = request.form['userEmail']

            newBlog = "INSERT INTO ActorAesthetic.users(fullName, userEmail) VALUES(%s, %s); "
            info = (fullname, email)
            cursor.execute(newBlog, info)
            con.commit()
    return render_template("login.html")


# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


# if Admin user bring to dashboard, other users are directed to the courses/shop
@app.route('/verify', methods=['GET', 'POST'])
def dashVerify():
    user = request.form['username']
    password = request.form['password']
    if user != 'maggiebera' or password != 'admin':
        return redirect(url_for('index'))
    else:
        return dash()


@app.route('/dashboard', methods=['GET', 'POST'])
def dash():
    cursor.execute("SELECT * FROM `blog` ORDER BY `postDate` DESC")
    blogdata = cursor.fetchall()

    cursor.execute("SELECT * FROM `podcast` ORDER BY `podDate` DESC")
    podata = cursor.fetchall()

    if request.method == 'POST':
        if request.form.get('blogSubmit'):
            title = request.form['postTitle']
            sub = request.form['postSub']
            content = request.form['postContent']
            file = request.form['file']
            cat = request.form['category']
            date = request.form['postDate']

            newBlog = "INSERT INTO ActorAesthetic.Blog(postTitle, postSub, postContent, postFile, postCat, " \
                      "postDate) VALUES(%s, %s, %s, %s, %s, %s); "
            info = (title, sub, content, file, cat, date)
            cursor.execute(newBlog, info)
            con.commit()
            return redirect(url_for('blog'))

        if request.form.get('podSubmit'):
            title = request.form['podTitle']
            sub = request.form['podSub']
            audio = request.form['podAudio']
            content = request.form['podContent']
            url = request.form['podURL']
            guest = request.form['podGuest']
            date = request.form['podDate']
            mp3Text = request.form['podText']

            newPod = "INSERT INTO ActorAesthetic.Podcast(podTitle, podSub, podAudio, podContent, podURL, podGuest, " \
                     "podDate, podText) VALUES(%s, %s, %s, %s, %s, %s, %s, %s); "
            info = (title, sub, audio, content, url, guest, date, mp3Text)
            cursor.execute(newPod, info)
            con.commit()
            return redirect(url_for('podcast'))
    return render_template('dash.html', blogdata=blogdata, podata=podata)


# blog database
@app.route('/blog', methods=['GET', 'POST'])
def blog():
    cursor.execute("SELECT * FROM `blog` ORDER BY `postDate` DESC")
    blogdata = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'top' ORDER BY `postDate` DESC")
    top = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'college' ORDER BY `postDate` DESC")
    college = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'equity' ORDER BY `postDate` DESC")
    equity = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'lifestyle' ORDER BY `postDate` DESC")
    lifestyle = cursor.fetchall()

    cursor.execute("SELECT * from Blog where postCat = 'auditioning' ORDER BY `postDate` DESC")
    auditioning = cursor.fetchall()
    return render_template('blog.html', blogdata=blogdata, top=top, college=college, equity=equity, lifestyle=lifestyle,
                           auditioning=auditioning)


# podcast database
@app.route('/podcast', methods=['GET', 'POST'])
def podcast():
    cursor.execute("SELECT * FROM `podcast` ORDER BY `podDate` DESC LIMIT 10")
    recent = cursor.fetchall()

    cursor.execute("SELECT * FROM `podcast` where `podGuest` != 'Maggie' ORDER BY `podDate` DESC")
    guest = cursor.fetchall()

    cursor.execute("SELECT * FROM `podcast` where `podGuest` = 'Maggie' ORDER BY `podDate` DESC")
    maggie = cursor.fetchall()

    return render_template('podcast.html', recent=recent, guest=guest, maggie=maggie)


# single blog post
@app.route('/blogPost', methods=['GET', 'POST'])
def blogPost():
    if request.method == 'POST':
        if request.form.get('readButton'):
            selectedPost = request.form['readButton']
            cursor.execute("SELECT * from Blog")
            blogdata = cursor.fetchall()
            html = str(selectedPost)
            return render_template('blogPost.html', blogdata=blogdata, html=html)


# single podcast
@app.route('/podcastPost', methods=['GET', 'POST'])
def podcastPost():
    if request.method == 'POST' and request.form.get('listenButton'):
        selectedPod = request.form['listenButton']
        cursor.execute("SELECT * from Podcast")
        podata = cursor.fetchall()
        id = str(selectedPod)
        return render_template('podcastPost.html', podata=podata, id=id)


# request audio transcript
@app.route('/transcript', methods=['GET', 'POST'])
def transcript():
    if request.method == 'POST' and request.form.get('textButton'):
        selectedPod = request.form['textButton']
        selectedPod = f"speech-files/{selectedPod}"
        return render_template(selectedPod)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
