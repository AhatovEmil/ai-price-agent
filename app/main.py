from agent import PriceAgent


def main():

    agent = PriceAgent()

    print(agent.greet())

    while True:

        request = input("\n> ")

        if request.lower() == "exit":
            break

        result = agent.process_request(request)

        print()
        print(result.model_dump_json(indent=4))


if __name__ == "__main__":
    main()