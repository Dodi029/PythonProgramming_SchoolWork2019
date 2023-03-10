total_sales=int(input("구입 금액을 입력하시오."))
if total_sales>100000:
    discount=total_sales*0.05
    sales=total_sales-discount
    print("지불 금액은", sales,"원 입니다.")
else:
    price=100000-total_sales
    print("만약",price,"원 만큼 더 구입하시면 5%할인을 받을 수 있습니다.")
