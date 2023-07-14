from fastapi import FastAPI
import random
#instance of FasctAPI class
app = FastAPI()
#Function to reads facts file and display randomly
def read_facts():
    with open('facts.txt', 'r') as file:
        facts = [line.strip() for line in file]
    return facts
facts_list = read_facts()
#Function to displayfacts fom  facts.txt file randomly
@app.get('/facts')
def read_random_fact():
    random_fact = random.choice(facts_list)
    return{'fact': random_fact}
@app.post('/add')
def add_fact(new_fact: str):
    with open('facts.txt', 'a') as file:
        file.write(new_fact + "\n")
    return {"message": "Fact added successfully."}
