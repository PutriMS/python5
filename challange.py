import random
import string
import os

i = 0
dicts = []
while True:
  print(''*15, '-INPUT DATA MAPEL-' , ''*15)

  datas = ('Mata pelajaran', 'Guru', 'Hari', 'Jam', 'Ruangan')
  data = dict.fromkeys(datas)

  data['Mata pelajaran'] = input('Mapel : ')
  data['Guru'] = input('Guru : ')
  data['Hari'] = input('Hari : ')
  data['Jam'] = input('Jam : ')
  data['Ruangan'] = input('Ruangan : ')

  lanjut = input("Lanjut (y/t)? ").lower()
  Id = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
  i += 1
  dicts.append({
    'Id': Id,
    'data': data,
  })

  if lanjut == 'y':
    print("-" * 20)
    os.system('cls')
    continue

  if lanjut == 't':
    print("=" * 65)
    print(f'{"ID":<10} {"Mata Pelajaran":<20} {"Guru":<12} {"Hari":<5} {"Jam":<5} {"Ruangan":<10}')
    print("=" * 65)
    for key, value in enumerate(dicts, start=1):
      print(f"MPL.{value['Id']:<5} {value['data']['Mata pelajaran']:<20} {value['data']['Guru']:<12} {value['data']['Hari']:<6} {value['data']['Jam']:<6} {value['data']['Ruangan']:<10}")
    break

  else:
    print("Tidak Valid")
    break