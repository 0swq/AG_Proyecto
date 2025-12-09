from datetime import datetime


def generar_numero_factura(prefijo="FAC", id=1):
    fecha_actual = datetime.now().strftime("%Y%m%d")
    numero_formateado = f"{prefijo}-{fecha_actual}-{id:05d}"
    return numero_formateado


def generar_numero_boleta(prefijo="BOL", id=1):
    fecha_actual = datetime.now().strftime("%Y%m%d")
    numero_formateado = f"{prefijo}-{fecha_actual}-{id:05d}"
    return numero_formateado


def generar_numero_comprobante(tipo_comprobante, prefijo=None, id=1):
    tipo = tipo_comprobante.lower().strip()

    if tipo == "factura":
        prefijo_final = prefijo if prefijo else "FAC"
        return generar_numero_factura(prefijo_final, id)
    elif tipo == "boleta":
        prefijo_final = prefijo if prefijo else "BOL"
        return generar_numero_boleta(prefijo_final, id)
    else:
        raise ValueError(f"Tipo de comprobante '{tipo_comprobante}' no válido. Use 'factura' o 'boleta'")