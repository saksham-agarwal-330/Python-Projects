from flask import Flask,render_template,request,session,redirect,flash,jsonify,send_from_directory,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
from datetime import datetime
import json
from flask_mail import Mail
import os
import math
from authlib.integrations.flask_client import OAuth

with open('config.json','r') as c:
    params=json.load(c)["params"]
local_server=True
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=params['upload_location']
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.secret_key='super-secret-key'

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='587',
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']

)
bcrypt = Bcrypt(app)
oauth = OAuth(app)
mail=Mail(app)
if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
bcrypt = Bcrypt(app) 
db = SQLAlchemy(app)

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    profile_pic = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_num = db.Column(db.String(15), nullable=False ,unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False, default='subuser')
    visit_count = db.Column(db.Integer, default=0)
    posts = db.relationship('Posts', backref='author', cascade="all, delete", lazy=True)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    tagline = db.Column(db.String(130), nullable=False)
    slug = db.Column(db.String(30), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    content = db.Column(db.Text, nullable=False)
    img_file = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    comments_count = db.Column(db.Integer, default=0)  # Use an integer column for count
    likes_count = db.Column(db.Integer, default=0)  # Use an integer column for count
    visit_count = db.Column(db.Integer, default=0)
    comments = db.relationship('Comments', backref='post', lazy=True)
    likes = db.relationship('Likes', backref='post', lazy=True)
    categories = db.relationship('Categories', back_populates='posts')

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    img_file = db.Column(db.String(100), nullable=True)
    posts = db.relationship('Posts', back_populates='categories')

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    email = db.Column(db.String(100), nullable=True)  # Add the new email column
    user = db.relationship('Users', backref='comments', lazy=True)


class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)  # Assume user_id is passed or managed by your auth system


class Media(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False, unique=True)
    url = db.Column(db.String(200), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    post = db.relationship('Posts', backref=db.backref('media', lazy=True))


@app.route('/')
def home():
    categories = Categories.query.all()
    posts = Posts.query.all()
    last=math.ceil(len(posts)/int(params['no_of_posts']))
    page=request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    posts=posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
    if(page==1):
        prev="#"
        next="/?page="+str(page+1)
    elif(page==last):
        prev="/?page="+str(page-1)
        next="#"
    else:
        prev="/?page="+str(page-1)
        next="/?page="+str(page+1)

    if 'user' not in session:
        # If the user is not logged in, show all posts
        
        return render_template('index.html',categories=categories, posts=posts, liked_post_ids=[],params=params,prev=prev,next=next,active_page='home')

    
    # Get the current logged-in user
    current_user = Users.query.filter_by(username=session['user']).first()
    
    # Get the IDs of the posts liked by the current user
    liked_post_ids = db.session.query(Likes.post_id).filter_by(user_id=current_user.user_id).all()
    liked_post_ids = [post_id for (post_id,) in liked_post_ids]  # Flatten list of tuples
    
    # Get all posts to display
    # posts = Posts.query.all()
    return render_template('index.html',categories=categories, posts=posts, liked_post_ids=liked_post_ids,params=params,prev=prev,next=next,active_page='home')

@app.route('/about')
def about():
    categories = Categories.query.all()
    return render_template('about.html',params=params,active_page='about',categories=categories)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = get_search_results(query)
    return render_template('posts.html', results=results)

def get_search_results(query):
    if query:
        search_criteria = [
            Posts.title.ilike(f'%{query}%'),
            Posts.tagline.ilike(f'%{query}%')
        ]
        
        query_obj = db.session.query(Posts).filter(or_(*search_criteria))
        print("Query Object:", query_obj)
        
        results = query_obj.all()
        print("Results:", results)
    else:
        results = []
    
    return results

@app.route('/contact',methods = ['GET', 'POST'])
def contact():
    categories = Categories.query.all()
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from blog' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" + phone)
        flash("Thank you for submitting your details. we will get back to you soon","success")
    return render_template('contact.html',categories=categories,params=params,active_page='contact')



@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
        flash("You have been logged out successfully.", "success")
    else:
        flash("You were not logged in.", "info")
    
    # Redirect to the login page or any other page you deem appropriate
    return redirect('/login')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route("/delete_post/<string:post_id>", methods=['GET', 'POST'])
def delete_post(post_id):
    if 'user' not in session:
        flash('You need to be logged in to delete posts.', 'danger')
        return redirect("/login")
    
    current_user = Users.query.filter_by(username=session['user']).first()
    post = Posts.query.filter_by(post_id=post_id).first()

    if post:
        # Check if the user is the publisher of the post or an admin
        if post.user_id == current_user.user_id or current_user.role == 'admin':
            db.session.delete(post)
            db.session.commit()
            flash('Post deleted successfully.', 'success')
        else:
            flash('You do not have permission to delete this post.', 'danger')
    else:
        flash('Post not found.', 'danger')

    return redirect("/dashboard")

        
@app.route('/post/<string:post_slug>', methods=['GET', 'POST'])
def post_route(post_slug):
    categories = Categories.query.all()
    post = Posts.query.filter_by(slug=post_slug).first_or_404()
    
    # Increment the visit count for the post
    post.visit_count += 1
    db.session.commit()
    
    current_user = None
    user_id = None
    liked_post_ids = []
    
    if 'user' in session:
        current_user = Users.query.filter_by(username=session['user']).first()
        user_id = current_user.user_id if current_user else None
    
    if request.method == 'POST':
        if current_user:
            comment_content = request.form.get('comment')
            email = request.form.get('email')
            new_comment = Comments(content=comment_content, email=email, post_id=post.post_id, user_id=user_id)
            db.session.add(new_comment)
            post.comments_count += 1
            db.session.commit()
            return redirect(url_for('post_route', post_slug=post_slug))

        else:
            flash('You need to log in to comment.', 'warning')
            return redirect(url_for('login'))
        
    comments = Comments.query.filter_by(post_id=post.post_id).all()
    likes_count = Likes.query.filter_by(post_id=post.post_id).count()

    if current_user:
        liked_post_ids = db.session.query(Likes.post_id).filter_by(user_id=user_id).all()
        liked_post_ids = [post_id for (post_id,) in liked_post_ids]  # Flatten list of tuples
    
    user_liked = Likes.query.filter_by(post_id=post.post_id, user_id=user_id).first() if user_id else None

    return render_template('post.html', post=post, categories=categories,comments=comments, liked_post_ids=liked_post_ids, likes_count=likes_count, user_liked=user_liked, active_page='')

@app.route('/category/<string:category>')
def category(category):
    categories = Categories.query.all()
    category_obj = Categories.query.filter_by(name=category).first()
     # Handle the case where the category does not exist
    if category_obj is None:
        return "Category not found"
    # Fetch posts belonging to the given category
    posts = Posts.query.filter_by(category_id=category_obj.id).all()
    
    # Initialize variables
    current_user = None
    user_id = None
    liked_post_ids = []

    # Check if the user is logged in
    if 'user' in session:
        current_user = Users.query.filter_by(username=session['user']).first()
        user_id = current_user.user_id if current_user else None

        # If the user is logged in, fetch liked posts' IDs
        if user_id:
            liked_post_ids = db.session.query(Likes.post_id).filter_by(user_id=user_id).all()
            liked_post_ids = [post_id for (post_id,) in liked_post_ids]  # Flatten list of tuples

    # Render the template with posts and liked post IDs
    return render_template('categories.html',categories=categories, posts=posts, liked_post_ids=liked_post_ids,active_page=category)



@app.route('/add/category/<int:id>', methods=['GET', 'POST'])
def add_category(id):
    if 'user' not in session:
        flash('You need to be logged in to add or edit a category.', 'warning')
        return redirect(url_for('login'))

    current_user = Users.query.filter_by(username=session['user']).first()

    if current_user.role != 'admin':
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('dashboard'))

    # POST request for form submission
    if request.method == 'POST':
        category_name = request.form.get('category')
        img_file = request.files.get('file1')
        filename = None

        # Handling image file upload
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        elif img_file:
            flash('Upload an image in a supported format.', 'warning')
            return render_template('add_category.html', id=id, category=None, active_page='')

        new_category = Categories(name=category_name.title(), img_file=filename)
        db.session.add(new_category)
        db.session.commit()
        flash('New category created successfully.', 'success')
        return redirect(url_for('dashboard'))

        
    return render_template('add_category.html', category=category, active_page='')



@app.route('/like_post/<int:post_id>', methods=['POST'])
def like_post(post_id):
    if 'user' not in session:
        #return jsonify(success=False, message='Please log in to like posts.')  # Redirect to login if user is not logged in
        return redirect('/login')
    post = Posts.query.get_or_404(post_id)
    current_user = Users.query.filter_by(username=session['user']).first()

    if not current_user:
        return jsonify(success=False, error="User not found"), 401

    data = request.get_json()
    action = data.get('action')
    
    # Check if the post is already liked by the current user
    like = Likes.query.filter_by(post_id=post_id, user_id=current_user.user_id).first()
    

    if action == 'like':
        if not like:
            new_like = Likes(post_id=post_id, user_id=current_user.user_id)
            db.session.add(new_like)
            post.likes_count += 1
    elif action == 'unlike':
        if like:
            db.session.delete(like)
            post.likes_count -= 1
    
    db.session.commit()
    liked_post_ids = db.session.query(Likes.post_id).filter_by(user_id=current_user.user_id).all()
    liked_post_ids = [post_id for (post_id,) in liked_post_ids]  # Flatten list of tuples
    return jsonify(success=True, likes_count=post.likes_count,liked_post_ids=liked_post_ids)

@app.route('/profile/<string:username>', methods=['GET'])
def profile_route(username):
    categories = Categories.query.all()
    user = Users.query.filter_by(username=username).first_or_404()
    
    # Increment visit count
    user.visit_count += 1
    db.session.commit()

    posts = Posts.query.filter_by(username=username).all()
    return render_template('profile.html', categories=categories,user=user, posts=posts)


@app.route('/posts/<string:username>',methods=['GET'])
def posts(username):
    posts=Posts.query.filter_by(username=username).all()
    return render_template('user_posts.html',params=params,posts=posts,username=username)



@app.route('/user/<string:user_id>', methods=['GET', 'POST'])
def manage_user(user_id):
    categories = Categories.query.all()
    if 'user' not in session:
        return redirect('/login')
    
    current_user = Users.query.filter_by(username=session['user']).first()
    if current_user.role != 'admin' and current_user.user_id != int(user_id):
        flash('You do not have permission to perform this action.', 'danger')
        return redirect('/dashboard')
    
    user = Users.query.filter_by(user_id=user_id).first() if user_id != '0' else None
    is_admin = current_user.role == 'admin'
    
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        uname = request.form.get('uname')
        uemail = request.form.get('uemail')
        upass = request.form.get('upass')
        uphone_num = request.form.get('phone_num')
        role = request.form.get('role') if is_admin else 'user'

        if user_id == '0':  # Creating a new user
            if Users.query.filter_by(username=uname).first():
                flash("Username already exists", "danger")
                return render_template('edit_user.html', categories=categories,user=None, user_id='0', is_admin=is_admin)
            
            new_user = Users(fname=fname,lname=lname,username=uname, password=upass, phone_num=uphone_num, email=uemail, role=role)
            db.session.add(new_user)
            db.session.commit()
            flash('User created successfully.', 'success')
            return redirect('/dashboard')
        else:  # Editing an existing user
            if user:
                user.fname=fname
                user.lname=lname
                user.username = uname
                user.email = uemail
                user.phone_num = uphone_num
                user.password = upass
                if is_admin:
                    user.role = role
                db.session.commit()
                flash('User details updated successfully.', 'success')
            else:
                flash('User not found.', 'danger')
            return redirect('/dashboard')

    return render_template('edit_user.html',categories=categories, user=user, user_id=user_id, is_admin=is_admin,active_page='')




@app.route('/register', methods=['GET', 'POST'])
def register():
    categories = Categories.query.all()
    if request.method == 'POST':
        uname = request.form.get('uname')
        upass = request.form.get('upass')
        cupass = request.form.get('cupass')
        uemail = request.form.get('uemail')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        
        
        if Users.query.filter_by(username=uname).first():
            flash("Username already exists", "danger")
            return render_template('register.html')
        
        if upass != cupass:
            flash("Passwords do not match", "danger")
            return render_template('register.html')

        hashed_password = bcrypt.generate_password_hash(upass).decode('utf-8')
        

        new_user = Users(username=uname, password=hashed_password, fname=fname, lname=lname, email=uemail, role='user', phone_num='1234')
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully. You can now log in.', 'success')
        return redirect('/login')
    
    return render_template('register.html',categories=categories,active_page='')

@app.route('/login', methods=['GET', 'POST'])
def login():
    categories = Categories.query.all()
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('upass')

        if not username or not password:
            flash('Username and password are required', 'danger')
            return render_template('login.html')
        
        user = Users.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            session['user'] = user.username
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html',categories=categories,active_page='')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    userdb = Users.query.filter_by(username=session['user']).first()
    if userdb.role == 'admin':
        categories = Categories.query.all()
        users = Users.query.all()
        posts=Posts.query.all()
        return render_template('admin.html', params=params,posts=posts, users=users,categories=categories, user=userdb)
    else:
        posts = Posts.query.filter_by(user_id=userdb.user_id).all()
        return render_template('user_dashboard.html', params=params, posts=posts, user=userdb,active_page='dashboard')
    


@app.route("/delete_user/<string:user_id>", methods=['GET', 'POST'])
def delete_user(user_id):
    if 'user' in session:
        current_user = Users.query.filter_by(username=session['user']).first()
        if current_user.role == 'admin':
            user = Users.query.filter_by(user_id=user_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                flash('User deleted successfully.', 'success')
            else:
                flash('User not found.', 'danger')
        else:
            flash('You do not have permission to delete this user.', 'danger')
        
        return redirect("/dashboard")
    else:
        flash('You need to be logged in to delete a user.', 'danger')
        return redirect("/dashboard")



# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#         file_url = f'/css/{filename}'

#         # You should specify the post_id appropriately
#         post_id = request.form.get('post_id')
#         if post_id:
#             media = Media(filename=filename, url=file_url, post_id=post_id)
#             db.session.add(media)
#             db.session.commit()

#         return jsonify({'url': file_url}), 200
#     else:
#         return jsonify({'error': 'Invalid file type'}), 400

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)




ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'file' not in request.files:
#         return jsonify(error='No file part'), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify(error='No selected file'), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         file_url = url_for('static', filename='css/' + filename)
#         return jsonify(url=file_url), 200
#     return jsonify(error='File not allowed'), 400


@app.route("/edit/<string:post_id>", methods=['GET', 'POST'])
def edit(post_id):
    categories = Categories.query.all()
    if 'user' not in session:
        flash('You need to be logged in to edit posts.', 'warning')
        return redirect('/login')
    
    current_user = Users.query.filter_by(username=session['user']).first()
    
    # Fetch the post if post_id is not 0 (indicating a new post)
    post = Posts.query.filter_by(post_id=post_id).first() if post_id != '0' else None

    if post_id != '0' and not post:
        flash('Post not found.', 'danger')
        return redirect('/dashboard')
    
    # Check if the current user is the author or an admin
    if post and (post.user_id != current_user.user_id and current_user.role != 'admin'):
        flash('You do not have permission to edit this post.', 'danger')
        return redirect('/dashboard')
    
    if request.method == "POST":
        box_title = request.form.get('title')
        tline = request.form.get('tagline')
        slug = request.form.get('slug')
        category = request.form.get('category')
        content = request.form.get('content')
        date = datetime.now()
        category = Categories.query.filter_by(name=category).first()
        category_id=category.id
        # print(category)
        if post_id == '0':
            # Create a new post
            new_post = Posts(
                title=box_title,
                slug=slug,
                category_id=category_id,
                content=content,
                tagline=tline,
                date=date,
                user_id=current_user.user_id  # Assign current user's ID
            )
            db.session.add(new_post)
            flash('New post created successfully.', 'success')
        else:
            # Update existing post
            post.title = box_title
            post.tagline = tline
            post.slug = slug
            post.category_id = category_id
            post.content = content
            post.date = date
            flash("Your post has been successfully updated.", "success")
        
        db.session.commit()
        return redirect('/dashboard')
    
    # Render the edit form with existing post data
    return render_template('edit.html', categories=categories,post=post, post_id=post_id,active_page='')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        file_url = f'/uploads/{filename}'

        return jsonify({'url': file_url}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)





if __name__ == "__main__":
    app.run(debug=True)
