import random
import googlesearch

google_API='GCP2452'

# Create a list of possible responses
responses = ["Hi there! How can I help you today?", "What can I do for you?", "What's on your mind?"]

# Create a function to generate a random response
def generate_response(user_input):
    # Get the length of the list of responses
    num_responses = len(responses)

    # Choose a random response
    response_index = random.randint(0, num_responses - 1)

    # Return the random response
    return responses[response_index]

# Create a function to chat with the user
def chat():
    # Get the user's input
    user_input = input("What would you like to talk about? ")

    # Check if the user wants to quit
    if user_input == "quit":
        print("Goodbye!")
        exit()

    # Check if the user's input is in the list of possible responses
    if user_input in responses:
        # Generate a random response
        response = generate_response(user_input)
    else:
        # Use Google Search to find the answer
        results =search(user_input)
        # Print the first result
        response = results[0]

    # Print the response
    print(response)

    # Continue chatting
    chat()

# Start chatting
chat()
