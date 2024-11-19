from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def homepage():
    return "<h1> seja bem vindo welcame, dine</h1>"

serve()

