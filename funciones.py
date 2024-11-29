import openpyxl
from openpyxl import Workbook

def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC)."""
    if altura <= 0:
        return None
    imc = peso / (altura ** 2)
    return imc

def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC)."""
    if altura <= 0:
        return None
    imc = peso / (altura ** 2)
    return imc
