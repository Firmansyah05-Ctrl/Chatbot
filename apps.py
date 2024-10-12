#!flask/bin/python
from flask import Flask, jsonify, request
import pickle
app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
        #program inference ML/DL
        loaded_model = pickle.load(open('model.sav', 'rb'))
        #program input dari frontend
        User = int(request.args.get('User'))
        Device = int(request.args.get('Device'))
        Operating = int(request.args.get('Operating'))
        data_baru = [[3, 0, 393, 6.4, 1872, 67, 1122, 40, 1]]  # Google Pixel 5, Android, Male
        data_baru2 = [[User, Device, Operating, 4.7, 1331, 42, 944, 47, 0]]
        #program input dari frontend
        hasil = loaded_model.predict(data_baru2)[0]
        return str(hasil)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5880')
