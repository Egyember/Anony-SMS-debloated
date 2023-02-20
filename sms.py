import requests

print('1: Send sms\n2: Help!')


choices = input("\nPlease choice[1]: ")

def SMS():
    smsnumb = input("Input the number of the target: ")
    message = input("Please input the message: ")

    resp = requests.post('https://textbelt.com/text', {
        'phone': f'{smsnumb}',
        'message': f'{message}',
        'key': 'textbelt',
    })

    print(resp.json())
    return(0)

if choices == "2":
    print(
        "Your phone number was not provided in E.164 format: you need to input the country code ex.+91"
    )
    print(lines)
    print(
        "Only one test text message is allowed per day: you can't send more than one message per day, however you could use vpn"
    )
    print(lines)
    print(
        "Else: please contact hyprid tech in github or youtube (the original bloated version's creator)"
    )

else:    
    SMS()
