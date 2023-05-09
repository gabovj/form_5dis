from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import google.auth
from gsheetsdb import connect
from google.oauth2 import service_account
import streamlit as st


# Google connection
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)
sheet_url = st.secrets["private_gsheets_url"]
sheet_id = sheet_url.split("/")[5]

# Function to write data to the Google Sheet


def write_data(sheet_id, range_name, data):
    try:
        service = build('sheets', 'v4', credentials=credentials)
        body = {
            'values': data
        }
        result = service.spreadsheets().values().append(
            spreadsheetId=sheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
        print(f'{result.get("updates").get("updatedCells")} cells appended.')
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None


def all_fields_filled():
    return all([empresa, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
                q12, q13, q14, q15, q16, q17, q18, q19, q20, q21])


# Reemplaza la siguiente línea con la URL de tu logo
logo_url = "https://neuvaimages.s3.us-west-2.amazonaws.com/E+-+Naranja+(Medium)Expectativa+(1).png"

st.image(logo_url, width=100)
# st.title("Test: Las Cinco Disfunciones de un equipo")
# st.subheader(
#     "Test basado en Las Cinco Disfunciones de un equipo de Patrick Lencioni.")


def all_fields_filled():
    return all([empresa, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
                q12, q13, q14, q15, q16, q17, q18, q19, q20, q21])


# Create a placeholder for the form
form_placeholder = st.empty()

with form_placeholder.form("test_form"):
    st.title("Test: Las Cinco Disfunciones de un equipo")
    st.subheader(
        "Test basado en Las Cinco Disfunciones de un equipo de Patrick Lencioni.")
    empresa = st.text_input("1. Empresa a la que pertenezco:")
    answer_type = ["1", "2", "3"]
    st.write(
        ":loudspeaker: :loudspeaker: Responde las preguntas, donde 1 = RARA VEZ y 3 = USUALMENTE :exclamation: :exclamation:")
    q1 = st.radio(
        "1\. Los miembros del equipo son abiertos y apasionados al discutir temas laborales:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q1 =int(q1)
    q2 = st.radio(
        "2\. Los miembros del equipo expresan las deficiencias y bajas de productividad de sus compañeros:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q2 =int(q2)
    q3 = st.radio(
        "3\. Los miembros del equipo saben en que están trabajando sus compañeros y cómo contribuyen en el logro de las metas:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q3 =int(q3)
    q4 = st.radio(
        "4\. Los miembros del equipo se disculpan rápida y genuinamente cuando dicen o hacen algo inapropiado o que pueda lastimar al equipo:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q4 =int(q4)
    q5 = st.radio(
        "5\. Los miembros del equipo están dispuestos a hacer sacrificios (presupuesto, territorio, plantilla) en sus departamentos por el bienestar del equipo:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q5 =int(q5)
    q6 = st.radio(
        "6\. Los miembros del equipo admiten abiertamente sus debilidades y errores:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q6 =int(q6)
    q7 = st.radio(
        "7\. Las juntas en la empresa son interesantes y no aburridas:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q7 =int(q7)
    q8 = st.radio(
        "8\. Los miembros del equipo salen de las juntas seguros de que sus compañeros están comprometidos con los acuerdos, aún cuando en la discusión estaban en desacuerdo:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q8 =int(q8)
    q9 = st.radio(
        "9\. El equipo se desmotiva cuando no se consiguen las metas grupales:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q9 =int(q9)
    q10 = st.radio(
        "10\. Durante las juntas, los temas más importantes y complicados se ponen en la mesa para ser discutidos y resueltos:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q10 =int(q10)
    q11 = st.radio(
        "11\. Los miembros del equipo se preocupan por no fallarle a sus compañeros:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q11 =int(q11)
    q12 = st.radio(
        "12\. Los miembros del equipo conocen detalles de la vida personal de sus compañeros y platican abiertamente sobre ello:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q12 =int(q12)
    q13 = st.radio(
        "13\. Los miembros del equipo terminan las discusiones con acuerdos claros y específicos y con planes de acción:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q13 =int(q13)
    q14 = st.radio(
        "14\. Los miembros del equipo desafían los planes y formas de sus compañeros:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q14 =int(q14)
    q15 = st.radio(
        "15\. Los miembros del equipo son más rápidos para dar crédito sobre los logros de los demás que sobre los propios:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q15 =int(q15)
    q16 = st.radio(
        "16\. Cuando hay una solicitud entre los compañeros o entre áreas se cumple en forma y tiempo:", answer_type, index=1, horizontal=True, help="1 = RARA VEZ y 3 = USUALMENTE", disabled=False)
    q16 =int(q16)
    q17 = st.text_input(
        "17\. ¿Qué palabra describiría mejor la interacción entre los miembros del equipo?:")
    q18 = st.selectbox("18\. Desde tu perspectiva ¿Cual es la tendencia del equipo de abordar el conflicto en función de la frecuencia y relevancia de los temas que se abordan?:", ("Frecuente - Irrelevante", "Poco frecuente - Irrelevante",
                                                                                                                                                                                     "Frecuente - Relevante", "Poco Frecuente - Relevantes"))
    answer_type2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    q19 = st.radio(
        "19\. ¿Qué tan dispuesto estarías a recomendar a tu equipo como un buen equipo para trabajar?:", answer_type2, index=0, horizontal=True, help="1 = NADA DISPUESTO y 3 = MUY DISPUESTO", disabled=False)
    q19 =int(q19)
    q20 = st.text_input(
        "20\. ¿Cuál es la causa principal de tu respuesta anterior?:")
    q21 = st.text_input(
        "21\. ¿Qué comportamiento podría cambiar el equipo para elevar su nivel de satisfacción y productividad?:")

    submitted = st.form_submit_button("Submit")
    if submitted:
        if all_fields_filled():
            # Write data to the Google Sheet
            range_name = 'A:U'
            data_to_write = [
                [empresa, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
                    q12, q13, q14, q15, q16, q17, q18, q19, q20, q21],
            ]

            write_data(sheet_id, range_name, data_to_write)
            # st.success("Form submitted successfully!")
            # Update the form placeholder with a thank you message
            form_placeholder.success("Test Enviado!")
        else:
            st.warning("Please fill in all fields before submitting.")


# streamlit_app.py
