def calculate(cart):
    total=sum(cart.values())
    print(f"Total:{total}")
    if len(cart)>5:

        discount=total*0.9
        print(f"Discount amount:{discount}")
        total=total-discount
        print(f"Total amount after 15% discount:{total}")

    if total>=20000 and total<=50000:
        discount1=total*0.10
        print(f"Discount amount:{discount1}")
        total=total-discount1
        print(f"Total amount after 10% discount:{total}")
    if total>50000:
        discount=total*0.15
        print(f"Discount amount:{discount}")
        total=total-discount
        print(f"Total amount after 15% discount:{total}")

cart={'Laptop':50000,'Headphones':2000,'Mouse':16000,'Keyboard':1500,'Monitor':8000,'Drive':1000}
print(f"Cart items: {cart}")
print(calculate(cart))
