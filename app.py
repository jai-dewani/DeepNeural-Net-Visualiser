from json import load
import tensorflow as tf 
import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 

from flask import Flask, request

# app = Flask(__name__)
def load_model():
    model = tf.keras.models.load_model('model.h5')
    feature_model = tf.keras.models.Model(
        model.inputs,
        [layer.output for layer in model.layers]
    )
    _, (x_test, _ ) = tf.keras.datasets.mnist.load_data()
    x_test = x_test/255
    return feature_model, x_test

def get_prediction():
    index = np.random.choice(x_test.shape[0])
    image = x_test[index, :, :]
    image_arr = np.reshape(image, (1, 784))
    return feature_model.predict(image_arr), image


feature_model, x_test = load_model()
st.set_page_config(layout="wide")
st.title('Neural Network Visualizer')
st.sidebar.markdown('## Input Image')

if st.button('Get random prediction'):
	# response = requests.post(URL, data={})
	# response = json.loads(response.text)
	preds, image  = get_prediction()
	# image = response.get('image')
	image = np.reshape(image, (28,28))
	
	st.sidebar.image(image, width=200)
	# print(preds)
	for layer, p in enumerate(preds):
		print(len(p[0]),p)
		numbers = np.squeeze(np.array(p))

		a = plt.figure(figsize=(32,6))
		col = len(p[0])
		row = 1		
		for i, number in enumerate(numbers):
			ax = plt.subplot(row,col,i+1)
			plt.imshow(1 * np.ones((8,8,3)).astype('float32'))
			# ax = plt.subplots()
			cc = plt.Circle((4,4),4, color=str(number))
			ax.add_patch(cc)
			ax.spines['top'].set_visible(False)
			ax.spines['right'].set_visible(False)
			ax.spines['bottom'].set_visible(False)
			ax.spines['left'].set_visible(False)
			plt.xlim(0,8)
			plt.ylim(0,8)
			plt.xticks([])
			plt.yticks([])

			if layer == 2:
				plt.xlabel(str(i), fontsize=40)
			else:
				plt.xlabel(str(i), fontsize=20)
		
		plt.subplots_adjust(wspace=0.05, hspace=0.05)
		plt.tight_layout()
		st.text('Layer {}'.format(layer+1))
		st.pyplot(a)






# @app.route('/', methods=['GET','POST'])
# def index():
#     if request.method == "POST":
#         preds, image = get_prediction()
#         final_preds = [p.tolist() for p in preds]
#         return json.dumps({
#             'prediction': final_preds,
#             'image': image.tolist()
#         })
#     return "Welcome to Neural Network Visualization"

# if __name__=="__main__":
#     app.run()