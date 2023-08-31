from flask import Flask, redirect, render_template_string, request
from hashids import Hashids

app = Flask(__name__)

hashids = Hashids(salt="This is a very very secured string")


def decode_string(encoded):
    decoded = "".join([chr(i) for i in hashids.decode(encoded)])
    return decoded


raw_html = """
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rushidhar1999 Redirect</title>
    <link rel="icon" href="https://i.slow.pics/vBpClAQI.webp">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous" />
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <style>
        .background{
            background-size: cover;
            background-color: black;
            text-align: center;
        }
        
        .normal{
            margin: auto;
            width: 65vw;
            height: 75vh;
            background-color: #1e1e1e;
            padding: 20px;
        }
        
        .space{
            height: 10vh;
        }
        
        .header{
            color: white;
            text-decoration: none;
        }
        
        .img {
          width: 50vw;
          height: 50vh;
          margin-top: 30px;
          margin-bottom: 30px;
        }
        
        .anchor {
            font-size: 30px;
            color: white;
            text-decoration: none;
        }
    </style>
  </head>
  <body class = "background">
    <div class = "space"></div>
    <div class = "normal">
        <div>
            <img class = "img" src = "https://i.slow.pics/vBpClAQI.webp" />
        </div>
        <a href="https://telegram.me/USE_FULL_BOTZ" class = "anchor" >USE FULL BOTZ</a>
        <h1 class = "header">..Redirecting..</h1>
        <script>
            setTimeout(function () {
                window.location.href = '{{ red_url }}';
            }, 5000);
        </script>
    </div>
  </body>
</html>
"""


# Redirect With Javascript (Support UI & Modification)


@app.route("/js")
def js_redirect():
    start_arg = request.args.get("start")
    bot_url = f"https://telegram.me/File_store_Rushidhar_3Bot?start={start_arg}"
    return render_template_string(raw_html, red_url=bot_url)


@app.route("/secured")
def js_enc_redirect():
    try:
        enc_start_arg = request.args.get("start")
        start_arg = decode_string(enc_start_arg)
        bot_url = f"https://telegram.me/File_store_Rushidhar_3Bot?start={start_arg}"
        return render_template_string(raw_html, red_url=bot_url)
    except BaseException:
        return "Invalid URL!"


# Normal Redirection


@app.route("/")
def home_redirect():
    try:
        start_arg = request.args.get("start")
        bot_url = f"https://telegram.me/File_store_Rushidhar_3Bot?start={start_arg}"
        return redirect(bot_url)
    except:
        return "<h1>Site Running</h1>"

if __name__ == "__main__":
    app.run()
