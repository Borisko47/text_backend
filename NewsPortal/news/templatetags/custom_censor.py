from django import template

register = template.Library()

CENSOR_WORDS = ['редиска', 'морковка', 'свекла']


@register.filter()
def filter_message(value):
    ln = len(CENSOR_WORDS)
    filtred_message = ''
    string = ''
    if isinstance(value, str):
        for i in value:
            string += i
            string2 = string.lower()

            flag = 0
            for j in CENSOR_WORDS:
                if not string2 in j:
                    flag += 1
                if string2 == j:
                    filtred_message += string2.replace(string2[1:], '*' * len(string2[1:]))
                    flag -= 1
                    string = ''

            if flag == ln:
                filtred_message += string
                string = ''

        if string2 != '' and string2 not in CENSOR_WORDS:
            filtred_message += string
        elif string2 != '':
            filtred_message += string2.replace(string2[1:], '*' * len(string2[1:]))

        return filtred_message
    else:
        raise TypeError("Мы тут со строками работаем")