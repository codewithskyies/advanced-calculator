import math

def calculator():
    print("🔢 Advanced Python Calculator")
    print("Type 'exit' to quit")
    print("You can use operators: +, -, *, /, %, **, //")
    print("Functions: sin(x), cos(x), tan(x), log(x), sqrt(x), factorial(x)")

    while True:
        expr = input("\nEnter expression: ")

        if expr.lower() == "exit":
            print("Exiting calculator... Goodbye! ")
            break

        try:
    
            allowed = {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,   
                "sqrt": math.sqrt,
                "factorial": math.factorial,
                "pi": math.pi,
                "e": math.e
            }

            result = eval(expr, {"__builtins__": None}, allowed)
            print("Result =", result)

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    calculator()
