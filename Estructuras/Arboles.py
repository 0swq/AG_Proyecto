import Global.Global as Global


class Nodo_arbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def insertar(raiz, objeto, criterio='id'):
    if raiz is None:
        return Nodo_arbol(objeto)

    valor_actual = getattr(objeto, criterio)
    valor_raiz = getattr(raiz.valor, criterio)

    if valor_actual < valor_raiz:
        raiz.izquierda = insertar(raiz.izquierda, objeto, criterio)
    else:
        raiz.derecha = insertar(raiz.derecha, objeto, criterio)

    return raiz


def construir_arbol(lista_objetos, criterio='id'):
    raiz = None
    for objeto in lista_objetos:
        raiz = insertar(raiz, objeto, criterio)
    return raiz
def buscar(raiz, valor_buscado, criterio='id'):
    if raiz is None:
        return None

    valor_actual = getattr(raiz.valor, criterio)

    if valor_actual == valor_buscado:
        return raiz.valor
    elif valor_buscado < valor_actual:
        return buscar(raiz.izquierda, valor_buscado, criterio)
    else:
        return buscar(raiz.derecha, valor_buscado, criterio)
