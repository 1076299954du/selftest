def story(**kwds):
    return 'jhfkhsf is a ' '{job} called {name}.'.format_map(kwds)


print(story(job='king', name='Gmby'))


def power(x , n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


print(power(2, 0))


