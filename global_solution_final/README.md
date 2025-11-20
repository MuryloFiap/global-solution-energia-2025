# Global Solution – Energia Sustentável e Futuro do Trabalho
## Ciências da Computação – 2º Semestre de 2025

### 1. Introdução
Este projeto mostra como tecnologias de análise de dados, Internet das Coisas (IoT) e energias renováveis podem tornar ambientes de trabalho mais eficientes, econômicos e sustentáveis.

A solução proposta utiliza dados simulados de consumo de energia ao longo de 24 horas, além de informações de temperatura e ocupação, para identificar desperdícios e propor melhorias.

---

### 2. Coleta e Análise de Dados
Foram utilizados **dados simulados** contendo:

- Horário (00h às 23h)
- Consumo de energia (kWh)
- Temperatura ambiente (°C)
- Ocupação do espaço (número de pessoas)

Com esses dados, foi possível:

- Calcular a **média diária de consumo**
- Identificar o **horário de pico**
- Estimar **desperdício energético** quando o consumo ultrapassa um limite crítico

Toda a análise é feita no arquivo `analise.py`.

---

### 3. Conexão com o Futuro do Trabalho
O futuro do trabalho exige ambientes:

- Mais automatizados
- Monitorados em tempo real
- Energeticamente eficientes
- Alinhados com práticas sustentáveis

A solução proposta se conecta a esse cenário ao mostrar como:

- Sensores (simulados) podem monitorar consumo em tempo real
- Um sistema inteligente pode agir automaticamente para reduzir desperdícios
- A integração com fontes renováveis reduz o impacto ambiental e os custos

---

### 4. Desenvolvimento da Solução

#### Opção A — Análise de Dados
No arquivo `analise.py`:

- São analisados os dados do arquivo `dados_consumo.csv`
- É calculada a média de consumo, o pico e o horário de maior uso
- É estimado um **desperdício energético** para consumos acima de 40 kWh
- É simulada uma redução de **18%** no consumo por meio de automação (IoT)

Um gráfico é gerado (`grafico_final.png`) comparando:

- Consumo atual
- Consumo com automação IoT
- Consumo com uso de energia solar

#### Opção B — Dispositivo IoT (simulado)
No arquivo `iot.py` temos um dispositivo IoT simulado que:

- Lê valores de consumo de energia (gerados aleatoriamente)
- Classifica o consumo como normal, de atenção ou crítico
- Toma decisões como:
  - Reduzir iluminação
  - Ajustar climatização
  - Desligar aparelhos ociosos

Isso representa um cenário real em que um sistema monitora o ambiente de trabalho e toma decisões para evitar desperdícios.

#### Opção C — Simulação de Uso de Energias Renováveis
Em `analise.py` também é simulada a **geração de energia solar** entre 08h e 16h:

- Parte do consumo é compensado por energia renovável
- O consumo final (`consumo_com_solar`) é reduzido
- É calculada a economia diária em kWh

---

### 5. Repositório no GitHub
O repositório está organizado com:

- `dados_consumo.csv` – dados simulados de consumo, temperatura e ocupação
- `analise.py` – análise de dados, automação IoT simulada e energia solar
- `iot.py` – simulação detalhada do dispositivo IoT
- `grafico_final.png` – gráfico comparando os cenários de consumo
- `README.md` – explicação da solução e orientações de execução

---

### 6. Como Executar

1. Ter Python instalado (3.x)
2. Instalar as dependências:

```bash
pip install pandas matplotlib
```

3. Executar a análise de dados:

```bash
python analise.py
```

4. Executar a simulação IoT:

```bash
python iot.py
```

---

### 7. Vídeo Explicativo
No vídeo (até 3 minutos), recomenda-se explicar:

- O problema de desperdício de energia em ambientes de trabalho
- Os dados utilizados e o que foi observado na análise
- Como o dispositivo IoT simulado atua para reduzir o consumo
- Como a simulação de energia renovável contribui para a sustentabilidade
- Que o repositório no GitHub está organizado com dados, códigos e instruções.

(Insira aqui o link do vídeo não listado no YouTube)
