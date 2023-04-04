import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np

st.set_page_config(page_title = "YOLO Object Detection",
                   layout='wide',
                   page_icon='./images/object.png')

st.title('welcome to Yolo for image')
st.write('please upload image to get detections')

with st.spinner('please wait while the model is loading'):
    yolo = YOLO_Pred(onnx_model='./models/best.onnx',
                    data_yaml= './models/data.yaml')
    st.balloons()


def upload_image():
    image_file = st.file_uploader(label='Upload Image')
    if image_file is not None:
        size_mb = image_file.size/(1024**2)
        file_details = {"filename": image_file.name,
                        "filetype": image_file.type,
                        "filesize": "{:,.2f} MB".format(size_mb)}
        
        #st.json(file_details)

        if file_details['filetype'] in ('image/png','image/jpeg'):
            st.success('VALID IMAGE file type')
            return {"file_name": image_file, 
                    "details": file_details
                    }

        else:
            st.error('IVALID Image file type')
            st.error('UPload only png,jpg')
            return None
        
def main():
    object = upload_image()

    if object:
        prediction = False
        image_obj =Image.open(object['file_name'])
        st.image(image_obj)

        col1, col2 = st.columns(2)

        with col1:
            st.info('preview')
            st.image(image_obj)

        with col2:
            st.subheader('file detials')
            st.json(object['details'])
            button1 = st.button('Get Detection from Yolo')
            if button1:
                image_array=np.array(image_obj)
                pred_img = yolo.predictions(image_array)
                pred_img_obj = Image.fromarray(pred_img)
                prediction = True
                st.write("you")
                
        if prediction:
            st.image(pred_img_obj)


if __name__ == "__main__":
    main()

        