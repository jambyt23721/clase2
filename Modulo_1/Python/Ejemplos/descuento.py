compra = float(input("Monto:"))
descuento = compra * 0.10
monto_total = compra - descuento
if compra > 100:
    print(f"Tienes un 10% de descuento, ya que tu compra es mayor a 100. Tu Monto a pagar es {monto_total}")
