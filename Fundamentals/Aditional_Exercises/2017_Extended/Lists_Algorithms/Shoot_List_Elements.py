def average(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)


def decrement(list_of_numbers):
    return [x - 1 for x in list_of_numbers]


result_list = []
command = input()
last_element = None
boolean = True
while not command == 'stop':
    if command == 'bang' and len(result_list) > 0:
        for element in result_list:
            if element <= average(result_list):
                result_list.remove(element)
                print(f"shot {element}")
                last_element = element
                break
        result_list = decrement(result_list)
    elif command == 'bang' and len(result_list) == 0:
        print(f"nobody left to shoot! last one was {last_element}")
        boolean = False
        break
    else:
        result_list.insert(0, int(command))
    command = input()
if boolean:
    if len(result_list) > 0:
        print(f"survivors: {' '.join([str(x) for x in result_list])}")
    else:
        print(f'you shot them all. last one standing was {last_element}')
