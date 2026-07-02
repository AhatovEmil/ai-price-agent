from agent import PriceAgent


def main():

    agent = PriceAgent()

    print(agent.greet())

    while True:

        request = input("\n> ")

        if request.lower() == "exit":
            break

        products = agent.process_request(request)

        print()
        print("========== RESULT ==========")

        if not products:
            print("Nothing found.")
            continue

        for index, product in enumerate(products, start=1):

            print(f"{index}. {product.title}")
            print(f"   Price : {product.price}")
            print(f"   Shop  : {product.shop}")
            print()

        print("============================")


if __name__ == "__main__":
    main()