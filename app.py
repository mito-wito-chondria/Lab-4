from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return 
def roll_combat (roll: int, result:str):
        i = [random.randit(1,20)]
        if i == 1:
            return result:'critical miss!'
        if i == 20:
            return result:'critical hit!'
        
        
if __name__ == "__main__":
    app.run(debug=True)