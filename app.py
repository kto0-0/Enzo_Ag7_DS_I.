tipo_de_imóvel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").lower()
consumo_de_água = float(input("Digite o consumo mensal de água em m3: "))

if tipo_de_imóvel == "comercial":
    print("Tarifa comercial aplicada, consulte o plano corporativo.")
elif tipo_de_imóvel == "apartamento" and consumo_de_água <= 10:
    print("consumo econômico, excelente consumo de água.")
elif tipo_de_imóvel == "apartamento" or tipo_de_imóvel == "casa" and consumo_de_água <= 25:
    print("consumo moderado, dentro do padrão residencial.")
else :
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")