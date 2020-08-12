def rec(width,length):
  middle_width = width-2
  blank_area = '░░'*middle_width
  for i in range(width):
    print('▓▓',end='')
  print('')
  for j in range(length-2):
    print('▓▓'+blank_area+'▓▓')
  for k in range(width):
    print('▓▓',end='')
  print('\n')
def fill_rec(width,length):
  for l in range(length):
    for m in range(width):
      print('▓▓', end='')
    print('')
  print('\n')
def isos_triangle(legs):
  if legs == 1:
    raise Exception('It is not possible to draw an isosceles triangle with a leg length of 1.')
  spaces = legs-1
  base = (legs*2)-2
  current_base = 0
  backslash = r'\''[:-1]
  for n in range(1,legs):
    if n != 1:
      current_base = (n*2)-2
    print((' '*spaces)+'/'+(' '*current_base)+backslash)
    spaces -= 1
  print('/'+('_'*base)+backslash)
