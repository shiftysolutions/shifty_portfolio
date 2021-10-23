import string
import random
import re

def generate_numbers(string_length=10) :
    assembly = string.digits
    return ''.join(random.choice(assembly) for i in range(string_length))

def generate_reference(model_name, ref_len):
    reference = None
    while True:
        random = generate_numbers(ref_len)
        if model_name.objects.filter(reference=random).exists():
            continue
        reference = random
        break
    return reference
