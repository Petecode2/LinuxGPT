from gpt4_integration import GPT4Integration

def main():
    gpt = GPT4Integration()

    query = "What is the capital of France?"
    gpt_response = gpt.get_response(query)

    print("GPT-4 Response:", gpt_response)

if __name__ == "__main__":
    main()
