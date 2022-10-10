import json

def statement(invoice, plays):

    total = 0
    creditos = 0

    with open(invoice, 'r') as file:
        faturamento = json.load(file)

    with open(plays, 'r') as file:
        cartaz = json.load(file)

    with open('fatura.txt', 'w') as fatura:

        fatura.write(f"Statement for {faturamento['customer']}\n")
        print(f"Statement for {faturamento['customer']}")

        for performance in faturamento['performances']:

            # simplify changes
            play_id = performance['playID']
            audience = performance['audience']

            custo_parcial = 0
            show = cartaz[play_id]

            match show['tipo']:

                case 'tragedy':
                    custo_parcial = 40_000
                    if audience > 30:
                        custo_parcial += 1_000 * (audience - 30)
                
                case 'comedy':
                    custo_parcial = 30_000
                    if audience > 20:
                        custo_parcial += 10_000 + 500 * (audience - 20)
                    custo_parcial += 300 * audience

                case _:
                    print(f"Unknown type: {show['tipo']}")

            creditos += max(audience - 30, 0)
            if audience == 'comedy':
                creditos += audience // 5
            
            fatura.write(f"  {play_id}: R$ {custo_parcial//100},00 ({audience} seats)\n")
            print(f"  {play_id}: R$ {custo_parcial//100},00 ({audience} seats)")
            total += custo_parcial

        fatura.write(f"Amount owed is R$ {total//100},00\n")
        fatura.write(f"You earned {creditos} credits\n")
        print(f"Amount owed is R$ {total//100},00")
        print(f"You earned {creditos} credits")

statement('faturamento.json', 'cartaz.json')