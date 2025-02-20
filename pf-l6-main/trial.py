
'''this function must exist in your program,
it should take one number as input, and it should output a dictionary of trivia about that number.'''

import json
import requests

def trivia_fetch(number):
    url = f'''http://numbersapi.com/{number}?json'''
    response = requests.get(url)
    
    trivia= json.loads(response.content)
    print(trivia)

# Calling the function
number = 1000
print(trivia_fetch(number))
import urllib.request

def trivia_fetch(num):

    
    try:
        url = f"http://numbersapi.com/{num}?json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        return {"number": num, "text": data["text"]}
    except urllib.error.URLError as e:
        print(f"Error fetching trivia for {num}: {e}")
        return {"number": num, "text": "Could not retrieve trivia."}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for {num}: {e}")
        return {"number": num, "text": "Could not retrieve trivia."}

def main():
    """
    Main function to run the trivia quiz.
    """
    #for i in range(1): # Keep it simple for the rewrite.
    num = int(input(f"\nEnter a number: "))
    trivia = trivia_fetch(num)
    print(trivia['text']) # Just print the trivia for simplicity


    print("Thanks for playing!")

if __name__=="__main__":
  main()
  def trivia_fetch(number):
    url = f'''http://numbersapi.com/{number}?json'''
    response = requests.get(url)
    
    trivia= json.loads(response.content)
    print(trivia)

# Calling the function
number = 1000
print(trivia_fetch(number))