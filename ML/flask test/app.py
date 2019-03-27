from flask import Flask
# import os
import tensorflow as tf

app = Flask(__name__)

# extra_dirs = ['E:\2CS\Intern\python_study\ML\flask test\app.py',]
# extra_files = extra_dirs[:]
# for extra_dir in extra_dirs:
#     for dirname, dirs, files in os.walk(extra_dir):
#         for filename in files:
#             filename = os.path.join(dirname, filename)
#             if os.path.isfile(filename):
#                 extra_files.append(filename)

@app.route('/')
# @app.route('/hello')
def hello():
    hello = tf.constant('Hello, Tnsow! ddaa')
    sess = tf.Session()
    return sess.run(hello)
    # return 'Hello ajinomoto'

# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port=5000)