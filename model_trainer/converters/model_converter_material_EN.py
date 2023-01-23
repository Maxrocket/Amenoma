import os

from tensorflow.keras.layers import Input, Reshape, Dense, Dropout, Bidirectional, LSTM
from tensorflow.keras.layers.experimental.preprocessing import StringLookup
from tensorflow.keras.models import Model

from ArtScanner.MaterialInfo import MaterialsNameEN as MaterialsName
from model_trainer.mobilenetv3 import MobileNetV3_Small

import model_trainer.model_info as model_info

MaterialsNameEN = list(MaterialsName.keys())

characters = sorted(
    [
        *set(
            "".join(
                list(MaterialsNameEN)
                + list("0123456789")
            )
        )
    ]
)
char_to_num = StringLookup(
    vocabulary=list(characters), num_oov_indices=0, mask_token="")
num_to_char = StringLookup(
    vocabulary=char_to_num.get_vocabulary(), oov_token="", mask_token="", invert=True)

width = 384
height = 16
max_length = 40
input_shape = (width, height)

input_img = Input(
    shape=(input_shape[0], input_shape[1], 1), name="image", dtype="float32"
)
mobilenet = MobileNetV3_Small(
    (input_shape[0], input_shape[1], 1), 0, alpha=1.0, include_top=False
).build()
x = mobilenet(input_img)
new_shape = ((input_shape[0] // 8), (input_shape[1] // 8) * 576)
x = Reshape(target_shape=new_shape, name="reshape")(x)
x = Dense(96, activation="relu", name="dense1")(x)
x = Dropout(0.2)(x)

# RNNs
x = Bidirectional(LSTM(192, return_sequences=True, dropout=0.25))(x)
x = Bidirectional(LSTM(96, return_sequences=True, dropout=0.25))(x)

# Output layer
output = Dense(len(characters) + 2, activation="softmax", name="dense2")(x)

# Define the model
model = Model(inputs=[input_img], outputs=output, name="ocr_model_v1")
model.load_weights(os.path.join("..", model_info.MODEL_DIR, model_info.MATERIALS_MODEL_NAME_EN))


def convert():
    model.summary()
    model.save(os.path.join(model_info.OUTPUT_DIR,
                            f"material_model_EN_{model_info.MODEL_TARGET_VERSION}.h5"))
