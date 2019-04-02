
#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from PIL import Image

batch_size = 16
mnist = tf.keras.datasets.mnist

# this is the augmentation configuration we will use for training
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

'''
this is a generator that will read pictures found in subfolers of 'data/train', and indefinitely generate
batches of augmented image data
'''
# train_generator = train_datagen.flow_from_directory(
#         'data/train',  # this is the target directory
#         target_size=(64, 64),  # all images will be resized to 64x64
#         batch_size=batch_size,
#         class_mode='categorical')  # since we use binary_crossentropy loss, we need binary labels

# # this is a similar generator, for validation data
# validation_generator = test_datagen.flow_from_directory(
#         'data/test',
#         target_size=(64, 64),
#         batch_size=batch_size,
#         class_mode='categorical')
# print(train_generator.class_indices)

model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation=tf.nn.relu),
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(32, (3, 3), activation=tf.nn.relu),
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),                                       # the model so far outputs 3D feature maps (height, width, features)
  tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu),
  tf.keras.layers.Flatten(),                                                            # this converts our 3D feature maps to 1D feature vectors
  tf.keras.layers.Dense(64, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(1, activation=tf.nn.sigmoid),
])

# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['accuracy'])
# model.summary()
# model.fit_generator(
#         train_generator,
#         steps_per_epoch=2000 // batch_size,
#         epochs=2,
#         validation_data=validation_generator,
#         validation_steps=800 // batch_size)
# model.save_weights('secondshit_try.h5')
model.load_weights('secondshit_try.h5')
img = tf.keras.preprocessing.image.load_img('data/test/non-vehicles/Far/image0019.png')  # this is a PIL image
x = tf.keras.preprocessing.image.img_to_array(img, 'channels_last')
x = x.reshape((1,) + x.shape)
print(model.predict(x))


# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# print((x_train, y_train), (x_test, y_test))
# x_train, x_test = x_train / 255.0, x_test / 255.0


# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# model.fit(x_train, y_train, epochs=5)

# model.evaluate(x_test, y_test)
# print(model)
