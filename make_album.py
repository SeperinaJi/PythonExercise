def make_album(singer_name, album_name, song_number=''):
    album = {'singer' : singer_name, 'ablum' : album_name}
    if song_number:
        album['song number'] = song_number
    return album

album_0 = make_album('breatney','hello my lover')
print(album_0)

album_1 = make_album('justin', 'byebye')
print(album_1)

album_2 = make_album('john', 'brave', '1')
print(album_2)

while True:
    print("\nPlease Enter your album info:")
    print("(enter 'q' at any time to quit)")

    singer_info = input("Your singer : ")
    if singer_info == 'q':
        break

    album_info = input("Your album : ")
    if album_info == 'q':
        break

    albums = make_album(singer_info, album_info)
    print(albums)
