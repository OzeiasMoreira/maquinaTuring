import json

def main():
    try: 
        with open("arquivo.json", "r") as arquivo_json:
            dados_json = json.load(arquivo_json)
    except FileNotFoundError:
        print("Erro: O arquivo 'arquivo.json' não foi encontrado.")
        return

    try:
        with open("entrada1.txt", "r") as arquivo_txt:
            entrada = arquivo_txt.readlines() 
    except FileNotFoundError:
        print("Erro: O arquivo 'entrada.txt' não foi encontrado.")
        return
    
    transicoes = dados_json['transitions']  
    transicoes_dict = {(t['from'], t['read']): t for t in transicoes} 
    simbolo_branco = dados_json['white'] 
    estados_finais = dados_json['final']  

    with open("saida.txt", "w") as arquivo_saida:
        for linha in entrada:
            
            fita = list(linha.strip())
            estado_atual = dados_json['initial'] 
            posicao_cabecote = 0 
            
            while estado_atual not in estados_finais:
        
                chave_transicao = (estado_atual, fita[posicao_cabecote])
                
                if chave_transicao in transicoes_dict:
                    transicao = transicoes_dict[chave_transicao]
                    print(f"Transição encontrada: {transicao}")
                    fita[posicao_cabecote] = transicao['write']
                    estado_atual = transicao['to']
                    
                    if transicao['dir'] == 'R':
                        posicao_cabecote += 1
                    elif transicao['dir'] == 'L':
                        posicao_cabecote -= 1
                    else:
                        print(f"Direção desconhecida: {transicao['dir']}")
                else:   
                    break  
        
                if posicao_cabecote < 0:
                    fita.insert(0, simbolo_branco)
                    posicao_cabecote = 0
                elif posicao_cabecote >= len(fita):
                    fita.append(simbolo_branco)

            arquivo_saida.write(''.join(fita) + '\n') 
    
        
            if estado_atual in estados_finais:
                print(1)  
            else:
                print(0)  

if __name__ == "__main__":
    main()