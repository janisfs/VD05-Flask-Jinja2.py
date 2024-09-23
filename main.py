from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def my_main_page():
    context = {
        "number": 5,
        "list": ["john", "peter", "sara", "lisa"],
        "poem": [
            "Сижу за решёткой в темнице сырой.",
            "Вскормленный в неволе орёл молодой,",
            "Мой грустный товарищ, махая крылом,",
            "Кровавую пищу клюёт под окном,",
            "Клюёт, и бросает, и смотрит в окно,",
            "Как будто со мною задумал одно."
                ]
    }
    return render_template("shablon.html" , **context)

@app.route("/blog/")
def my_blog_page():
    return render_template("blog.html")

@app.route("/contacts/")
def my_contacts_page():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run()