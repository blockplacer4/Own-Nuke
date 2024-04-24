import random


async def random_message() -> str:
    mesages = ["Ciskyon", "Janosch", "Claralara", "Micha", "Michi", "Blockky", "Würgen", "NOT A PEDOPHILE", "Your Momma", "PedoHure"]
    return "nuked by - " + random.choice(mesages)
