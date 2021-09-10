class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


list_of_messages = []
txt = input().split()
while not txt[0] == 'Stop':
    message = Email(txt[0], txt[1], txt[2])
    list_of_messages.append(message)
    txt = input().split()
is_sent_list = list(map(lambda x: int(x), input().split(', ')))
for i in is_sent_list:
    list_of_messages[i].send()
for j in list_of_messages:
    print(j.get_info())
