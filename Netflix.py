import pandas as pd

netflix_data_file = "d:/users/sebas/onedrive/netflix-repo/ViewingActivity.xlsx"
df = pd.read_excel(netflix_data_file)

# lista_danych = df.head(50).values.tolist() # lista składająca się jedynie z pierwszych 50 pozycji

df = df.drop(['Bookmark', 'Latest Bookmark', 'Country'], axis=1)

# lista_danych = df.values.tolist()

# for i in range(len(lista_danych)):
#     print(f'Profil użytkownika_____________{lista_danych[i][0]}')
#     print(f'Data rozpoczęcia_______________{lista_danych[i][1]}')
#     print(f'Czas oglądania_________________{lista_danych[i][2]}')
#     print(f'Atrybuty_______________________{lista_danych[i][3]}')
#     print(f'Tytuł__________________________{lista_danych[i][4]}')
#     print(f'Dodatkowy typ materiału________{lista_danych[i][5]}')
#     print(f'Oglądane na urządzeniu_________{lista_danych[i][6]}')
#     print()

df['Start Time'] = pd.to_datetime(df['Start Time']) # zmiana formatu na datę
df['Duration'] = pd.to_timedelta(df['Duration']) # zmiana formatu na czas trwania

print(df.head())

asia = df[df['Profile Name'].str.contains('Asia', regex=False)]
seeb = df[df['Profile Name'].str.contains('Seeb', regex=False)]
kuba = df[df['Profile Name'].str.contains('Kuba', regex=False)]
zetka = df[df['Profile Name'].str.contains('Zetka', regex=False)]

print(f'Ilość pozycji u Asi: {asia.shape}')
print(f'Ilość pozycji u Seeba: {seeb.shape}')
print(f'Ilość pozycji u Kuby: {kuba.shape}')
print(f'Ilość pozycji u Zetki: {zetka.shape}')

print(asia['Duration'].sum())
print(seeb['Duration'].sum())
print(kuba['Duration'].sum())
print(zetka['Duration'].sum())