from os import environ 
environ.setdefault('PYTHON_DEFAULT',"Python Default")
print(f"value of 'MUST_BE_SET':'{environ['MUST_BE_SET']}'")
print(f"value of 'PYTHON_DEFAULT':'{environ['PYTHON_DEFAULT']}'")

try :
    print(f"Value of 'ALWAYS_OVERRRIDDEN' before override:'{environ['ALWAYS_OVERRRIDDEN']}'")

except KeyError:
    print("'ALWAYS_OVERRRIDDEN' was not set.")

environ["ALWAYS_OVERRRIDDEN"] = "Always Override In Python"
print(f"Value of 'ALWAYS_OVERRRIDDEN' after override:'{environ['ALWAYS_OVERRRIDDEN']}'")
print(f"Value of 'OPTIONAL':'{environ.get('OPTIONAL')}'")
