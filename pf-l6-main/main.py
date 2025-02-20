
'''this function must exist in your program,it should take one number as input, and it should output a dictionary of trivia about that number.'''

import json
import requests

def trivia_fetch(num):
  
        url = f"http://numbersapi.com/{num}?json"
        response = requests.get(url)

        data = json.loads(response.content)

        return {"number": num, "text": data["text"]}

def main():
    
    #Main function to run the trivia quiz.  
    num = int(input("Enter a number: "))
    print(trivia_fetch(num))
     

if __name__=="__main__":
  main()