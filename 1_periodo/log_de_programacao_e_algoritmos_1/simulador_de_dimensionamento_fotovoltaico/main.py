def coletar_dados_cliente():
    print("---coleta de dados (CRM) ---")
    nome = input("digite onome do cliente: ")
    consumo = float(input("digite o consumo memsal médio (kwh): "))
    hsp = float(input("digite o HSP (horas de sol pleno) da região: "))
    return nome, consumo, hsp

def calcular_sistema(consumo, hsp, potencia_painel):
    #cálculo da quantidade de painéis
    #fórmula: (consumo /30) / (HSP * (potencia /1000) * eficiência)
    #eficiência padrão de 80% (0.8)
    potencia_kw. = pontecia_painel / 1000
    producao_diaria_necessaria = consumo /30
    qtd_paineis = producao_diaria_necessaria / (hsp * potencia_kw * 0.8)
    
    #arredondndo para cima, pois não existe meio painel
    qtd_final = int(qtd_paineis) + (1 if qtd_paineis % 1 > 0 else 0)
    
    #cálculo de custo  e payback (valores fictcíos para o milestone 1)
    # supondo R$ 4.50 por watt instalado e tarifa de R$ 0.95/kwh
    custo_total_ = qtd_final * potencia_painel * 4.50
    economia_mensal= consumo * 0.95
    payback_anos = custo_total_ / (economia_mensal * 12)
    
    return qtd_final,  custo_total_, payback_anos
    
#--- fluxo principal (main) ---
def main():
    print(" inciando milistone 1 -  arthur\n")
    
    # 1. chama o processamento ( o que seria o motor_solar.py)
    paineis, custo,  payback = calcular-sistema(consumo_mensal, hsp_local,  p_painel)
    
    #4. imprime  os resultados direto do terminal
    print("\n" "="*40)
    print(f "RESUMO DA ANÁLISE: {nome_cliente}")
    print("_" * 40)
    print(f"quantidade de painéis: {(paineis)}")
