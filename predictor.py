
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
print('Loading Model...')


model = load_model('./final_model')
print('Model loaded!')

def image_processor(filepath_string):
#     loading image
    x = load_img(filepath_string, target_size=(256,256))
#     saving to array
    x = img_to_array(x, data_format='channels_last')
#     reshaping to the correct size
    x = np.reshape(x, (1, 256, 256, 3 ))
    return x

def get_prediction(image_as_array):
    return int(model.predict_classes(image_as_array))

def output_statement(prediction):
    if prediction == 7:
        print("This is most likely a Maize/Corn plant, Do not pluck it!")
        return 1
    else:
        print('This is most likely a weed plant, Pluck it!')
        return 0

def output_func(image_file):

    image = image_processor(image_file)

    pred = get_prediction(image)

    return output_statement(pred)


def directory_predictor(num_of_pics, file_path='./seedlings/maize/'):
    weed_locations = []
    for i in range(num_of_pics):
        try:
            status = output_func(f'{file_path}{i}.png')
            print(i)
            if status == 0:
                weed_locations.append(i)
        except:
            pass
    print("Weed locations are at: " , weed_locations, len(weed_locations), "total weeds predicted!")

number_of_predictions = input("How many pictures need predictions?")
file_path = input("And What is the filepath?(start with a ./)")

if number_of_predictions == 1:
    output_func(file_path)
else:
    directory_predictor(int(number_of_predictions) + 1, file_path)
