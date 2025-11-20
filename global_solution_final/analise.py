import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados
dados = pd.read_csv("dados_consumo.csv")

# --- Análise básica ---
media = dados["consumo_kwh"].mean()
pico = dados["consumo_kwh"].max()
horario_pico = dados.loc[dados["consumo_kwh"].idxmax(), "horario"]

print("Média diária:", round(media, 2), "kWh")
print("Pico de consumo:", pico, "kWh")
print("Horário de pico:", horario_pico)

# --- Cálculo de desperdício ---
# Considerando que acima de 40 kWh é considerado consumo crítico para o ambiente
limite_critico = 40
consumo_critico = dados[dados["consumo_kwh"] > limite_critico]["consumo_kwh"].sum()
consumo_ajustado = len(dados[dados["consumo_kwh"] > limite_critico]) * limite_critico
desperdicio = consumo_critico - consumo_ajustado
print("Desperdício estimado:", round(desperdicio, 2), "kWh")

# --- Automação IoT (redução automática) ---
fator_economia = 0.18  # 18% de economia com automação
dados["consumo_otimizado"] = dados["consumo_kwh"] * (1 - fator_economia)

economia_total = dados["consumo_kwh"].sum() - dados["consumo_otimizado"].sum()
print("Economia estimada com IoT (kWh/dia):", round(economia_total, 2))

# --- Simulação de energia solar (Opção C) ---
# Considerando geração solar entre 08h e 16h
geracao_solar = [0,0,0,0,0,0,2,5,8,10,12,13,14,14,13,10,7,0,0,0,0,0,0,0]
dados["geracao_solar"] = geracao_solar
dados["consumo_com_solar"] = dados["consumo_kwh"] - dados["geracao_solar"]

print("Economia com energia solar:", dados["geracao_solar"].sum(), "kWh/dia")

# --- Gráfico ---
plt.figure(figsize=(12,6))
plt.plot(dados["horario"], dados["consumo_kwh"], label="Consumo atual")
plt.plot(dados["horario"], dados["consumo_otimizado"], label="Após IoT")
plt.plot(dados["horario"], dados["consumo_com_solar"], label="Com energia solar")
plt.xticks(rotation=90)
plt.xlabel("Horário")
plt.ylabel("Consumo (kWh)")
plt.legend()
plt.tight_layout()
plt.savefig("grafico_final.png")
print("Gráfico salvo como grafico_final.png")
