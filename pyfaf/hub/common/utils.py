import datetime
import types

from django.core.paginator import Paginator, EmptyPage, InvalidPage

def split_distro_release(inp):
    '''
    Returns decomposed distro, release names.

    fedora results in (fedora, fedora) meaning all releases,
    fedora-17 results in (fedora, 17).
    '''
    distro = release = inp
    if '-' in inp:
        split = inp.split('-')
        distro = split[0]
        release = ''.join(split[1:])

    return (distro, release)

def paginate(objects, request):
    '''
    Pagination short hand function
    '''
    paginator = Paginator(objects, 200)
    try:
        page = int(request.GET.get('page'))
    except (ValueError, TypeError):
        page = 1

    try:
        objs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        objs = paginator.page(paginator.num_pages)

    return objs

def date_iterator(first_date, time_unit='d', end_date=None):
    '''
    Iterates from date until reaches end date or never finishes
    '''
    if time_unit == 'd':
        next_date_fn = lambda x : x + datetime.timedelta(days=1)
    elif time_unit == 'w':
        first_date -= datetime.timedelta(days=first_date.weekday())
        next_date_fn = lambda x : x + datetime.timedelta(weeks=1)
    elif time_unit == 'm' or time_unit == '*':
        first_date = first_date.replace(day=1)
        next_date_fn = lambda x : (x.replace(day=25) +
            datetime.timedelta(days=7)).replace(day=1)
    else:
        raise ValueError('Unknown time unit type : "%s"' % time_unit)

    toreturn = first_date
    yield toreturn
    while True:
        toreturn = next_date_fn(toreturn)
        if not end_date is None and toreturn > end_date:
            break

        yield toreturn

def unique(seq, idfun=None):
    '''
    Return unique values of `seq` with preserved order.

    idfun can be used to specify unique part of the item (useful for tuples).
    '''
    if idfun is None:
        idfun = lambda x: x[0]
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    if ltype == types.GeneratorType:
        return l
    return ltype(l)
