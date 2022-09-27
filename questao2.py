nota1: float; nota2: float; nota3: float; media: float
nota1= float(input("Digite sua primeira nota: "))
nota2= float(input("Digite sua segunda nota: "))
nota3= float(input("Digite sua terceira nota: "))
media= (nota1 + nota2 + nota3)/3
if media>=0 and media<3:
    print("Reprovado!")
elif media>=3 and media<6:
    print(f"Recuperação, você deve tirar: {6-media} para passar.")
else:
    print("Aprovado!")