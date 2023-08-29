# Libraries 
import streamlit as st
import pandas as pd
from langchain import OpenAI
from langchain import SQLDatabase
from langchain import SQLDatabaseChain          # Using Langchain Version = 0.0.242
import os
from sqlalchemy import create_engine
from streamlit_card import card
from streamlit_extras.grid import grid



os.environ['OPENAI_API_KEY'] = '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' # OpenAI API Key
llm = OpenAI(temperature = 0, verbose = False) 


excel_file = "Gen_AI_Glossary Sample.xlsx"
df = pd.read_excel(excel_file, sheet_name="Sheet1")

engine = create_engine('sqlite:///SampleDatabase.db')
table_name = os.path.splitext(excel_file)[0]
df.to_sql(table_name, engine, if_exists='replace', index=False)
engine.dispose()

sql_db = SQLDatabase.from_uri("sqlite:///SampleDatabase.db")
db_chain = SQLDatabaseChain.from_llm(llm, db=sql_db, verbose=True)


st.set_page_config(layout="wide")

# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.squarespace-cdn.com/content/v1/5d2c8662957f82000116912e/1617996155519-FYHLWSXE57QHRSI1O29T/banner1.png");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-size: 2000px 470px;
background-attachment: local;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# st.markdown(
#         """
#     <style>
#     .stApp {
#     background-image: url("https://www.stockbrokers.org.au/wp-content/uploads/SAFAAHeaderImage.jpg");
#     background-repeat: no-repeat;
    
#     background-size: 2000px 500px;
#     background-attachment: scroll;
#     }
#     </style>
#         """
#         , unsafe_allow_html=True
#     )



#CSS for Button Color
st.markdown(
        """
        <style>
        .stButton>button {
            color: #071D49; /* Change to your desired color */
            background: #e6ffff;
           
        }
        </style>
        """
        , unsafe_allow_html=True
    )



#CSS for Logo
st.markdown(
        """
        <style>
        .logo-container {
            position: absolute;
            top: -80px; /* Adjust the top position */
            left: 1600px; /* Adjust the left position */
            z-index: 999; /* Ensure the logo appears above other content */
        }
        .logo {
            width: 190px;
            height: 40px;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

# Logo in the corner
st.markdown(
        """
        <div class="logo-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/AbbVie_logo.svg/1280px-AbbVie_logo.svg.png" alt="Logo" class="logo">
        </div>
        """
        , unsafe_allow_html=True
    )



# Creating 2 tabs
tab1, tab2= st.tabs(["Discover Data", "Query the Data"])

#Tab 1
with tab1:
  
    my_grid = grid(1,1,3, vertical_align="bottom")

    my_grid.markdown("""
        <h1 style="text-align: left; color: #071D49; margin-left: 650px;">DATA DISCOVERABILITY</h1>
        """, unsafe_allow_html=True)
    
    my_grid.markdown("""<span style="color: #071D49;font-size: 32px;margin-left: 500px;">Discover the limitless possibilities of Abbvie's data ecosystem</span>""", unsafe_allow_html=True)
    
    my_grid.text("")
    
    query = my_grid.text_input("",value="", key='query_input',)

    if my_grid.button('Filter', key='submit_button'):
        
        if query=="HCP Attribute":
            card7 = card(title="HCP Attribute", text=["Description: Description: HCP universe for all onboarded brands along with their attributes and segment inforation","Data Owner:PCM-MathCo","Domain: HCP"],on_click=lambda: print("Selected"), styles={
        "card": {
            "width": "400px",
            "height": "200px",
            "border-radius":"0px",
            "background":"#66d9ff"}})
            #st.write(card4)
            # if True:
            #     st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 200px;">HCP Attribute Selected!.</span>', unsafe_allow_html=True)
            if card7:
                st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 200px;">HCP Attribute Selected!</span>', unsafe_allow_html=True)

        if query=="NBRx":

            card8 = card(title="NBRx", text=["Description: NBRx numbers at the weekend date level for both Abbvie and competitor brands","Data Owner:PCM-MathCo", "Domain: PCM Description",],on_click=lambda: print("Selected"),styles={
        "card": {
            "width": "400px",
            "height": "200px",
            "border-radius":"0px",
            "background":"#66d9ff"}})
            

        if query=="ISA Calls":
            card9 = card(title="ISA Calls", text=["Description: ","Data Owner:PCM-MathCo", "Domain: Promo Activity"],on_click=lambda: print("Selected"),styles={
        "card": {
            "width": "400px",
            "height": "200px",
            "border-radius":"0px",
            "background":"#66d9ff"}})
               


    if query=="":

        st.markdown("""<span style="color: #071D49;font-size: 22px;margin-left: 100px;">Click on the card to select. Then go to Query tab to ask questions</span>""", unsafe_allow_html=True)

        col1,col2,col3=st.columns(3)
        with col1:
            card1 = card(title="HCP Attribute", text=["Description: Description: HCP universe for all onboarded brands along with their attributes and segment inforation","Data Owner:PCM-MathCo","Domain: HCP"],on_click=lambda: print("Selected"), styles={
            "card": {
                "width": "400px",
                "height": "200px",
                "border-radius":"0px",
                "background":"#66d9ff"}})
            if card1:
                st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 180px;">HCP Attribute Selected!</span>', unsafe_allow_html=True)
        
        with col2:
            card2 = card(title="NBRx", text=["Description: NBRx numbers at the weekend date level for both Abbvie and competitor brands","Data Owner:PCM-MathCo", "Domain: PCM Description",],on_click=lambda: print("Selected"),styles={
            "card": {
                "width": "400px",
                "height": "200px",
                "border-radius":"0px",
                "background":"#66d9ff"}})
            if card2:
                st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 200px;">NBRx Selected!</span>', unsafe_allow_html=True)
        with col3:
            card3 = card(title="ISA Calls", text=["Description: ","Data Owner:PCM-MathCo", "Domain: Promo Activity"],on_click=lambda: print("Selected"),styles={
            "card": {
                "width": "400px",
                "height": "200px",
                "border-radius":"0px",
                "background":"#66d9ff"}})
            if card3:
                st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 200px;">ISA Calls Selected!</span>', unsafe_allow_html=True)
        
        col4,col5,col6=st.columns(3)
        with col4:
            card4 = card(title="HCP Attributes", text=["Description: Description: HCP universe for all onboarded brands along with their attributes and segment inforation","Data Owner:PCM-MathCo","Domain: HCP"],on_click=lambda: print("Selected"), styles={
            "card": {
                "width": "400px",
                "height": "200px",
                "border-radius":"0px",
                "background":"#66d9ff"}})
            if card4:
                st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 200px;">HCP Attribute Selected!</span>', unsafe_allow_html=True)
        
        with col5:
            card5 = card(title="NBRxs", text=["Description: NBRx numbers at the weekend date level for both Abbvie and competitor brands","Data Owner:PCM-MathCo", "Domain: PCM Description",],on_click=lambda: print("Selected"),styles={
            "card": {
                "width": "400px",
                "height": "200px",
                "border-radius":"0px",
                "background":"#66d9ff"}})
            if card5:
                st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 200px;">NBRx Selected!</span>', unsafe_allow_html=True)
        with col6:
            card6 = card(title="ISA Callss", text=["Description: ","Data Owner:PCM-MathCo", "Domain: Promo Activity"],on_click=lambda: print("Selected"),styles={
            "card": {
                "width": "400px",
                "height": "200px",
                "border-radius":"0px",
                "background":"#66d9ff"}})
            if card6:
                st.markdown('<span style="text-align: center;font-size: 20px;margin-left: 200px;">ISA Calls Selected!</span>', unsafe_allow_html=True)


#Tab 2
with tab2:

    my_grid = grid(1,1,3, vertical_align="bottom")

    my_grid.markdown("""
        <h1 style="text-align: left; color: #071D49; margin-left: 720px;">DATA TREASURY</h1>
        """, unsafe_allow_html=True)
    
    my_grid.markdown('<span style="color: #071D49;font-size: 32px;margin-left: 750px;">Ask Your Question.</span>', unsafe_allow_html=True)

    my_grid.text("")



    # Input box for user's query
    query1 = my_grid.text_input("",value="", key='query_input_1')





    # Add a button with styling
    if my_grid.button('Submit', key='submit_button_1'):
        # Add a loading indicator while processing
        with st.spinner("Processing..."):
            if query1=="":
                st.header("No Query Found")
            
            else:
            
                res = db_chain.run(query1)
                st.success("Response Generated")

                # Display the result
                st.write("\n")
                st.header("Result")
                # Display the text with wrapping
                st.text_area("",value=res)


   


