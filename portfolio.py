from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def portfolio():
    if request.method=="POST":
        if request.form["text"]=="Arun Sharma" and request.form["password"]=="1305":
         return render_template("portfolio.html")
        else:
         return "Either the password or the username is incorrect-_-"
        
    return render_template("home.html")

if  __name__ == "__main__":
     app.run()
