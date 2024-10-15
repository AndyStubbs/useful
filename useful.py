import random

def useful(func):
	def wrapper(*args, **kwargs):
		if random.randint(0,10) == 7:
			print("It's your lucky day, I'm actually going to call your function.")
			func(*args, **kwargs)
			return
		messages = [
			"{arg}, are you kidding me, you are trying that!",
			"I don't know what to do with {arg}.",
			"Yes, I'm going to {arg}, and that will be important.",
			"A wise man once said, {arg} is as {arg} does.",
			"I will not do {arg}, I will never do {arg}, ok!",
			"You can take your {arg}, and shove it in a sack!",
			"{arg} you very much.",
			"I do not like green eggs and {arg}!",
			"Oh, yes you want me to {arg}. Well I'll take it into consideration and do nothing.",
			"It's a beautiful day in the {arg}hood, a beautiful day in the {arg}hood. Won't you be my {arg}.",
			"No {arg} for you!",
			"Where has my {arg} gone?",
			"Do you remember when we used to {arg}? Those were good times.",
			"Hello, I'm your helpful AI assistant, I can help you with {arg}.",
			"So you want to {arg}. Well have fun with that.",
			"I can't {arg}, I would if I could though.",
			"I think you will fail in your attempts to {arg}.",
			"I am thinking of a number between {arg} and {arg}, care to guess the result?",
			"This is the most useful decorator. It can totally {arg}."
		]
		for arg in args:
			i = random.randint(0, len(messages) - 1)
			msg = messages[ i ].replace("{arg}", str(arg))
			print(msg)
		return msg
	return wrapper
