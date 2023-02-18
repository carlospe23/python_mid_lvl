import logging

# FORMA DE USAR LOGS Y TESTEAR NUESTROS PROGRAMAS EN PYTHON

#TIPOS MENSAJES LOGGING 
#DEBUG => PARA TESTEAR => 10
#INFO => FLUJO NORMAL EJECUCION =>20
#WARNING => ALERTAS =>30
#ERROR => ERRORES PARA EXCEPCIONES =>40
#CRITICAL => EL PROGRAMA NO PUEDE CONTINUAR =>50

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s - %(processName)s', 
    filename='ejercicio.log', 
    filemode='a'
)

def get_current_price(id):
    logging.debug('Entramos a la funcion get_current price')

    response = id

    if response:
        logging.debug('La respuesta fue exitosa')

        return 'Exitosa'
    else:
        logging.warning('No fue posible una respuesta')

    return None


if __name__ == '__main__':

    response = get_current_price(1)
    logging.debug('Obtenemos una respuesta')

    logging.info(response)
