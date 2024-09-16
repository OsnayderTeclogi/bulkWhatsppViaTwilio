import os
import csv
import re
import json
from dotenv import load_dotenv
from twilio.rest import Client
from config import TwilioAccount, MessageService, MsgTemplate, TwilioVariables


load_dotenv()

ALL_CREDS = {
    "TECLOGI":{
        "account": os.environ.get('TECLOGI_ACCOUNT_SID'),
        "token": os.environ.get('TECLOGI_AUTH_TOKEN')
    },
    "LOGGIAPP":{
        "account": os.environ.get('LOGGIAPP_INNNOVBO_ACCOUNT_SID'),
        "token": os.environ.get('LOGGIAPP_INNNOVBO_TOKEN')
    }
}

# ____________________________________________________________________
# __________________________ PARÁMETROS ______________________________

CONTENT_SID = MsgTemplate.PUBLICACION_VIAJES
MESSAGE_SERVICE_ID = MessageService.TECLOGI
TWILIO_ACCOUNT = TwilioAccount.TECLOGI
CSV_FILE_PATH = "./data/os.csv" # Esta es la ubicación del listado de telefonos
COMPANY = "TECLOGI" # Estes es el nombre de la empresa de transporte
VARIABLES = TwilioVariables.PELDAR

# ☝️________________________ PARÁMETROS _____________________________☝️
# _____________________________________________________________________

ACCOUNT_CREDS = ALL_CREDS[TWILIO_ACCOUNT.value]
client = Client(ACCOUNT_CREDS["account"], ACCOUNT_CREDS["token"])


def main():
    """Main"""
    with open('results.csv', 'w', newline='', encoding="utf8") as file_csv:
        colums = ["name",
                    "phone",
                    "error_code",
                    "error_message",
                    "sid",
                    "status",
                    "date_sent"]
        writer_csv = csv.DictWriter(file_csv, fieldnames=colums)

        writer_csv.writeheader()

        contacts = get_contacts()
        for contact in contacts:

            response = send_message(contact["phone"], contact["name"])
            writer_csv.writerow({
                "name": contact["name"],
                "phone": contact["phone"],
                "error_code": response["error_code"],
                "error_message": response["error_message"],
                "sid": response["sid"],
                "status": response["status"],
                "date_sent": response["date_sent"]
            })
            print(f'Sent to {contact["phone"]}')
    print('Proceso completado')


def get_contacts() -> list:
    """Lee el csv de contactos y convierte en un listado de objetos

    Returns:
        list: Una lista de {"name":"nombre", "phone":"573000002233}
    """
    contacts = []

    with open(CSV_FILE_PATH, 'r', encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            contacts.append({
                "name": row[0],
                "phone": row[1]
            })

    return contacts


def send_message(phone: str, user_name: str = ""):
    """Send message"""
    response = {
        "error_code": "",
        "error_message": "",
        "sid": "",
        "status": "",
        "date_sent": "",
    }

    try:
        message = client.messages \
            .create(
                    content_sid=CONTENT_SID.value,
                    from_=MESSAGE_SERVICE_ID.value,
                    to=f'whatsapp:+{phone}',
                    content_variables=json.dumps(VARIABLES.value),
                    )

        response = {
            "error_code": message.error_code,
            "error_message": message.error_message,
            "sid": message.sid,
            "status": message.status,
            "date_sent": message.date_sent,
        }
    except Exception as e: # pylint: disable=broad-exception-caught

        patron = re.compile(
            r'Twilio returned the following information:(.*?)More information may be available here:', # pylint: disable=line-too-long
            re.DOTALL
        )

        coincidencias = patron.search(str(e))

        if coincidencias:
            informacion = coincidencias.group(1).strip()
            informacion_sin_saltos = informacion.replace('\n', '')
            response["error_message"] = informacion_sin_saltos
        else:
            print("No se encontró la información.")
            response["error_message"] = "other error"

    return response


if __name__ == "__main__":
    main()
    print('Proceso terminado')
