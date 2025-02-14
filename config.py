from enum import Enum
from typing import Dict


class TwilioAccount(Enum):
    """Twilio account
    """
    TECLOGI = "TECLOGI"
    LOGGIAPP = "LOGGIAPP"


class MessageService(Enum):
    """Msg Service"""
    TECLOGI = 'MG8d5efcb11e6a0d5e07a31258a79db495'
    TECLOGI_TEST = 'MG1943ff4905f73f363e2b78f55a3dfddc'
    LOGGIAPP = 'MGa4312d9c551071df43c8cad0544f971d'
    LOGGIAPP_INNOVBO_TEST = 'MG74cadf3e25b877b49dbe67def90914d3'
    LOGGIAPP_INNOVBO_PROD = 'MGe0a7faae9e75b0db1d0b8152322e7c14'


class MsgTemplate(Enum):
    """MsgTemplate"""
    CUMPLIDOS = 'HXe3d937c0257fd9aa79df7bc07f5ddf4a'
    ENTURNAMIENTO = 'HX013743576c387cd8e865c4d73d6c3c19'
    OPTIN_TECLOGI = 'HX7051c8542a4dcfb89ac0f6b4eb830fb4'
    OPTIN_LOGGIAPP_V1 = 'HX983a4779d1f5e01270cb008b0ce0f7a2'
    PRONTO_PAGO = 'HXc53fe78ba821f728d0712062b129748c'
    OPTIN_LOGGIAPP_V2 = 'HXa3c102f65900773c2e049198de2323cf'
    PUBLICACION_VIAJES = 'HXed664881a0219139426abf6a4c910702'
    SEGURIDAD = 'HX47f13506972a396b155f624a4cd029db'
    ENTURNAMIENTO_BONO = 'HXfd556e7d73126c20a4d92a0720166591'
    ENTURNAMIENTO_BONO_CAMIONES = 'HX6f84e525a215aec20f12d6ca94e576d2'
    ENT_BONO_TRACTO_BOG_COSTA = 'HXc687a987911f5aa8a578650365c97301'
    ENT_BONO_NACIONAL_29_11 = 'HX68041d3035f9fd937c5021c47b902f20'
    TEMP = 'HX1fe20f2ea260991ff2c4e41eeb6e24c1'



class DestinationPhones(Enum):
    """DestinationPhones"""
    OS = "./data/os.csv"
    GINA = "./data/gina.csv"
    CAMIONES_Y_CAMIONETAS = "./data/camiones_y_camionetas.csv"
    GENERAL = "./data/general.csv"
    TRACTOCAMIONES = "./data/tractocamiones.csv"
    TRANSALUD = "./data/transalud.csv"
    TEMP = "./data/temp.csv"
    PRONTO_PAGO = "./data/pronto_pago.csv"
    CARRILLO = "./data/carrillo.csv"
    EXTREMA = "./data/extrema.csv"
    TRACTOCAMIONES_BUN = "./data/tractocamiones_bun.csv"
    PATINETAS = "./data/patinetas.csv"
    MULAS = "./data/mulas.csv"
    OPPERAR = "./data/opperar.csv"


class TwilioVariables(Enum):
    """Viajes"""
    USER_DATA: Dict[str, str] = {
        "name": "Daniela"
    }
    BUN_PALMIRA: Dict[str, str] = {
        "tipo_vehiculo": "Patineta",
        "tipo_carroceria": "Plancha",
        "peso": "_",
        "cubicaje": "_",
        "origen": "Buenaventura",
        "destino": "Palmira",
        "fecha_viaje": "_",
        "obs": "Puede aplicar pronto pago. Contrato por 1 año",
        "telefono_contacto": "3157004161, 3184629850"
    }
    ULTIMA: Dict[str, str] = {
        "tipo_vehiculo": "Sencillo",
        "tipo_carroceria": "Plancha",
        "peso": "9 ton",
        "cubicaje": "_",
        "origen": "Bogotá",
        "destino": "Bucaramanga",
        "fecha_viaje": "Hoy miércoles 16",
        "obs": "_",
        "telefono_contacto": "3112035526  - 3176581079"
    }

    OBS: Dict[str, str] = {
        "1": " ",
    }
