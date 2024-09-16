from enum import Enum
from typing import Dict

class TwilioAccount(Enum):
    """Twilio account
    """
    TECLOGI= "TECLOGI"
    LOGGIAPP= "LOGGIAPP"

class MessageService(Enum):
    """Msg Service"""
    TECLOGI = 'MG8d5efcb11e6a0d5e07a31258a79db495'
    LOGGIAPP = 'MGa4312d9c551071df43c8cad0544f971d'
    LOGGIAPP_INNOVBO_TEST = 'MG74cadf3e25b877b49dbe67def90914d3'
    LOGGIAPP_INNOVBO_PROD = 'MGe0a7faae9e75b0db1d0b8152322e7c14'

class MsgTemplate(Enum):
    """MsgTemplate"""
    CUMPLIDOS = 'HXe3d937c0257fd9aa79df7bc07f5ddf4a'
    ENTURNAMIENTO = 'HXa1a9855e93336019ff45da21e3fa979e'
    OPTIN_TECLOGI = 'HXd137b96cb50396d540894ccba7a65ed3'
    OPTIN_LOGGIAPP_V1 = 'HX983a4779d1f5e01270cb008b0ce0f7a2'
    PRONTO_PAGO = 'HXc53fe78ba821f728d0712062b129748c'
    OPTIN_LOGGIAPP_V2 = 'HXa3c102f65900773c2e049198de2323cf'
    PUBLICACION_VIAJES = 'HXed664881a0219139426abf6a4c910702'


class TwilioVariables(Enum):
    """Viajes"""
    PELDAR: Dict[str, str] = {
            "tipo_vehiculo": "Mula o patinetas",
            "tipo_carroceria": "Plancha",
            "peso": "18 - 20 tons",
            "cubicaje": "0",
            "origen": "Cogua",
            "destino": "Barranquilla, Itagui y Bucaramanga",
            "fecha_viaje": "Hoy mismo",
            "obs": "Carpa, sobre carpa + 10 amarres",
            "telefono_contacto": "3157004161, 3184629850"
        }
