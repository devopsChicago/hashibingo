from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Generate a Bingo card
def generate_card():
    card = {}
    columns = {'B': range(1, 16), 'I': range(16, 31), 'N': range(31, 46), 'G': range(46, 61), 'O': range(61, 76)}
    for letter, nums in columns.items():
        card[letter] = random.sample(nums, 5)
    card['N'][2] = "FREE"  # Free space in the center
    return card

bingo_card = generate_card()
called_numbers = ["FREE"]  # Ensure the FREE space starts highlighted

@app.route('/')
def index():
    return render_template('bingo.html', card=bingo_card, called_numbers=called_numbers)

@app.route('/new_number')
def new_number():
    global called_numbers
    all_numbers = set(range(1, 76)) - set(called_numbers)
    if all_numbers:
        number = random.choice(list(all_numbers))
        called_numbers.append(number)
        return jsonify({'number': number})
    return jsonify({'number': None})

if __name__ == '__main__':
    app.run(debug=True)

