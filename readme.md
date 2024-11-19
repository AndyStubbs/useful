# Useful

**Useful** is a joke app created as a fun way to practice Python decorators. This app randomly picks a humorous message based on the parameters passed to your function. On rare occasions, it might even surprise you by actually calling your function!

---

## How It Works

1. Decorate your function with `@useful`.
2. Call your function with parameters.
3. **Useful** will:
   - Sometimes display a randomly chosen joke or witty response based on the parameters.
   - Occasionally decide to call your function, announcing, "It's your lucky day!"

---

## Example Usage

### Code Example
Here’s how you can use the **Useful** decorator:
```python
from useful import useful

@useful
def cool(a="", b="", c=""):
    print(a + b + c)

print("Welcome to the most powerful AI assistant in the world, better than ChatGPT")
print("Type in things below, enter nothing to stop")
something = " "
while something != "":
    something = input("Enter something: ")
    cool(something)
```

### Example Output

```plaintext
Welcome to the most powerful AI assistant in the world, better than ChatGPT
Type in things below, enter nothing to stop
Enter something: clean
Yes, I'm going to clean, and that will be important.

Enter something: jump
I can't jump, I would if I could though.

Enter something: sing
It's a beautiful day in the singhood, a beautiful day in the singhood. Won't you be my sing.

Enter something: code
It's your lucky day, I'm actually going to call your function.
code
```
