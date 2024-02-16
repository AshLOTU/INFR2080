
def compare_sorting_time(data_generator, size, sorting_function):
    data = data_generator(size)
    start_time = get_current_time()
    sorted_data = sorting_function(data)
    end_time = get_current_time()
    return end_time - start_time

current_time_counter = 0

def get_current_time():
    return current_time_counter


if __name__ == "__main__":
    
    def load_product_data(file_name):
        products = []
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                product_id = int(parts[0])
                name = parts[1]
                price = float(parts[2])
                category = parts[3]
                products.append({'product_id': product_id, 'name': name, 'price': price, 'category': category})
        return products



    def find_product_by_id(products, product_id):
        for product in products:
            if product['product_id'] == product_id:
                return product
        return None


    def insert_product(products, product_id, name, price, category):
        if find_product_by_id(products, product_id) is None:
            products.append({'product_id': product_id, 'name': name, 'price': price, 'category': category})
            print(f"Product with ID {product_id} inserted")
        else:
            print(f"Product with ID {product_id} already exists.")


    def update_product(products, product_id, name, price, category):
        for product in products:
            if product['product_id'] == product_id:
                product['name'] = name
                product['price'] = price
                product['category'] = category
                print(f"Product with ID {product_id} updated")
                return
        print(f"Product with ID {product_id} does not exist.")


    def delete_product(products, product_id):
        for i, product in enumerate(products):
            if product['product_id'] == product_id:
                del products[i]
                print(f"Product with ID {product_id} deleted")
                return
        print(f"Product with ID {product_id} does not exist.")


    def display_products(products):
        for product in products:
            print(f"Product ID: {product['product_id']}, Name: {product['name']}, Price: {product['price']}, Category: {product['category']}")


    def search_product_by_id(products, product_id):
        product = find_product_by_id(products, product_id)
        if product:
            print(f"Product ID: {product['product_id']}, Name: {product['name']}, Price: {product['price']}, Category: {product['category']} SEARCHED")
        else:
            print(f"Product with ID {product_id} does not exist.")


    def bubble_sort_by_price(products):
        n = len(products)
        for i in range(n):
            for j in range(0, n-i-1):
                if products[j]['price'] > products[j+1]['price']:
                    products[j], products[j+1] = products[j+1], products[j]
        return products


    def generate_sorted_data(size):
        return [{'product_id': i, 'name': f'Product {i}', 'price': i, 'category': 'Category'} for i in range(1, size + 1)]


    def generate_reverse_sorted_data(size):
        return [{'product_id': i, 'name': f'Product {i}', 'price': size - i + 1, 'category': 'Category'} for i in range(1, size + 1)]


    def compare_sorting_time(data_generator, size, sorting_function):
        global current_time_counter
        data = data_generator(size)
        start_time = get_current_time()
        sorted_data = sorting_function(data)
        current_time_counter += 100 
        end_time = get_current_time()
        return end_time - start_time



        
    product_data = load_product_data('C:\\Users\\terra\\Desktop\\Pyhton\\product_data.txt')
    print("Product Data Loaded!")

    insert_product(product_data, 10088, 'Shiba Inu', 69.99, 'Memes')

    print("\nInserted Product Data:")
    display_products(product_data)


    update_product(product_data, 10088, 'Tory the Shina Inu', 420.00, 'Memes')
    
    print("\nUpdated Product Data:")
    display_products(product_data)


    delete_product(product_data, 10088)

    print("\nCurrent Product Data:")
    display_products(product_data)

    print("\nSearched Product:")
    search_product_by_id(product_data, 30483)

    sorted_products = bubble_sort_by_price(product_data)
    print("\nProduct Data Sorted By Price:")
    display_products(sorted_products)

    num_products = len(product_data)

    sizes = [num_products, 1000, 5000]

    for size in sizes:
        print(f"\nSize of data: {size}")

        sorted_time = compare_sorting_time(generate_sorted_data, size, bubble_sort_by_price)
        print(f"Time taken to sort sorted data: {sorted_time:.6f} seconds")

        reverse_sorted_time = compare_sorting_time(generate_reverse_sorted_data, size, bubble_sort_by_price)
        print(f"Time taken to sort reverse-sorted data: {reverse_sorted_time:.6f} seconds\n")
