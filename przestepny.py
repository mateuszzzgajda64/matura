rok = int(input())
if(rok % 4 == 0) and (rok % 100 != 0):
    print('rok {} jest przestepny'.format(rok))
if(rok % 4 == 0) and (rok% 400 == 0):
    print('rok {} jest przestepny'.format(rok))
if(rok % 4 == 0) and (rok% 100 == 0) and (rok % 400 != 0):
    print('rok {} nie jest przestepny'.format(rok))
if(rok % 4 != 0):
    print('rok {} nie jest przestepny'.format(rok))
