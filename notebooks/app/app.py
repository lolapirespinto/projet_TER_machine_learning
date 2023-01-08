import imp
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open('model_classification.pkl', 'rb'))
print("------------------------------")
print(f'modèle = {model}')
print("------------------------------")
def predict():
    final_features = []
    print("entrez les valeurs des caractéristiques du téléphone\n\n-------")
    final_features.append(input("battery power : "))
    final_features.append(input("blue : "))
    final_features.append(input("clock_speed : "))
    final_features.append(input("dual_sim : "))
    final_features.append(input("fc : "))
    final_features.append(input("four_g : "))
    final_features.append(input("int_memory : "))
    final_features.append(input("m_dep : "))
    final_features.append(input("mobile_wt : "))
    final_features.append(input("n_cores : "))
    final_features.append(input("pc : "))
    final_features.append(input("px_height : "))
    final_features.append(input("px_width : "))
    final_features.append(input("ram : "))
    final_features.append(input("sc_h : "))
    final_features.append(input("sc_w : "))
    final_features.append(input("talk_time : "))
    final_features.append(input("three_g : "))
    final_features.append(input("touch_screen : "))
    final_features.append(input("wifi : "))

    prediction = model.predict([final_features])
    output = round(prediction[0], 2)
    return output

out = predict()
print(f'catégorie de prix : {out}')