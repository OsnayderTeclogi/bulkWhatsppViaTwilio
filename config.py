from enum import Enum

message_service = {
    'TECLOGI': 'MG8d5efcb11e6a0d5e07a31258a79db495',
    'LOGGIAPP': 'MGa4312d9c551071df43c8cad0544f971d',
    'LOGGIAPP_INNOVBO_TEST': 'MG74cadf3e25b877b49dbe67def90914d3',
    'LOGGIAPP_INNOVBO_PROD': 'MGe0a7faae9e75b0db1d0b8152322e7c14'
}

template = {
    'cumplidos': 'HXe3d937c0257fd9aa79df7bc07f5ddf4a',
    'enturnamiento': 'HXa1a9855e93336019ff45da21e3fa979e',
    'optin': 'HXd137b96cb50396d540894ccba7a65ed3',
    'optin_loggiapp': 'HX983a4779d1f5e01270cb008b0ce0f7a2',
    'status_rndc': 'HXa27becc36e25ec04470ccf85782baaca',
    'atriles': 'HX03c82efef011e9f573a1ad6b372ea2ec',
    'bun_tractocamion_pronto_pago': 'HX2cd5fb6dd3aecf760cb38146f8a7716c',
    'pronto_pago': 'HXc53fe78ba821f728d0712062b129748c',
    'publicacion_viajes': 'HXfb3e243ab1b6952539b00e662fab6b12',
    'viruela': 'HXdc0dde7f1a52f98a2466ac79e84f1b59', 
    'optin_loggiapp_innovbo': 'HXa3c102f65900773c2e049198de2323cf'
}

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
    PUBLICACION_VIAJES = 'HX6357333f1fa5dac221b00b86d961a223'
