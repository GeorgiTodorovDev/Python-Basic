#Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes
#Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot

product = str(input())
result = ""

if product == "banana" or product == "apple" or product == "kiwi" \
    or product == "cherry" or product == "lemon" or product == "grapes":
    result = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" \
    or product == "carrot":
    result = "vegetable"
else:
    result = "unknown"

print(result)