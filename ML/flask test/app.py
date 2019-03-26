from flask import Flask
import tensorflow as tf

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello():
    hello = tf.constant('Hello, TensorFlow! cccc def')
    sess = tf.Session()
    return sess.run(hello)
    # return 'Hello ajinomoto'

# if __name__ == '__main__':
#     app.run(debug=True, host = '0.0.0.0', port=5000)