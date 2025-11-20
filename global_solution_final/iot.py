import random
import time

def medir_consumo():
    # Simula um consumo entre 20 e 55 kWh
    return random.uniform(20, 55)

def atuador(consumo):
    if consumo > 45:
        return "⚠ Ação: Reduzindo iluminação e desligando aparelhos ociosos."
    elif consumo > 35:
        return "Atenção: Ajustando climatização para reduzir consumo."
    else:
        return "Consumo dentro do normal."

print("Simulação de dispositivo IoT para monitoramento de energia:\n")

for _ in range(10):
    consumo = medir_consumo()
    print(f"Consumo atual: {consumo:.2f} kWh")
    print(atuador(consumo))
    print("---")
    time.sleep(0.5)
