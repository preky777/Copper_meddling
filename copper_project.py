import numpy as np
import streamlit as st
import re

# Set page layout to wide
st.set_page_config(layout="wide")

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

# Header with Icon and Italics
st.markdown("""
    <div style='text-align:center; padding: 20px; background-color: #f5f5f5; border-radius: 10px; margin-bottom: 20px;'>
        <h1 style='color:#000000; font-style: italic;'>
            <i class="fas fa-cogs" style='margin-right: 10px;'></i> Industrial Copper Modeling App
        </h1>
    </div>
""", unsafe_allow_html=True)





st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 3rem;
        
    }
    </style>
    """,unsafe_allow_html=True)




st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 32px;


}
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .stRadio [role=radiogroup]{
        align-items: center;
        justify-content: center;
    }
    </style>
""",unsafe_allow_html=True)

# Custom styling for centering the radio button heading
st.markdown("""
    <style>
    .radio-heading {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


# Add FontAwesome CSS
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)


# Header with Icon and Reduced Box Size with Italics
st.markdown("""
    <div style='text-align:center; padding: 10px; background-color: #f5f5f5; border-radius: 5px; margin: 0 auto 10px auto; max-width: 500px;'>
        <h3 style='color:#000000; font-style: italic;'>
            <i class="fas fa-sharp fa-light fa-wand-magic" style='margin-right: 10px;'></i> Select Prediction Type
        </h3>
    </div>
""", unsafe_allow_html=True)




prediction_type = st.radio("", ["***PREDICT SELLING PRICE*** :scales:", "***PREDICT STATUS*** :signal_strength:"], horizontal=True)













if prediction_type == "***PREDICT SELLING PRICE*** :scales:":
    # Your existing code for predicting selling price
    # Define the possible values for the dropdown menus
    status_options = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
    item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
    country_options = [28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
    application_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
    product = ['611112', '611728', '628112', '628117', '628377', '640400', '640405', '640665',
              '611993', '929423819', '1282007633', '1332077137', '164141591', '164336407',
              '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662',
              '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738',
              '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']

    # Define the widgets for user input
    # Apply custom styling to the form
    st.markdown("""
        <style>
        div[data-baseweb="form-control"] {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)
    with st.form("my_form"):

        col1, col2, col3 = st.columns([5, 2, 5])
        with col1:
            st.write(' ')
            st.write(' ')
            status = st.selectbox("*Status*", status_options, key=1)
            item_type = st.selectbox("*Item Type*", item_type_options, key=2)
            country = st.selectbox("*Country*", sorted(country_options), key=3)
            application = st.selectbox("*Application*", sorted(application_options), key=4)
            product_ref = st.selectbox("*Product Reference*", product, key=5)
        with col3:
            st.write(
                '<h5 style="color: #000000; font-style: italic; background-color: #f5f5f5; padding: 8px; border-radius: 4px; margin: 0 auto 10px auto; max-width: 550px;text-align: center;">NOTE: Range is given use it to enter the value</h5>',
                unsafe_allow_html=True)
            st.write(' ')
            quantity_tons = st.text_input("*Enter Quantity Tons (Range => 611728 - 1722207579)*")
            thickness = st.text_input("*Enter thickness (Range => 0.18 - 400)*")
            width = st.text_input("*Enter width (Range => 1 - 2990)*")
            customer = st.text_input("*customer ID (Range => 12458 - 30408185)*")
            submit_button = st.form_submit_button(label=" *CLICK TO PREDICT SELLING PRICE* ")
            st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: #f5f5f5;
                    color: #000000;
                    width: 40%;
                }
                </style>
            """, unsafe_allow_html=True)

        flag = 0
        pattern = "^(?:\d+|\d*\.\d+)$"
        for i in [quantity_tons, thickness, width, customer]:
            if re.match(pattern, i):
                pass
            else:
                flag = 1
                break

    if submit_button:
        if flag == 1:
            if len(i) == 0:
                st.write("*Please enter a valid number. Spaces are not allowed.*")
            else:
                st.write("*You have entered an invalid value: *", i)
        elif not (611728 <= float(quantity_tons) <= 1722207579 and 0.18 <= float(thickness) <= 400 and 1 <= float(width) <= 2990 and 12458 <= float(customer) <= 30408185):
            st.write("*Please enter values within the specified range.*")

        else:
            import pickle

            # Load models and preprocessors
            with open("model.pkl", 'rb') as file:
                loaded_model = pickle.load(file)
            with open('scaler.pkl', 'rb') as f:
                scaler_loaded = pickle.load(f)
            with open("t.pkl", 'rb') as f:
                t_loaded = pickle.load(f)
            with open("s.pkl", 'rb') as f:
                s_loaded = pickle.load(f)

            # Prepare input for prediction
            new_sample = np.array([[np.log(float(quantity_tons)), application, np.log(float(thickness)),
                                    float(width), country, float(customer), int(product_ref), item_type, status]])
            new_sample_ohe = t_loaded.transform(new_sample[:, [7]]).toarray()
            new_sample_be = s_loaded.transform(new_sample[:, [8]]).toarray()
            new_sample = np.concatenate((new_sample[:, [0, 1, 2, 3, 4, 5, 6, ]], new_sample_ohe, new_sample_be), axis=1)
            new_sample1 = scaler_loaded.transform(new_sample)
            new_pred = loaded_model.predict(new_sample1)[0]
            st.write(
                '## <div style="color: black; background-color: white; padding: 5px; border-radius: 10px; margin: 0 auto 7px auto; max-width: 450px; text-align: center;">*Predicted selling price: {}*</div>'.format(
                    np.exp(new_pred)), unsafe_allow_html=True)


if prediction_type == "***PREDICT STATUS*** :signal_strength:":

    # Define the possible values for the dropdown menus
    status_options = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
    item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
    country_options = [28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
    application_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
    product = ['611112', '611728', '628112', '628117', '628377', '640400', '640405', '640665',
              '611993', '929423819', '1282007633', '1332077137', '164141591', '164336407',
              '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662',
              '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738',
              '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']
    
    # Your existing code for predicting status
    with st.form("my_form1"):
        c1, c2, c3 = st.columns([5, 1, 5])
        with c3:
            st.write(
                '<h5 style="color: #000000; font-style: italic; background-color: #f5f5f5; padding: 8px; border-radius: 4px; margin: 0 auto 10px auto; max-width: 550px;text-align: center;">NOTE: Range is given use it to enter the value</h5>',
                unsafe_allow_html=True)
            st.write(' ')
            cquantity_tons = st.text_input("*Enter Quantity Tons (Range => 611728 - 1722207579)*")
            cthickness = st.text_input("*Enter thickness (Range => 0.18 - 400)*")
            cwidth = st.text_input("*Enter width (Range => 1 - 2990)*")
            ccustomer = st.text_input("*customer ID (Range => 12458 - 30408185)*")
            cselling = st.text_input("*Selling Price (Range => 1 - 100001015)*")
            csubmit_button = st.form_submit_button(label="*CLICK TO PREDICT STATUS*")

            # Apply custom styling to the submit button
            st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: #f5f5f5;
                    color: black;
                    width: 30%;
                    margin: 0;
                }
                </style>
            """, unsafe_allow_html=True)

        with c1:
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')

            citem_type = st.selectbox("*Item Type*", item_type_options, key=21)
            ccountry = st.selectbox("*Country*", sorted(country_options), key=31)
            capplication = st.selectbox("*Application*", sorted(application_options), key=41)
            cproduct_ref = st.selectbox("*Product Reference*", product, key=51)

        cflag = 0
        pattern = "^(?:\d+|\d*\.\d+)$"
        for k in [cquantity_tons, cthickness, cwidth, ccustomer, cselling]:
            if re.match(pattern, k):
                pass
            else:
                cflag = 1
                break

    if csubmit_button:
        if cflag == 1:
            st.write("*Please enter valid numeric values. Spaces are not allowed.*")
        elif not (611728 <= float(cquantity_tons) <= 1722207579 and 0.18 <= float(cthickness) <= 400
                and 1 <= float(cwidth) <= 2990 and 12458 <= float(ccustomer) <= 30408185
                and 1 <= float(cselling) <= 100001015):
            st.write("*Entered values are out of the specified range.*")
        else:
            import pickle

            # Load models and preprocessors
            with open("cmodel.pkl", 'rb') as file:
                cloaded_model = pickle.load(file)
            with open('cscaler.pkl', 'rb') as f:
                cscaler_loaded = pickle.load(f)
            with open("ct.pkl", 'rb') as f:
                ct_loaded = pickle.load(f)

            # Prepare input for prediction
            new_sample = np.array([[np.log(float(cquantity_tons)), np.log(float(cselling)), capplication,
                                    np.log(float(cthickness)), float(cwidth), ccountry, int(ccustomer), int(cproduct_ref),
                                    citem_type]])
            new_sample_ohe = ct_loaded.transform(new_sample[:, [8]]).toarray()
            new_sample = np.concatenate((new_sample[:, [0, 1, 2, 3, 4, 5, 6, 7]], new_sample_ohe), axis=1)
            new_sample = cscaler_loaded.transform(new_sample)
            new_pred = cloaded_model.predict(new_sample)
            if new_pred == 1:
                st.write(
                    '## <div style="color: black; background-color: white; padding: 5px; border-radius: 10px; margin: 0 auto 7px auto; max-width: 450px; text-align: center;">*The Status is Won*</div>',
                    unsafe_allow_html=True)
            else:
                st.write(
                    '## <div style="color: black; background-color: white; padding: 5px; border-radius: 10px; margin: 0 auto 7px auto; max-width: 450px; text-align: center;">*The Status is Lost*</div>',
                    unsafe_allow_html=True)
