def calculate_blank_pages(n,m):
    if n < 0 or m < 0:
        return 0 
    # кол-во студентов умножаем на страницы
    else: return n * m
# кол-во студентов умножаем на кол-во страниц
print(calculate_blank_pages(3,3))
# кол-во стдентов не может быть отрицательным
print(calculate_blank_pages(-3,3))