# --- Demo of Tab

from PyTab import Tab

if __name__=='__main__':
  '''Example'''

  def f1():
    tab = Tab()
    tab1 = Tab()
    print(tab, 'In f1')

    for x in range(4):
      print(tab1, 'x=%g' % x)

    print(tab, 'Calling f2')
    f2()

  def f2():
    tab = Tab()
    print(tab, 'In f2')

  tab = Tab()
  print(tab, 'starting test')
  f1()
  print(tab, 'done test')
