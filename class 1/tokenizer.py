import tiktoken 

encoder = tiktoken.encoding_for_model('gpt-4o')

text = "i am the intelligent boy learning gen ai"
token  = encoder.encode(text)

print ("token", token)

decode  = encoder.decode([72, 939, 290, 32075, 8473, 7524, 3645, 8440])

print("decoder",  decode)
