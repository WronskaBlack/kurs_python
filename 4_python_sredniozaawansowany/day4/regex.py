import re

# print(re.search(r"[A-Z]la", "ala Ola Ela"))
# print(re.match(r"[A-Z]la", "Ola Ela"))
# print(re.fullmatch(r"[A-Z]la", "Ela"))
# print(re.findall(r".la", "ala Ola Ela"))
# iter = re.finditer(r".la", "Ola ala Ela")
# for i in iter:
#     print(i)
# print(re.split(r",|\.", "apple,pear.grapes,carrot.cabbage"))
# print(re.sub(r"[a-z]{4}", "psa", "Ala ma kota i port"))
# print(re.subn(r"[a-z]{4}", "psa", "Ala ma kota i port"))
#
# text = "Tomasz W. (33 l.), widziany ostatnio w Krakowie"
# pattern = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+) l\.\)"
# match = re.search(pattern, text)
# print(match)
# print(match.groups())
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))
#
# text = "Tomasz (33 l.) i Ela (24 l.), widziani ostatnio w Krakowie"
# pattern = r"([A-Z]{1}[a-z]+) \((\d+) l\.\)"
# print(re.findall(pattern, text))


# pattern = r"[a-z0-9_\-\.]*@[a-z0-9_\-\.]*\.[a-z0-9_\-]*"
# text = "Kamil kamil@google.com, Tomek tomek@o2.pl, Ania ania-nowak@o2.pl, Kamil kamil.borowski@poczta.onet.pl, Anna .anna@anna.com."
# print(re.findall(pattern, text))

# text = "jan@onremove_thiset.pl"
# pattern = r"remove_this"
# start, stop = re.search(pattern, text).span()
# text = text[:start] + text[stop:]
# print(text)

# text = "It's in the frakking ship!"
# profanity = 'frakking'
# print(re.sub(profanity, "*" * len(profanity), text))

# text = "Nie lubię w poniedziałki wcześnie wstawać"
# pattern = r"\b[\S]{1,7}\b"
# match = re.findall(pattern, text)
# print(match)

def is_real(number):
    pattern = r"[789][0-9]{8}"
    return bool(re.fullmatch(pattern, number))

# print(is_real('845367865'))
# print(is_real('8453678654'))
# print(is_real('745367854'))
# print(is_real('945367654'))
# print(is_real('945368s54'))

# text = "Ala a kota i lubi esport."
# pattern = r"\b[aeAE][\w]*"
# print(re.findall(pattern, text))

# text = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
# pattern = r"[aeiouyAEIOUY]{2,}"
# print(re.findall(pattern, text))

def is_divisible_4(number):
    pattern = r"-?(\d*[13579][26]|(\d*[02468])?[048])"
    return bool(re.fullmatch(pattern, number))

# print(is_divisible_4("8"))
# print(is_divisible_4("42"))
# print(is_divisible_4("757465"))
# print(is_divisible_4("2036"))
# print(is_divisible_4("1100"))
# print(is_divisible_4("-12"))
# print(is_divisible_4("36"))




# text = '2020-10-02'
# pattern = r"(\d{4})\-(\d{2})\-(\d{2})"
# match = re.match(pattern, text)
# year, month, day = match.groups()
# print(year, month, day)


text = "SZczecin, POlska, Japonia IT, WW"
def replace_second_upper(text):
    pattern = r"\b([A-Z])([A-Z])(\w+)"
    new_text = re.sub(pattern, lambda m: m.group(1) + m.group(2).lower() + m.group(3), text)
    pattern = r"\b([A-Z])([A-Z])\b"
    for i in re.finditer(pattern, new_text):
        st, end = i.span()
        print(f"Do yo want to repalace {new_text[st:end]}?")
        yes = input()
        if yes == 'y':
            new_new_text = new_text[:st+1] + new_text[st+1].lower() + new_text[end:]
    return new_new_text
# print(replace_second_upper(text))