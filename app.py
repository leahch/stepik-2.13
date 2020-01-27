from flask import Flask, g, request, render_template

import data as data

app = Flask(__name__)

# step 1
# – главной /, (выведите здесь будет главная)
# – направления /from/<direction> (выведите здесь будет направление)
# – тура /tours/<id>/ (выведите здесь будет тур)

# step 3
# – index.html для главной
# – direction.html для направления
# – tour.html для тура

@app.route('/')
def index():
    '''index route
    '''
    tours = [t for t in data.tours.items()][:6]
    return render_template('index.html', data=data, tours=tours)
#    return 'здесь будет главная'

@app.route('/from/<direction>/')
def direction(direction):
    '''direction route
    '''
    tours = [t for t in data.tours.items() if t[1].get("departure","") == direction]
    stat = {}
    if tours:
        stat["min_price"] = min([t["price"] for _,t in tours])
        stat["max_price"] = max([t["price"] for _,t in tours])
        stat["min_nights"] = min([t["nights"] for _,t in tours])
        stat["max_nights"] = max([t["nights"] for _,t in tours])
    return render_template('direction.html', data=data, direction=direction, tours=tours, stat=stat)
#    return 'здесь будет направление: ' + direction

@app.route('/tours/<int:id>/')
def tour(id):
    '''Tour route
    '''
    tour = data.tours.get(id, dict())
    return render_template('tour.html', tour=tour, data=data)
#    return 'здесь будет тур: ' + id

if __name__ == '__main__':
    # app.config['DEBUG'] = True
    app.run('0.0.0.0', 8000)
