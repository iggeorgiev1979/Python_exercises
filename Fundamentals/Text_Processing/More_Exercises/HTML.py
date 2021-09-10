print(f"""<h1>
    {input()}
</h1>""")
print(f"""<article>
    {input()}
</article>""")
text = input()
while not text == 'end of comments':
    print(f"""<div>
    {text}
</div>""")
    text = input()
